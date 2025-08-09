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
                'Piquero Peruano',
                'Piquero Peruano',
                'Pato doméstico',
                'ganso común',
                'Guirirí',
                'Pato enmascarado',
                'Vencejo chimenea',
                'aguaitacamino migratorio',
                'chorlito de rompientes',
                'Vuelve piedras',
                'vuelve piedras negro',
                'chorlitejo',
                'Playero gritón',
                'chorlo de Wilson',
                'chorlo de campo',
                'Playero dorado',
                'chorlito dorado siberiano',
                'Playero cabezón',
                'ostrero, cangrejero',
                'gaviota negra',
                'Gaviotín blanco',
                'Gaviotín negro',
                'Gaviotín común',
                'Gaviotín elegante',
                'Gaviotín Real',
                'gaviota Cabecigrís',
                'gaviota cola bifurcada',
                'Gaviotin inca',
                'gaviota de Delaware',
                'gaviota dominicana',
                'gaviota reidora',
                'gaviota de lava',
                'gaviota de Franklin',
                'Gaviota Austral',
                'Gaviotín de cabeza blanca',
                'tero real',
                'correlino',
                'playero común',
                'playero de Baird',
                'Playero pecho rufo',
                'playero de rabadilla blanca',
                'correlino tarsilargo',
                'Playero occipital',
                'Tin Güín',
                'Playero enano',
                'Playero semipalmeado',
                'agujeta piquicorta',
                'aguja canela',
                'aguja del mar',
                'Zarapito',
                'falaropo rojo',
                'falaropo norteño',
                'falaropo de Wilson',
                'chorlo chico',
                'errante',
                'chorlo real',
                'Playero aliblanco',
                'Playero solitario',
                'Playerito canela',
                'Salteador grande',
                'salteador rabero',
                'Salteador polar',
                'Salteador parásito',
                'salteador',
                'Paloma doméstica, Paloma de Castilla, Paloma Común',
                'Paloma sabanera',
                'Paloma de Galápagos',
                'Martín pescador',
                'cuclillo pico negro',
                'cuclillo gris',
                'cuclillo',
                'Garrapatero, Ani, Garrapatero Pico liso, Pico machete.',
                'alcón peregrino',
                'codorniz',
                'Gallina - Gallo doméstico',
                'Pavo doméstico',
                'gallina de Guinea',
                'Pavo real',
                'gallareta americana',
                'gallinula',
                'Pachay',
                'gallareta',
                'gallinula púrpura',
                'Polluela norteña',
                'Miracielito',
                'Azulillo',
                'Pidgordito degollado',
                'cardenal rojo',
                'Cardenal migratorio colorado',
                'Golondrina de Horquilla',
                'Golondrina risquera',
                'Golondrina de Galápagos',
                'Golondrina de Iglesias',
                'golondrina parda',
                'golondrina parda',
                'tordo arrocero',
                'Quiscal mexicano',
                'cucuve de Española',
                'cucuve de San Cristóbal',
                'cucuve de Galápagos',
                'cucuve de Floreana',
                'chipe de agua norteño',
                'candelita americana',
                'Reinita protonotaria',
                'Canario María',
                'reinita rayada',
                'Pinzón de manglar',
                'Pinzón carpintero, artesano',
                'Pinzón arboreo pequeño',
                'Pinzón arboreo mediano',
                'Pinzón arboreo grande',
                'Pinzón cantor gris',
                'Pinzón cantor verde',
                'platanera común',
                'Pinzon de tierra de Genovesa',
                'Pinzón de cactus grande',
                'Pinzón de pico afilado',
                'Pinzón mediano de tierra',
                'Pinzón tierrero pequeño',
                'Pinzón tierrero grande',
                'Pinzón de cactus de Genovesa',
                'Pinzón de cactus comun',
                'Pinzón vampiro',
                'Pinzón vegetariano',
                'Jilguero dorado',
                'Pitirre americano',
                'Pájaro Brujo de San Cristóbal',
                'Pájaro Brujo de Galápagos',
                'Papamoscas',
                'Julián Chiuí Ojirajo',
                'garza blanca',
                'garza morena',
                'garza bueyera',
                'garza estriada',
                'garcita verde',
                'garza azul',
                'garcita blanca',
                'garza tricolor',
                'garza nocturna',
                'garza nocturna',
                'Pelícano café',
                'Pájaro Tropical',
                'Pájaro tropical colirojo',
                'Flamenco Chileno',
                'flamenco',
                'Sormomujo',
                'Albatros real',
                'Albatros paseador',
                'Albatros de Galápagos',
                'Albatros pies negros',
                'albatros ceja negra',
                'Bailarín',
                'Golondrina de Elliot',
                'golondrina de Madeira',
                'Golondrina de mar de collar',
                'Golondrina de mar',
                'Golondrina de Markham',
                'Golondrina Negra',
                'Golondrina de Tormenta de Galápagos',
                'Golondrina cariblanca',
                'Petrel del Cabo',
                'Petrel plateado',
                'Fardela negruzca',
                'Fardela blanco',
                'Pufino negro',
                'Pardela del Pacífico',
                'petrel gigante del sur',
                'petrel gigante del norte',
                'petrel Ballena',
                'Petrel Negro Parkinson',
                'Petrel moteado',
                'Petrel de Gould',
                'Petrel de Galápagos',
                'Pufino negro',
                'Pufino de Galápagos',
                'Aratinga de Guayaquil',
                'Pingüino de Galápagos',
                'Lechuza de campo',
                'lechuza de campanario',
                'fragata real de Galápagos',
                'fragata común',
                'cormorán no volador',
                'Piquero de Nazca',
                'Piquero café',
                'Piquero patas azules',
                'Piquero patas rojas'
            ],
            'peces': [
                'anguilla moteada gigante',
                'morena falso de dos colores',
                'morena menuda',
                'morena boca de gancho, morena mosaico',
                'morena quijada delgada, morena kuijada esbelto',
                'morena cebra',
                'morena errante',
                'pargo amarillo',
                'morena pintita, morena punto fino',
                'morena de borde amarillo',
                'morena boca blanca',
                'morena pecas blancas',
                'morena de piedra, morena clepsidra',
                'morena lentejuela, morena pinta',
                'anguila bruja, serpentina bruja',
                'tieso moteado',
                'congrio culebra, aguila congrio panamica',
                'congrio de cola tiesa',
                'anguila jardín de Galápagos',
                'congrio colicorta, congrio de coda corta, congrio de cola corta',
                'congrio de corta nareza, congrio de labio grueso, congrio labioso',
                'Tieso ecuatorial, Tieso sin aletas',
                'anguila de Galapagos',
                'tieso bigotón, tieso de Afuera',
                'tieso sonriente',
                'safio tigre, anquila tigre',
                'anguila de aleta chica',
                'anguila bolsona',
                'tieso vibora, tieso vípora',
                'morena estrellada, morena estriada, kal',
                'morena pecosa',
                'morena atigrada de arrecifes',
                'morena cabeza grande',
                'morena',
                'morena verde panamica',
                'morena ojo negro',
                'morena pimienta',
                'plateado rayado',
                'pejerrey azulado',
                'conejo, conejo de lo alto, lanzón, lanzón nariz larga, lanzón picudo',
                'pez iguana marina',
                'garrobo lucio',
                'garrobo liguiso',
                'bruja, pez fraile luminoso, sapo margarita, sapo luminoso',
                'aguja americana, aguja corbata, agujón sable',
                'aguja brava, lápiz aguja, agujón californiano, pez aguja',
                'aguja, agujón crocodrilo, marao lisero',
                'aguja, agujón del Pacífico, marao ojón',
                'Pez volador, Volador planeador',
                'volador dorso manchado, Volador lomo manchado',
                'pez volador, volador ala manchada, volador de alas punteadas',
                'pez volador, volador jaspeado',
                'pez volador, volador de puntas blancas',
                'pez volador, volador alimanchado, volador bonito, volador pequeño',
                'pez volador, volador barbón, volador barbudo',
                'pez volador, lisa voladora, volador',
                'pez volador, volador de banda',
                'pez volador, volador aleta negra, golondrina del mar',
                'pez volador, volador espejo',
                'agujeta de aleta larga, pajarito de aleta larga, volador alita',
                'Pez volador',
                'silio, pajarito, aujeta alargada, agujeta alargada',
                'agujeta pajarito',
                'picuda, choquita, agujeta blanca',
                'candil escama grande, soldado escama grande',
                'candil púrpura, soldado panamico',
                'candil sol',
                'sardina peruana o redonda, sardina redonda, sardineta canalera, Sardina canalera, Sardina japonesa',
                'sardina rayada, sardineta piquitinga pelada',
                'Machuelo hebra de Galapagos',
                'sardina-gallera común',
                'sardina peruana',
                'chicotera, chumumo, anchoa chicotera',
                'anchoveta, carduma, chuchueco, chuhueco ojito, esmeraldas, ojito, sardina',
                'anchoveta, anchoa, anchoveta peruana, atunera, Chicora, Sardina bocona',
                'chiro, diabla',
                'bregmacero manchado, bregmacero, bacalaito plateado',
                'granadero de cola fina',
                'granadero peruano',
                'granadero californiano',
                'granaderos',
                'Granadero anguloso',
                'granadero abisal, granadero máximo',
                'granadero trompacorta',
                'granadero de hocico angosto',
                'Granadero ojón',
                'Peje-rata, Ratón',
                'granadero trompacorta',
                'granadero de Myers',
                'pez rata, granadero cano',
                'merluza, merluza del Pacífico sur, merluza chilena, peje palo, pescada, merluza maltona',
                'brótola azul, mollera azul',
                'carbonero de fango',
                'corneta, trompeta lisa, pez corneta, corneta flautera',
                'diabla',
                'cardenal, cinta, flema, flemma, listoncillo festón',
                'Pejerana bandeado',
                'pejerana bocon, pez sapo cola de banda.',
                'ganso manchado',
                'pez sapo, bocón barbudo, rape de hebra, rape de rabo delgado',
                'Murciélago boca colorado, pez murciélago labio rojo',
                'Pejerana colorado',
                'ranisapo escarlata',
                'ranisapo de Commerson',
                'pez murcielago',
                'pez murcielago',
                'pez murcielago',
                'pez murcielago',
                'pez murcielago',
                'lisa de rio',
                'lisa, lisa hocicona',
                'lisa de Galápagos',
                'lisa criolla',
                'lisa rabo amarillo, lisa pardete',
                'lisa agugu',
                'pejecito linterna, linterna de Diógenes',
                'linternilla, pez linterna',
                'linternilla, pez linterna',
                'brótulas viviparas',
                'brótulas vivíparas',
                'brótula, brótula púrpura',
                'brótula, brótula naranja',
                'brótula, brótula rosada',
                'brótula, brótula colimanchada',
                'brótulas vivíparas',
                'pez perla, culebrilla, perlero del pacifico',
                'perlero nocturno, pez perla',
                'perlero mocho, pez perla sin aletas',
                'brótulas',
                'brótula pintada',
                'brótulas',
                'lengua de  Galápagos',
                'congriperla mancha café',
                'brótula',
                'brótula hocico velludillo',
                'argentina alicia',
                'cirujano convicto, lancero convicto.',
                'pez cirujano',
                'peón panámico, lanceta de arena plateado.',
                'cardenal punta negra',
                'cardenal pintado',
                'cardenal rosado, cardenal morro listado',
                'trambollito negro, borracho mono',
                'trambollito diente sable',
                'japuta menuda, japuta  comun',
                'chancho piraña, japuta negra, palometa negra, tristón coliquillada',
                'dragonito  de asta',
                'pámpano africano',
                'cocinero dorado, jurel verde',
                'jurel común',
                'jurel negro',
                'jurel de aleta azul',
                'jurel, jurel alicorta, jurel fino, macarela alicorta, macarela fina',
                'Macarela mexicana',
                'macarela salmón, macarela arco iris',
                'pámpanos, jurel, carángido',
                'jurel negro',
                'jurel de aleta azul',
                'jurel, jurel alicorta, jurel fino, macarela alicorta, macarela fina',
                'Macarela mexicana',
                'macarela salmón, macarela arco iris',
                'chicharro ojón',
                'carita celosa, carita común, espejo, chancleta, jorobado  espejo',
                'jurel, jurel alicorta, jurel fino, macarela alicorta, macarela fina',
                'Macarela mexicana',
                'macarela salmón, macarela arco iris',
                'chicharro ojón',
                'carita celosa, carita común, espejo, chancleta, jorobado  espejo',
                'palometa, huayaipé',
                'paloma pompano',
                'pampano filo',
                'pámpano acerado',
                'cojinoba palmera',
                'robalo, robalo plateado, robalo blanco.',
                'mariposa de tres bandas',
                'tilapia negra',
                'halcón de coral',
                'carabalí, mero chino',
                'halcón narizón',
                'dorado, dorado chato',
                'dorado comun',
                'mirador de estrellas blanco',
                'mirador de estrellas flecha',
                'mirador de estrellas aletita',
                'Rémora, Pega, Pegatimon, Pegador',
                'chalaco, chame, porroco, poyoco, dormilón, camote del Pacífico',
                'guavina machada, mongolo, vieja, dormilon manchado',
                'cawa',
                'mirador de estrellas flecha.',
                'mirador de estrellas aletita.',
                'Rémora, Pega, Pegatimon, Pegador',
                'chalaco, chame, porroco, poyoco, dormilón, camote del Pacífico',
                'guavina machada, mongolo, vieja, dormilon manchado',
                'cawa',
                'escolar  de  canal',
                'escolar negro, mírame lindo',
                'escolar',
                'mojarra, mojarra pedorra, mojarra aletas amarillas, periche, mojarra cortiaguda',
                'mojarra, Española plateada, mojarra plateada',
                'mojarra tricolor, mojarra tricolor, mojarrita bandera, palmito bandera, leiro',
                'mojarilla plateada',
                'Mojarra, Mojarra charrita, Mojarra leiro, Palometa',
                'mojarra, palometa, mojarra china',
                'mojarra rayada, mojarra blanca',
                'gobio bonito de Galápagos, Gobio de bandas azules de Galápagos',
                'ronco almejero, roncador almejero',
                'corcovado zapata',
                'ojón blanca',
                'ojón rayado, ojon',
                'roncador de Forbes',
                'picudo banderón, pez vela del Indo-Pacífico, volador',
                'merlín negro, picudo negro, aguja negra',
                'merlín rayado, picudo blanco, picudo rollizo, aguja azul del Indo-Pacífico',
                'chopa gris, chopa rayada',
                'chopa Cortés',
                'chopa negra,  chopa penumbre',
                'chopa salema',
                'vieja de piedra, Vieja ribeteada',
                'vieja mulata, vieja arlequín',
                'doncella san pedrano, vieja camaleón',
                'doncella solterona, vieja soltera',
                'vieja',
                'Vieja verde',
                'arco iris de Cortez, arco iris',
                'viejita pavo real',
                'pargo raicero',
                'pargo amarillo',
                'pargo blanco',
                'pargo negro',
                'pargo azul',
                'pargo azul-dorado',
                'cabezudo, blanquillo',
                'Pez gusano colibandera',
                'pez  gusano  transparente',
                'salmonete barbón,salmonete barbón cola amarillo',
                'papagallo',
                'bocón grande de Galápagos',
                'aguapuro, guapuro azul, barbudo azul, barbudo seis barbas',
                'pez bandera',
                'machín, machín lechuza, angel de Cortés, pez ángel',
                'sargento mayor',
                'sargento mayor, petaca banderita',
                'castañuela punta negro',
                'castañeta de aqua profunda, chromis dorso plateado',
                'castañeta conguita, castañeta cola de tijera',
                'jaqueta vistosa, damisela cabeza chichón',
                'jaqueta gigante, damisela gigante',
                'castañeta indiga',
                'jaqueto amarillo',
                'jaqueta rabo blanco',
                'castañeta azul dorado',
                'damisela achiotada, damisela coquito.',
                'loro jorobado, loro guacamayo',
                'loro barbazul',
                'bombache ojon, corvina bronce.',
                'corvinilla camiseta, Gungo de Galápagos',
                'verrugato de  Galápagos',
                'peto, guaho',
                'barrilete negro',
                'listado',
                'bonito mono',
                'estornino',
                'carite sierra',
                'atún blanco',
                'atún de aleta amarilla',
                'patudo',
                'mero orillero',
                'Merito Arco Iris',
                'bacalao',
                'gringo',
                'jabonero de Cortés, jabonero moteado',
                'jabonero negro, jabonero doble punteado',
                'mero cabeza de zorro, plumero',
                'camotillo',
                'sargo camiseta, camiseta rayada',
                'pluma marotilla',
                'pluma palma, pluma de Galápagos',
                'picuda pelícano',
                'gallinazo, pámpano, palometa cometrapo, palometa del Pacífico',
                'cintilla',
                'blennio de aleta triple, trambollito triple aleta de Galápagos',
                'miracielo buldog',
                'pez espada',
                'cirujano de borde dorado, cirugano cariblanco.',
                'navajón lancero, pez cirugano púrpura',
                'pez unicornio',
                'pez unicornio manchado',
                'pez unicornio liso',
                'pez unicornio de nariz grande',
                'cochinito puntada',
                'idolo moro',
                'borracho aleta mocha, trambollo aleta mocha',
                'trambollito pico de lapa, borraco vacilo',
                'trombollito de Castro, trombollito percebes de Galápagos',
                'Trambollito de Galápagos',
                'chupa piedra',
                'trambollo bravo',
                'trambollo de Jenkins',
                'trambollo moteado, trambollo pintado',
                'trombollo panzimanchado',
                'trambollo de  Galápagos',
                'peje sapito',
                'chupapiedra rojo, pez prendedor de Galápagos.',
                'gobio manchada',
                'mapo del sur',
                'gobio semaforo, gobio luz roja.',
                'gobio bandeado, gobio barbero de bandas',
                'gobio bonito, gusanito del diablo, gobio azul  rayado',
                'gobio ligero, gobio manchado',
                'resbalosa, viejita colorada, viejita manchada, señorita de mancha negra',
                'vieja negra',
                'señorita herida',
                'Vieja Dorada',
                'señorita de cintas',
                'viejita pavo Real',
                'señorita viejita, vieja mueve roca',
                'vieja mancha roja',
                'vieja variante, vieja oleaja',
                'loro de Carolinas, perico de diente verde, pococho perico',
                'loro chato, loro verdeazul',
                'loro violáceo',
                'pococho beriquete',
                'jurel voráz, jurel oral',
                'jurel fino, macarela caballa',
                'macarela chuparaco, jurela',
                'jurel de piedra, jurel dorado, merlindo',
                'pez piloto',
                'palometa, voladora mascapalo, chaqueta de cuero, cuchillo, zapatero siete  cueros.',

                'caramelo, jurel lengua blanca, tiñosa blanca',
                'mariposa de aleta ribeteada',
                'mariposa de barra penumbre',
                'mariposa mapache',
                'mariposa de Meyer',
                'Mariposa Lagrima',
                'mariposa hocicona',
                'mariposa barbera',
                'Mariposa Guadana',
                'rémora chupadora, rémora delgada, pez pega lineado',
                'rémora de merlín, sapito blanco, peje piloto, rémora gris, tardanaves',
                'agarrador, rémora de merlín, rémora marlinera',
                'rémora común',
                'remora, rémora blanca',
                'chambo',
                'burrito frijol, zapatilla',
                'roncador peruano',
                'ronco bacoco, roncador ojo dorado.',
                'roncador fríjol',
                'roncador brinco',
                'burrito brin, corocoro brin, teniente ',
                'dará bandera',
                'pargo coconaco',
                'pargo, pargo de altura, pargo lunarejo, cojinoba rosada',
                'panchito rayado',
                'cabezón, cabezudo, blanquillo, blanquillo cabezón, blanquillo',
                'chivito, chivo escamudo, chivo colorado, salmonete gringuito',
                'Bocón gigante',
                'perico presidiario, tigris',
                'catalufa aleta larga, Catalufa',
                'catalufa de roca, semáforo',
                'ojotón',
                'corvina, corvina pampera, corvinilla, gringa',
                'corvina ojona, corvineta vacuocua',
                'corvina, corvina colilarga, corvina picuda',
                'corvina',
                'guaseta del Pacifico, guaseta',
                'pez joya',
                'mero panameño, enjambe',
                'caga leche, mero cuero',
                'camotillo, camotillo naranja,  cagua, serrano carabonita, serrano guavina',
                'camotillo cabezón, serrano extranjero',
                'camotillo, serrano cagua, serrano mexicano',
                'camotillo, serrano frenado',
                'cabrilla gallina, gallina, norteño',
                'cabrilla piedrera',
                'rabijunco, cabrilla de Perú, cabrilla doblecola, doncella',
                'serrano ojo de uva, ojo de uva',
                'mero',
                'cherna pintada, mero',
                'guaseta serrano',
                'guaseta  manchada',
                'botellita, melva, melvera',
                'botellita grande, melva',
                'barracuda, picúa, picuda, picuda barracuda',
                'derivante ojón, pez medusa, flotador  largo aleta',
                'pastorcillo, pez azul',
                'guardaboya, guardaboya tapadera, suela rayada',
                'lenguado moteado, lenguado ojo leopardo',
                'lenguado tropical',
                'lengua',
                'lenguado huarache',
                'sol reticulado, Suela de Herre',
                'lenguado, lenguado oval, lenguado ovalado, lenguado pega-pega',
                'lenguada hua',
                'lengua',
                'caballito  moro',
                'escorpion manchado',
                'pez escorpion roja',
                'rascacio jugador',
                'escorpion roquero',
                'rascacio arco iris',
                'Pez diablo de profundidad, Rascacio profundo',
                'rubio falso volador',
                'escorpion espinoso',
                'rubio rey, vaca cariblanca',
                'trompeta espinosa, pez trompeta',
                'pez corneta, Pez corneta de arrecife',
                'caballito del Pacifico, caballito de mar del Pacifico',
                'pez pipa velero',
                'agujón, pez pipa chato',
                'pez pipa chica',
                'pejepuerco coche, cachudo escama fina',
                'pez puerco, cochito negro',
                'Pejepuerco cola rosada, cochito cola rosada',
                'chancho',
                'cochinito',
                'cachudo cola roja',
                'pejerizo enmascarado, pez erizo balón',
                'pez puerco espín, pez erizo punteado',
                'pez sol oceánico, mola mola',
                'mola',
                'ranzania, mola flaca',
                'lija trompa, pez lija puntiazul.',
                'pez caja manchado, pez caja pacifico',
                'tamboríl hawaiiano, tamboril verde de puntos blancos',
                'tamboríl negro, botete negro',
                'botete bonito, tamboril punteado nariz aguda',
                'pejepuerco de piedra',
                'pejerizo chiquito, pez erizo de aleta manchada, pez erizo del pacífico, pez erizo enano',
                'pez erizo espinas amarillas, pez erizo base de punto',
                'pez erizo pelágico',
                'mola coliaguda, pez luna coliagudo',
                'puerco de altura, Lija barbuda',
                'cachua blanca nieves, pez lija vagabundo',
                'tamboril oceánico, botete oceánico, pez globo',
                'Tamboríl panal, botete panal.',
                'tamboril oceánico, botete oceánico, pez globo',
                'Tamboríl panal, botete panal.',
                'tamboríl cóncavo',
                'tambulero',
                'Tumbulero lóbulo',
                'tiburón de puntas blancas, tiburon de punta plateada.',
                'Tiburón jaquetón',
                'tiburón de Galápagos',
                'tiburón tigre, alecrin, tintorera',
                'cazón, cazón trompa blanca, pico blanco, tiburón coyotito',
                'tiburón azul, azulejo',
                'Tiburón baboso',
                'cazón, tiburón oceánico, tiburón pardo, galano',
                'cazón, tiburón aleta de cartón, tiburón brasilero, tiburón pardo',
                'gato trompudo, pejegato trompudo',
                'tiburón martillo',
                'cachona',
                'cachona',
                'tollo manchado',
                'tiburón macuira, tiburón punta negra, tiburón volador',
                'tiburón coralero ñato, cazon coralero tompacorta, Cazón coralero tompacorta',
                'cachona',
                'tollo fino, musola fina',
                'tiburón gato',
                'zorro pelágico, zorro de mar',
                'zorro ojón, zorro de mar',
                'solrayo',
                'jaquetónes, marrajos',
                'marrajo dientuso',
                'tiburón ballena',
                'raya batana, raya de espina',
                'Batana, Batea, Raya diamante, Raya látigo diamante',
                'raya coluda, raya latigo largo',
                'raya del pacífico',
                'raya látigo violeta, raya negra',
                'raya manchada',
                'tecolote',
                'águila áspera, águila cueruda,',
                'manta voladora, manta gigante, manta raya',
                'manta de aguijón',
                'diablo manta',
                'manta cornuda, raya cornuda, diablo gigante de Guinea',
                'raya aguila',
                'manta, pez-diablo',
                'raya dorada, Gavilán Negro',
                'raya blanca',
                'raya falsa sureña',
                'raya bruja',
                'guitarra del pacífico',
                'quelvacho negro',
                'tollo negro peine',
                'tollo cigarro',
                'Tiburón negro',
                'torpedo eléctrico'
            ],
            'mamiferos': [
                'ganado vacuno',
                'Chivo, Cabra',
                'Ovejuno',
                'Cerdo, chancho, puerco, marrano, porcino, cochinito, lechón.',
                'Perro doméstico, Canino.',
                'Felino, Gato doméstico',
                'ballena minke',
                'ballena Sei',
                'ballena de Bryde',
                'ballena azul',
                'ballena de aleta, rorcual común',
                'ballena jorobada',
                'Delfín común oceanico',
                'orca pigmea',
                'ballena piloto de aleta corta',
                'delfín de Risso',
                'delfín de Fraser',
                'orca',
                'ballena cabeza de melón',
                'falsa orca',
                'delfín listado',
                'delfin tornillo',
                'delfín de dientes rugosos',
                'delfín nariz de botella',
                'cachalote pigmeo',
                'Cachalote enano',
                'cachalote',
                'ballena nariz de botella',
                'ballena picuda de Longman',
                'ballena picuda de Blainville',
                'ballena picuda de Ginkgo',
                'ballena picuda',
                'ballena picuda de Cuvier',
                'Murciélago rojo',
                'Murciélago negro',
                'Zariguella de orejas negras común',
                'Conejo doméstico',
                'Burro, Asno',
                'equino, caballo',
                'Lobo marino de dos pelos',
                'Lobo marino Sudamericano',
                'lobo marino de un pelo',
                'Mono cabeza de algodón',
                'Humano moderno',
                'cuy',
                'Rata gigante de Isabela',
                'Ratón, ratón casero, pulpero',
                'Raton de Darwin',
                'Raton de Fernandina',
                'Raton de Isabela 2',
                'Raton de Isabela 3',
                'Raton de Rábida',
                'Raton de Santa Cruz',
                'Rata de Fernandina',
                'Rata de Santa Fe',
                'Rata de San Cristóbal',
                'Rata de Santiago',
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
                'Tortuga de Rábida',
                'Gecko - tuberculosus',
                'serpiente marina amarilla',
                'Iguana marina',
                'Iguana rosada',
                'Iguana de Santa Fe',
                'iguana terestre de Santiago',
                'Iguana terrestre de Galápagos',
                'Iguana verde',
                'Lagartija el inesperado',
                'Lagartija de lava Albemarle',
                'Lagartija de lava de San Cristobal',
                'Lagartija de lava de Española',
                'Lagartija de lava de Pinzón',
                'Lagartija de lava de Floreana',
                'Lagartija de lava de Marchena',
                'Lagartija de lava Indefatigable',
                'Lagartija de lava de Santiago',
                'Lagartija de lava de Pinta',   
                'Coral ratonera/coralillo/Falsa coral',
                'Tortuga de Florida',
                'Tortuga boba',
                'Tortuga marina verde',
                'tortuga marina de carey',
                'tortuga marina escamosa',
                'tortuga laud',
                'charapa pequeña',
                'Tortuga Gigante de Pinta',
                'Tortuga Gigante de Volcán Wolf',
                'Tortuga Gigante de San Cristóbal',
                'Tortuga Gigante de Santiago',
                'Tortuga del Este de Santa Cruz',
                'Tortuga Gigante de Floreana',
                'Tortuga de Pinzón',
                'Tortuga Gigante de Sierra Negra',
                'Tortuga de Española',
                'Tortuga Gigante de Volcán Darwin',
                'Tortuga de Fernandina',
                'Tortuga del Oeste de Santa Cruz',
                'Tortuga de Santa Fe',
                'Tortuga de Cerro Montura',
                'tortuga de Alcedo',
                'Tortuga de Cerro Azul',
                'Tortuga de Rábida',
            ]

        }
        
        # Mapeo de categorías a términos de búsqueda en la página web
        self.category_search_terms = {
            'anfibios': ['amphibia', 'anfibios', 'sapo', 'rana'],
            'aves': ['aves', 'bird', 'gavilán', 'águila', 'pato', 'cerceta', 'piquero'],
            'peces': ['pisces', 'peces', 'fish', 'anguila', 'morena', 'pargo'],
            'mamiferos': ['mammalia', 'mamíferos', 'mammals', 'rata', 'ratón', 'ganado', 'perro', 'gato', 'ballena', 'delfín', 'orca', 'cachalote', 'lobo marino', 'murciélago'],
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