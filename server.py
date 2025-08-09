#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import urllib.parse
import os
import sys
from darwin_scraper import DarwinScraper
from species_processor import SpeciesProcessor

class DarwinHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/scrape':
            self.handle_scrape_request()
        elif self.path == '/api/search-species':
            self.handle_species_search()
        elif self.path == '/api/search-species-complete':
            self.handle_species_search_complete()
        else:
            self.send_error(404, "Not Found")
    
    def handle_scrape_request(self):
        try:
            # Leer el cuerpo de la solicitud
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            category = data.get('category')
            subcategory = data.get('subcategory')
            subcategory_name = data.get('subcategoryName')
            mode = data.get('mode', 'test')
            
            print(f"Procesando solicitud: {category} -> {subcategory} ({subcategory_name})")
            
            # Crear instancia del scraper
            scraper = DarwinScraper(test_mode=(mode == 'test'))
            result = scraper.scrape_category(category, subcategory, subcategory_name)
            
            # Enviar respuesta
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps(result)
            self.wfile.write(response.encode('utf-8'))
            
        except Exception as e:
            print(f"Error procesando solicitud: {e}")
            self.send_error(500, f"Internal Server Error: {str(e)}")
    
    def handle_species_search(self):
        """Maneja las búsquedas específicas de especies"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            category = data.get('category')
            species_name = data.get('speciesName')
            
            print(f"Buscando especie: {species_name} en categoría: {category}")
            
            processor = SpeciesProcessor()
            result = processor.search_species(category, species_name)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps(result)
            self.wfile.write(response.encode('utf-8'))
            
        except Exception as e:
            print(f"Error en búsqueda de especies: {e}")
            self.send_error(500, f"Internal Server Error: {str(e)}")
    
    def handle_species_search_complete(self):
        """Maneja las búsquedas completas de especies (scraping + procesamiento)"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            species_name = data.get('speciesName')
            test_mode = data.get('testMode', False)
            
            print(f"Búsqueda completa de especie: {species_name} (test_mode: {test_mode})")
            
            processor = SpeciesProcessor()
            # Cambiar esta línea para usar el método correcto con Gemini
            result = processor.search_species_complete_with_gemini(species_name)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps(result)
            self.wfile.write(response.encode('utf-8'))
            
        except Exception as e:
            print(f"Error en búsqueda completa de especies: {e}")
            self.send_error(500, f"Internal Server Error: {str(e)}")
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DarwinHTTPRequestHandler)
    print(f"Servidor iniciado en http://localhost:{port}")
    print("Presiona Ctrl+C para detener el servidor")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nDeteniendo servidor...")
        httpd.server_close()

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    run_server(port)