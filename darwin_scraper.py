#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
import json
import urllib.parse
from pathlib import Path
import time
import re

class DarwinScraper:
    def __init__(self, test_mode=False):
        self.base_url = "https://datazone.darwinfoundation.org"
        self.checklist_url = "https://datazone.darwinfoundation.org/es/checklist/checklists-archive"
        self.test_mode = test_mode
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Base de datos de especies por categoría
        self.species_database = {
            'anfibios': [
                'Sapo común',
                'Rana de árbol'
            ],
            'aves': [
                'gavilán de Galápagos',
                'aguila pescadora',
                'Patillo',
                'Pato Cuchara Norteño',
                'Cerceta colorada (canela)',
                'Cerceta aliazul',
                'Piquero Peruano'
            ],
            'peces': [
                'anguilla moteada gigante',
                'morena falso de dos colores',
                'morena menuda',
                'morena boca de gancho, morena mosaico',
                'morena quijada delgada, morena kuijada esbelto',
                'morena cebra',
                'morena errante',
                'pargo amarillo'
            ],
            'mamiferos': [
                'ganado vacuno',
                'Chivo, Cabra',
                'Ovejuno',
                'Cerdo, chancho, puerco, marrano, porcino, cochinito, lechón.',
                'Perro doméstico, Canino.',
                'Felino, Gato doméstico',
                'Mono cabeza de algodón',
                'Humano moderno',
                'cuy',
                'Rata de Santa Fe',
                'Rata de San Cristóbal',
                'Rata gigante de Santa Cruz e Isabela',
                'Rata Noruega, Rata de Noruega, Rata gris',
                'Rata negra, rata de barco, rata de tejado, rata común, pericote, rata de buque, rata de barco.'
            ],
            'reptiles': [
                'culebra de Galápagos',
                'culebra de Española',
                'culebra slevini',
                'culebra dorsalis',
                'Salamanquesa o Gecko enano',
                'Gecko de casa o común',
                'Gecko de luto',
                'gecko barringtonensis',
                'gecko bauri',
                'tortuga de Alcedo',
                'Tortuga de Cerro Azul',
                'Tortuga de Rábida'
            ]
        }
        
        # Mapeo de categorías a términos de búsqueda en la página web
        self.category_search_terms = {
            'anfibios': ['amphibia', 'anfibios', 'sapo', 'rana'],
            'aves': ['aves', 'bird', 'gavilán', 'águila', 'pato', 'cerceta', 'piquero'],
            'peces': ['pisces', 'peces', 'fish', 'anguila', 'morena', 'pargo'],
            'mamiferos': ['mammalia', 'mamíferos', 'mammals', 'rata', 'ratón', 'ganado', 'perro', 'gato'],
            'reptiles': ['reptilia', 'reptiles', 'culebra', 'gecko', 'tortuga', 'salamanquesa']
        }
        
    def log(self, message):
        """Log messages para debugging"""
        print(f"[LOG] {message}")
        
    def find_species_category(self, species_name):
        """Encuentra la categoría de una especie específica"""
        species_lower = species_name.lower().strip()
        
        for category, species_list in self.species_database.items():
            for species in species_list:
                species_clean = species.lower().strip()
                # Búsqueda exacta o parcial
                if (species_lower == species_clean or 
                    species_lower in species_clean or 
                    species_clean in species_lower):
                    self.log(f"Especie '{species_name}' encontrada en categoría: {category}")
                    return category
        
        self.log(f"Especie '{species_name}' no encontrada en la base de datos")
        return None
    
    def search_species_direct(self, species_name):
        """Busca una especie específica realizando scraping automático"""
        self.log(f"Iniciando búsqueda directa para: {species_name}")
        
        # Encontrar la categoría de la especie
        category = self.find_species_category(species_name)
        if not category:
            return {
                'success': False,
                'error': f'Especie "{species_name}" no encontrada en la base de datos',
                'species_name': species_name
            }
        
        # Realizar scraping de la categoría
        scraping_result = self.scrape_category_for_species(category, species_name)
        
        return scraping_result
    
    def scrape_category_for_species(self, category, species_name):
        """Realiza el scraping de una categoría específica para encontrar una especie"""
        self.log(f"Realizando scraping para categoría: {category}")
        
        # Crear directorio para descargas
        download_dir = os.path.join('downloads', category)
        os.makedirs(download_dir, exist_ok=True)
        
        results = {
            'success': False,
            'category': category,
            'species_name': species_name,
            'files_found': 0,
            'files_downloaded': 0,
            'csv_files': [],
            'download_results': []
        }
        
        # Si estamos en modo de prueba, crear archivos de prueba
        if self.test_mode:
            self.log("Modo de prueba activado")
            test_files = self.create_test_csv(download_dir, category)
            results['success'] = True
            results['files_found'] = len(test_files)
            results['files_downloaded'] = len(test_files)
            results['csv_files'] = [f['filename'] for f in test_files]
            results['download_results'] = test_files
            return results
        
        # Obtener contenido de la página principal
        html_content = self.get_page_content(self.checklist_url)
        if not html_content:
            results['error'] = 'No se pudo obtener el contenido de la página principal'
            return results
        
        # Encontrar enlaces CSV para la categoría
        csv_links = self.find_csv_links_for_category(html_content, category)
        results['files_found'] = len(csv_links)
        
        if not csv_links:
            results['error'] = f'No se encontraron archivos CSV para la categoría {category}'
            return results
        
        # Descargar el primer CSV encontrado (como especificaste)
        csv_link = csv_links[0]
        download_result = self.download_csv(csv_link['url'], download_dir)
        results['download_results'].append(download_result)
        
        if download_result['success']:
            results['files_downloaded'] = 1
            results['csv_files'] = [download_result['filename']]
            results['success'] = True
            self.log(f"CSV descargado exitosamente: {download_result['filename']}")
        else:
            results['error'] = f"Error al descargar CSV: {download_result.get('error', 'Error desconocido')}"
        
        return results
    
    def get_page_content(self, url):
        """Obtiene el contenido HTML de una página"""
        try:
            self.log(f"Obteniendo contenido de: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            self.log(f"Respuesta exitosa: {response.status_code}")
            return response.text
        except requests.RequestException as e:
            self.log(f"Error al obtener la página {url}: {e}")
            return None
    
    def find_csv_links_for_category(self, html_content, category):
        """Encuentra enlaces CSV específicos para una categoría"""
        soup = BeautifulSoup(html_content, 'html.parser')
        csv_links = []
        
        # Obtener términos de búsqueda para la categoría
        search_terms = self.category_search_terms.get(category, [category])
        self.log(f"Buscando CSV con términos: {search_terms}")
        
        # Buscar divs con clase 'checklist'
        checklist_divs = soup.find_all('div', class_='checklist')
        self.log(f"Encontrados {len(checklist_divs)} divs con clase 'checklist'")
        
        for div in checklist_divs:
            # Buscar el encabezado h4 dentro del div
            header = div.find('h4')
            if not header:
                continue
                
            header_text = header.get_text().lower()
            
            # Verificar si el encabezado contiene algún término de la categoría
            if any(term.lower() in header_text for term in search_terms):
                self.log(f"¡Coincidencia encontrada en encabezado: {header_text}!")
                
                # Buscar enlaces CSV dentro de este div
                csv_elements = div.find_all('a', href=True)
                for link in csv_elements:
                    href = link['href']
                    if href.endswith('.csv') or 'csv' in href.lower():
                        # Construir URL completa
                        if href.startswith('http'):
                            full_url = href
                        else:
                            full_url = urllib.parse.urljoin(self.base_url, href)
                        
                        # Evitar duplicados
                        if not any(p['url'] == full_url for p in csv_links):
                            self.log(f"Encontrado enlace CSV: {full_url}")
                            csv_links.append({
                                'url': full_url,
                                'filename': os.path.basename(full_url)
                            })
                            # Solo tomar el primer CSV como especificaste
                            break
                
                # Si encontramos un CSV, salir del bucle
                if csv_links:
                    break
        
        self.log(f"Encontrados {len(csv_links)} enlaces CSV para {category}")
        return csv_links
    
    def download_csv(self, url, output_dir):
        """Descarga un archivo CSV"""
        try:
            self.log(f"Descargando CSV: {url}")
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            # Extraer nombre del archivo de la URL
            filename = os.path.basename(url)
            if not filename.endswith('.csv'):
                filename += '.csv'
            
            filepath = os.path.join(output_dir, filename)
            
            # Guardar el archivo
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            self.log(f"CSV descargado exitosamente: {filepath}")
            return {
                'success': True,
                'filename': filename,
                'path': filepath
            }
        except Exception as e:
            self.log(f"Error al descargar CSV {url}: {e}")
            return {
                'success': False,
                'filename': os.path.basename(url),
                'error': str(e)
            }
    
    def create_test_csv(self, download_dir, category):
        """Crea un archivo CSV de prueba"""
        os.makedirs(download_dir, exist_ok=True)
        
        filename = f"test_{category}_checklist.csv"
        filepath = os.path.join(download_dir, filename)
        
        # Crear contenido CSV de prueba
        csv_content = '''spanish common name,english common name,genus,specific epithet,iucn status,spanish distribution comments,spanish description,english description,spanish comments,baltra,bartolome,darwin,espanola,fernandina,floreana,genovesa,isabela,marchena,pinta,pinzon,rabida,san_cristobal,santa_cruz,santa_fe,santiago,seymour_norte,wolf
Sapo común,Common Toad,Rhinella,marina,Least Concern,Zonas húmedas costeras,Anfibio de tamaño mediano con piel rugosa,Medium-sized amphibian with rough skin,Pérdida de hábitat,false,false,false,true,false,true,false,true,false,false,false,false,true,true,false,false,false,false'''
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(csv_content)
        
        return [{
            'success': True,
            'filename': filename,
            'path': filepath
        }]
    
    # Mantener métodos existentes para compatibilidad
    def scrape_category(self, category, subcategory, subcategory_name):
        """Método existente para compatibilidad con la interfaz anterior"""
        return self.scrape_category_for_species(category, subcategory_name)

# Función de utilidad para uso directo
def search_species(species_name, test_mode=False):
    """Función de conveniencia para buscar una especie directamente"""
    scraper = DarwinScraper(test_mode=test_mode)
    return scraper.search_species_direct(species_name)

# Ejemplo de uso directo
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        species_name = ' '.join(sys.argv[1:])
        print(f"Buscando especie: {species_name}")
        
        # Usar modo de prueba por defecto
        result = search_species(species_name, test_mode=True)
        
        if result['success']:
            print(f"✓ Especie encontrada en categoría: {result['category']}")
            print(f"✓ Archivos descargados: {result['files_downloaded']}")
            print(f"✓ Archivos CSV: {result['csv_files']}")
        else:
            print(f"✗ Error: {result.get('error', 'Error desconocido')}")
    else:
        print("Uso: python darwin_scraper.py <nombre_de_especie>")
        print("Ejemplo: python darwin_scraper.py 'Patillo'")