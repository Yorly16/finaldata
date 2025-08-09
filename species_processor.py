#!/usr/bin/env python3
import csv
import io
import os
import requests
import json
from darwin_scraper import DarwinScraper

class SpeciesProcessor:
    def __init__(self):
        self.scraper = DarwinScraper()
        # IMPORTANTE: Reemplaza con tu clave real de Google Gemini
        self.gemini_api_key = "AIzaSyB5r4LUJIwWmU7Cj8uN9Q51vjANLr6H0MY"  
        self.gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent"
    
    def read_csv_with_encoding(self, csv_path):
        """Lee un archivo CSV probando múltiples codificaciones"""
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1', 'utf-16']
        
        for encoding in encodings:
            try:
                with open(csv_path, 'r', encoding=encoding) as file:
                    content = file.read()
                print(f"[LOG] Archivo leído exitosamente con codificación: {encoding}")
                return content, encoding
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"[LOG] Error con codificación {encoding}: {str(e)}")
                continue
        
        raise Exception(f"No se pudo leer el archivo {csv_path} con ninguna codificación probada")

    def analyze_csv_with_gemini(self, csv_path, species_name):
        """Analiza el CSV usando Google Gemini API para extraer información de especies"""
        try:
            # Leer el contenido del CSV con múltiples codificaciones
            csv_content, used_encoding = self.read_csv_with_encoding(csv_path)
            print(f"[LOG] Usando codificación: {used_encoding}")
            
            # Limpiar y limitar el contenido del CSV
            max_chars = 2000  # Reducir aún más el límite
            if len(csv_content) > max_chars:
                lines = csv_content.split('\n')
                header = lines[0] if lines else ""
                sample_lines = lines[1:15] if len(lines) > 1 else []  # Menos líneas
                csv_content = header + '\n' + '\n'.join(sample_lines)
            
            # Limpiar caracteres problemáticos
            csv_content = csv_content.replace('"', '\"').replace('\n', '\\n').replace('\r', '')
            
            # Crear el prompt para Gemini con todos los campos específicos
            prompt = f"""Analiza este CSV de especies de Galápagos y busca información sobre: {species_name}

CSV: {csv_content[:1500]}  

Devuelve SOLO un JSON con este formato exacto, incluyendo TODOS los campos disponibles:
{{
  "found": true,
  "species_info": {{
    "Nombre Común en Español": "valor del spanish common name",
    "Nombre Común en Inglés": "valor del english common name",
    "Género": "valor del genus",
    "Epíteto Específico": "valor del Specific Epithet",
    "Estado UICN": "valor del IUCN Status",
    "Hábitat": "valor de Spanish Distribution Comments",
    "Islas de Presencia": "todas las islas de la región que digan true (separadas por coma)",
    "Descripción (Español)": "valor de Spanish Description",
    "Descripción (Inglés)": "valor de English Description",
    "Amenazas": "valor de Spanish Comments (separadas por coma)"
  }}
}}

Busca en TODAS las columnas del CSV. Si algún campo no está disponible, usa "No disponible".
Si no encuentras la especie, devuelve: {{"found": false}}"""
            
            # Preparar la solicitud para Gemini
            headers = {
                'Content-Type': 'application/json'
            }
            
            # Agregar la API key como parámetro de URL
            url_with_key = f"{self.gemini_url}?key={self.gemini_api_key}"
            
            data = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }],
                "generationConfig": {
                    "temperature": 0.1,
                    "maxOutputTokens": 1000
                }
            }
            
            # Llamar a Gemini API
            try:
                response = requests.post(
                    url_with_key,
                    headers=headers,
                    json=data,
                    timeout=30
                )
                
                print(f"[DEBUG] Status code: {response.status_code}")
                print(f"[DEBUG] Response: {response.text[:500]}")
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    # Extraer el texto de la respuesta
                    if 'candidates' in response_data and len(response_data['candidates']) > 0:
                        candidate = response_data['candidates'][0]
                        if 'content' in candidate and 'parts' in candidate['content']:
                            text_response = candidate['content']['parts'][0]['text']
                            
                            # Intentar extraer JSON de la respuesta
                            import re
                            json_match = re.search(r'\{.*\}', text_response, re.DOTALL)
                            if json_match:
                                json_str = json_match.group(0)
                                result = json.loads(json_str)
                                return result
                            else:
                                return {
                                    "found": False,
                                    "error": "No se pudo extraer JSON de la respuesta de Gemini",
                                    "raw_response": text_response[:500]
                                }
                        else:
                            return {
                                "found": False,
                                "error": "Estructura de respuesta inesperada de Gemini",
                                "response_data": response_data
                            }
                    else:
                        return {
                            "found": False,
                            "error": "No hay candidatos en la respuesta de Gemini",
                            "response_data": response_data
                        }
                        
                elif response.status_code == 400:
                    return {
                        "found": False,
                        "error": f"Solicitud inválida a Gemini API (400): {response.text[:200]}",
                        "details": response.text
                    }
                elif response.status_code == 401:
                    return {
                        "found": False,
                        "error": "API Key inválida para Gemini (401)",
                        "details": response.text
                    }
                elif response.status_code == 429:
                    return {
                        "found": False,
                        "error": "Límite de rate excedido en Gemini (429)",
                        "details": response.text
                    }
                else:
                    return {
                        "found": False,
                        "error": f"Error HTTP {response.status_code} de Gemini",
                        "details": response.text
                    }
                    
            except requests.exceptions.Timeout:
                return {
                    "found": False,
                    "error": "Timeout al conectar con Gemini API"
                }
            except requests.exceptions.ConnectionError:
                return {
                    "found": False,
                    "error": "Error de conexión con Gemini API"
                }
            except Exception as api_error:
                return {
                    "found": False,
                    "error": f"Error de API Gemini: {str(api_error)}"
                }
                
        except FileNotFoundError:
            return {
                "found": False,
                "error": f"Archivo CSV no encontrado: {csv_path}"
            }
        except json.JSONDecodeError as json_error:
            return {
                "found": False,
                "error": f"Error al parsear JSON de Gemini: {str(json_error)}"
            }
        except Exception as e:
            return {
                "found": False,
                "error": f"Error general al analizar con Gemini: {str(e)}"
            }
    
    def search_csv_simple(self, csv_path, species_name):
        """Búsqueda simple en CSV como respaldo"""
        try:
            # Usar la función de lectura con múltiples codificaciones
            csv_content, used_encoding = self.read_csv_with_encoding(csv_path)
            print(f"[LOG] Método de respaldo usando codificación: {used_encoding}")
            
            # Convertir el contenido a un objeto StringIO para csv.DictReader
            csv_file = io.StringIO(csv_content)
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                spanish_name = row.get('Spanish Common Name', '').lower()
                english_name = row.get('English Common Name', '').lower()
                
                if (species_name.lower() in spanish_name or 
                    species_name.lower() in english_name):
                    
                    return {
                        "found": True,
                        "species_info": {
                            "Nombre Común en Español": row.get('Spanish Common Name', ''),
                            "Nombre Común en Inglés": row.get('English Common Name', ''),
                            "Género": row.get('Genus', ''),
                            "Epíteto Específico": row.get('Specific Epithtet', ''),
                            "Estado UICN": row.get('IUCN Status', ''),
                            "Hábitat": row.get('Spanish Distribution Comments', ''),
                            "Islas de Presencia": "Información no disponible",
                            "Descripción (Español)": row.get('Spanish Description', ''),
                            "Descripción (Inglés)": row.get('English Description', ''),
                            "Amenazas": row.get('Spanish Comments', '')
                        }
                    }
                    
            return {"found": False, "error": "Especie no encontrada en CSV"}
            
        except Exception as e:
            return {"found": False, "error": f"Error al leer CSV: {str(e)}"}
    
    def search_species_complete_with_gemini(self, species_name):
        """Búsqueda completa de una especie usando Gemini para análisis"""
        try:
            # Paso 1: Realizar scraping usando DarwinScraper
            scraping_result = self.scraper.search_species_direct(species_name)
            
            if not scraping_result['success']:
                return scraping_result
            
            # Paso 2: Procesar el CSV descargado
            if not scraping_result['csv_files']:
                return {
                    'success': False,
                    'error': 'No se descargaron archivos CSV'
                }
            
            # Obtener la ruta del primer archivo CSV
            csv_filename = scraping_result['csv_files'][0]
            csv_path = os.path.join('downloads', scraping_result['category'], csv_filename)
            
            # Paso 3: Intentar analizar con Gemini
            gemini_result = self.analyze_csv_with_gemini(csv_path, species_name)
            
            # Si Gemini falla, usar método simple de respaldo
            if not gemini_result.get('found', False):
                print(f"Gemini falló: {gemini_result.get('error', 'Error desconocido')}")
                print("Intentando con método de respaldo...")
                
                backup_result = self.search_csv_simple(csv_path, species_name)
                if backup_result.get('found', False):
                    return {
                        'success': True,
                        'species_name': species_name,
                        'category': scraping_result['category'],
                        'species_info': backup_result['species_info'],
                        'csv_file': csv_filename,
                        'analysis_method': 'backup_simple',
                        'gemini_error': gemini_result.get('error', 'Error desconocido')
                    }
                else:
                    return {
                        'success': False,
                        'error': f"Ni Gemini ni el método de respaldo encontraron la especie '{species_name}'",
                        'gemini_error': gemini_result.get('error', 'Error desconocido'),
                        'backup_error': backup_result.get('error', 'Error desconocido')
                    }
            
            species_info = gemini_result['species_info']
            
            return {
                'success': True,
                'species_name': species_name,
                'category': scraping_result['category'],
                'species_info': species_info,
                'csv_file': csv_filename,
                'analysis_method': 'gemini'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Error en el procesamiento: {str(e)}'
            }

# Función de utilidad para uso directo con Gemini
def search_and_process_species_with_gemini(species_name):
    """Función de conveniencia para búsqueda completa con Gemini"""
    processor = SpeciesProcessor()
    return processor.search_species_complete_with_gemini(species_name)

# Ejemplo de uso directo
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        species_name = ' '.join(sys.argv[1:])
        print(f"Procesando especie con Gemini: {species_name}")
        
        # Usar Gemini para análisis
        result = search_and_process_species_with_gemini(species_name)
        
        if result['success']:
            print(f"\n✓ Especie encontrada: {result['species_name']}")
            print(f"✓ Categoría: {result['category']}")
            print(f"✓ Archivo CSV: {result['csv_file']}")
            print(f"✓ Método de análisis: {result['analysis_method']}")
            print("\n=== INFORMACIÓN DE LA ESPECIE (GEMINI) ===")
            
            for key, value in result['species_info'].items():
                if value:
                    print(f"{key}: {value}")
        else:
            print(f"✗ Error: {result.get('error', 'Error desconocido')}")
    else:
        print("Uso: python species_processor.py <nombre_de_especie>")
        print("Ejemplo: python species_processor.py 'Patillo'")