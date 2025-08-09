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
            print(f"[GEMINI] Iniciando análisis para: {species_name}")
            print(f"[GEMINI] API Key configurada: {self.gemini_api_key[:10]}...")
            
            # Leer el contenido del CSV con múltiples codificaciones
            csv_content, used_encoding = self.read_csv_with_encoding(csv_path)
            print(f"[LOG] Usando codificación: {used_encoding}")
            
            # Limpiar y limitar el contenido del CSV con estrategia inteligente
            max_chars = 8000  # Aumentar significativamente el límite
            max_lines = 100   # Más líneas para mayor cobertura
            
            if len(csv_content) > max_chars:
                lines = csv_content.split('\n')
                header = lines[0] if lines else ""
                
                # Estrategia inteligente: buscar primero si la especie está en el CSV
                species_line_found = False
                species_line_index = -1
                
                # Buscar la especie en el CSV completo
                for i, line in enumerate(lines[1:], 1):
                    if species_name.lower() in line.lower():
                        species_line_found = True
                        species_line_index = i
                        break
                
                if species_line_found:
                    # Si encontramos la especie, incluir líneas alrededor de ella
                    start_idx = max(1, species_line_index - 20)
                    end_idx = min(len(lines), species_line_index + 30)
                    sample_lines = lines[start_idx:end_idx]
                    print(f"[LOG] Especie encontrada en línea {species_line_index}, incluyendo contexto")
                else:
                    # Si no la encontramos, usar muestra más grande del inicio
                    sample_lines = lines[1:max_lines] if len(lines) > 1 else []
                    print(f"[LOG] Especie no encontrada en búsqueda rápida, usando muestra ampliada")
                
                csv_content = header + '\n' + '\n'.join(sample_lines)
                
                # Si aún es muy largo, truncar pero mantener la especie si la encontramos
                if len(csv_content) > max_chars:
                    csv_content = csv_content[:max_chars]
            
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
                    "maxOutputTokens": 2048
                }
            }
            
            # Llamar a Gemini API
            try:
                print(f"[GEMINI] Enviando request a: {self.gemini_url}")
                response = requests.post(
                    url_with_key,
                    headers=headers,
                    json=data,
                    timeout=30
                )
                
                print(f"[GEMINI] Status code recibido: {response.status_code}")
                print(f"[DEBUG] Response: {response.text[:500]}")
                
                if response.status_code == 200:
                    print(f"[GEMINI] ✅ Respuesta exitosa de Gemini")
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
                    print(f"[GEMINI] ❌ Error HTTP: {response.status_code}")
                    print(f"[GEMINI] Response text: {response.text[:200]}...")
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
        """Búsqueda mejorada en CSV como respaldo"""
        try:
            # Usar la función de lectura con múltiples codificaciones
            csv_content, used_encoding = self.read_csv_with_encoding(csv_path)
            print(f"[LOG] Método de respaldo mejorado usando codificación: {used_encoding}")
            
            # Convertir el contenido a un objeto StringIO para csv.DictReader
            csv_file = io.StringIO(csv_content)
            csv_reader = csv.DictReader(csv_file)
            
            # Normalizar el nombre de búsqueda
            search_terms = self._normalize_species_name(species_name)
            print(f"[LOG] Términos de búsqueda: {search_terms}")
            
            best_match = None
            best_score = 0
            
            for row_num, row in enumerate(csv_reader, 1):
                # Obtener todos los nombres posibles de la especie
                spanish_name = row.get('Spanish Common Name', '').strip()
                english_name = row.get('English Common Name', '').strip()
                genus = row.get('Genus', '').strip()
                epithet = row.get('Specific Epithet', row.get('Specific Epithtet', '')).strip()  # Manejar typo
                scientific_name = f"{genus} {epithet}".strip()
                
                # Calcular score de coincidencia
                match_score = self._calculate_match_score(search_terms, {
                    'spanish': spanish_name,
                    'english': english_name,
                    'scientific': scientific_name,
                    'genus': genus,
                    'epithet': epithet
                })
                
                if match_score > best_score:
                    best_score = match_score
                    best_match = {
                        'row': row,
                        'row_num': row_num,
                        'score': match_score
                    }
                    
                    # Si encontramos una coincidencia perfecta, no seguir buscando
                    if match_score >= 0.9:
                        break
            
            if best_match and best_score > 0.3:  # Umbral mínimo de coincidencia
                row = best_match['row']
                print(f"[LOG] Mejor coincidencia encontrada en fila {best_match['row_num']} con score {best_score:.2f}")
                
                # Extraer información de islas
                islands_info = self._extract_islands_presence(row)
                
                return {
                    "found": True,
                    "species_info": {
                        "Nombre Común en Español": row.get('Spanish Common Name', 'No disponible'),
                        "Nombre Común en Inglés": row.get('English Common Name', 'No disponible'),
                        "Género": row.get('Genus', 'No disponible'),
                        "Epíteto Específico": row.get('Specific Epithet', row.get('Specific Epithtet', 'No disponible')),
                        "Estado UICN": row.get('IUCN Status', 'No disponible'),
                        "Hábitat": row.get('Spanish Distribution Comments', row.get('English Distribution Comments', 'No disponible')),
                        "Islas de Presencia": islands_info,
                        "Descripción (Español)": row.get('Spanish Description', 'No disponible'),
                        "Descripción (Inglés)": row.get('English Description', 'No disponible'),
                        "Amenazas": row.get('Spanish Comments', row.get('English Comments', 'No disponible')),
                        "Nombre Científico": f"{row.get('Genus', '')} {row.get('Specific Epithet', row.get('Specific Epithtet', ''))}".strip(),
                        "Familia": row.get('Family', 'No disponible'),
                        "Orden": row.get('Order', 'No disponible'),
                        "Score de Coincidencia": f"{best_score:.2f}"
                    },
                    "match_details": {
                        "row_number": best_match['row_num'],
                        "match_score": best_score,
                        "search_terms": search_terms
                    }
                }
            else:
                return {
                    "found": False, 
                    "error": f"Especie no encontrada en CSV. Mejor coincidencia: {best_score:.2f} (umbral: 0.3)"
                }
                
        except Exception as e:
            return {"found": False, "error": f"Error al leer CSV: {str(e)}"}

    def _normalize_species_name(self, species_name):
        """Normaliza el nombre de la especie para búsqueda flexible"""
        import re
        
        # Convertir a minúsculas y limpiar
        normalized = species_name.lower().strip()
        
        # Remover acentos y caracteres especiales
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'ñ': 'n', 'ü': 'u'
        }
        for old, new in replacements.items():
            normalized = normalized.replace(old, new)
        
        # Generar términos de búsqueda
        terms = [normalized]
        
        # Agregar variaciones comunes
        words = normalized.split()
        if len(words) > 1:
            terms.extend(words)  # Palabras individuales
            terms.append(' '.join(words[:2]))  # Primeras dos palabras
        
        # Remover duplicados y términos muy cortos
        terms = list(set([term for term in terms if len(term) > 2]))
        
        return terms

    def _calculate_match_score(self, search_terms, species_data):
        """Calcula un score de coincidencia entre términos de búsqueda y datos de especie"""
        max_score = 0
        
        for term in search_terms:
            for field_name, field_value in species_data.items():
                if not field_value:
                    continue
                    
                field_lower = field_value.lower()
                
                # Coincidencia exacta
                if term == field_lower:
                    return 1.0
                
                # Coincidencia de palabra completa
                if term in field_lower.split():
                    max_score = max(max_score, 0.9)
                
                # Coincidencia parcial
                elif term in field_lower:
                    # Score basado en la proporción de coincidencia
                    score = len(term) / len(field_lower)
                    max_score = max(max_score, min(score * 0.8, 0.7))
        
        return max_score

    def _extract_islands_presence(self, row):
        """Extrae información de presencia en islas del CSV"""
        islands = [
            'Baltra', 'Bartolome', 'Darwin', 'Espanola', 'Fernandina', 
            'Floreana', 'Genovesa', 'Isabela', 'Marchena', 'Pinta', 
            'Pinzon', 'Rabida', 'San Cristobal', 'Santa Cruz', 'Santa Fe', 
            'Santiago', 'Wolf'
        ]
        
        present_islands = []
        
        for island in islands:
            # Buscar columnas que contengan el nombre de la isla
            for column_name, value in row.items():
                if island.lower() in column_name.lower():
                    # Si el valor indica presencia (True, 1, 'Yes', 'Sí', etc.)
                    if str(value).lower() in ['true', '1', 'yes', 'sí', 'si', 'x']:
                        present_islands.append(island)
                    break
        
        return ', '.join(present_islands) if present_islands else 'No disponible'

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