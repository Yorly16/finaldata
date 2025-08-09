// Base de datos de especies por categoría
const speciesDatabase = {
    'anfibios': [
        'Sapo común',
        'Rana de árbol'
    ],
    'reptiles':[
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
    ],
    'aves': [
        'gavilán de Galápagos',
        'aguila pescadora',
        'Patillo',
        'Pato Cuchara Norteño',
        'Cerceta colorada (canela)',
        'Cerceta aliazul',
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
        'Raton de Santa Cruz',
        'Rata de Fernandina',
        'Rata de Santa Fe',
        'Rata de San Cristóbal',
        'Rata gigante de Santa Cruz e Isabela',
        'Rata Noruega, Rata de Noruega, Rata gris',
        'Rata negra, rata de barco, rata de tejado, rata común, pericote, rata de buque, rata de barco.'
    ]
};

// Elementos del DOM
const speciesInput = document.getElementById('speciesInput');
const searchBtn = document.getElementById('searchBtn');
const suggestions = document.getElementById('suggestions');
const messages = document.getElementById('messages');
const resultsContainer = document.getElementById('resultsContainer');
const loading = document.getElementById('loading');
const speciesResults = document.getElementById('speciesResults');

// Event listeners
speciesInput.addEventListener('input', showSuggestions);
speciesInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchSpecies();
    }
});
searchBtn.addEventListener('click', searchSpecies);

// Mostrar sugerencias mientras el usuario escribe
function showSuggestions() {
    const query = speciesInput.value.toLowerCase().trim();
    
    if (query.length < 2) {
        suggestions.style.display = 'none';
        return;
    }
    
    const allSpecies = [];
    Object.keys(speciesDatabase).forEach(category => {
        speciesDatabase[category].forEach(species => {
            if (species.toLowerCase().includes(query)) {
                allSpecies.push({ name: species, category });
            }
        });
    });
    
    if (allSpecies.length > 0) {
        suggestions.innerHTML = allSpecies.slice(0, 5).map(item => 
            `<div class="suggestion-item" onclick="selectSpecies('${item.name}')">
                ${item.name} <small>(${item.category})</small>
            </div>`
        ).join('');
        suggestions.style.display = 'block';
    } else {
        suggestions.style.display = 'none';
    }
}

// Seleccionar una especie de las sugerencias
function selectSpecies(speciesName) {
    speciesInput.value = speciesName;
    suggestions.style.display = 'none';
    searchSpecies();
}

// Función principal de búsqueda
async function searchSpecies() {
    const query = speciesInput.value.trim();
    
    if (!query) {
        showMessage('Por favor ingresa el nombre de una especie', 'error');
        return;
    }
    
    // Encontrar la categoría de la especie
    const category = findSpeciesCategory(query);
    
    if (!category) {
        showMessage('Especie no encontrada en la base de datos', 'error');
        return;
    }
    
    showMessage(`Especie encontrada en categoría: ${category}`, 'success');
    
    // Mostrar loading
    resultsContainer.style.display = 'block';
    loading.style.display = 'block';
    speciesResults.innerHTML = '';
    searchBtn.disabled = true;
    
    try {
        // Realizar búsqueda completa con Gemini
        const result = await scrapeCategory(category, query);
        
        if (result.success) {
            // Mostrar información completa de Gemini
            displaySpeciesInfoFromGemini(result, category);
        } else {
            throw new Error(result.error || 'Error en la búsqueda');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showMessage(`Error al buscar la especie: ${error.message}`, 'error');
        resultsContainer.style.display = 'none';
    } finally {
        loading.style.display = 'none';
        searchBtn.disabled = false;
    }
}

// Encontrar la categoría de una especie
function findSpeciesCategory(speciesName) {
    const normalizedQuery = speciesName.toLowerCase();
    
    for (const [category, species] of Object.entries(speciesDatabase)) {
        for (const speciesItem of species) {
            if (speciesItem.toLowerCase().includes(normalizedQuery) || 
                normalizedQuery.includes(speciesItem.toLowerCase())) {
                return category;
            }
        }
    }
    
    return null;
}

// Realizar scraping de la categoría (función actualizada)
async function scrapeCategory(category, speciesName) {
    try {
        const response = await fetch('/api/search-species-complete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                speciesName: speciesName,
                testMode: false // Cambiar a true para modo de prueba
            })
        });
        
        if (!response.ok) {
            throw new Error(`Error del servidor: ${response.status}`);
        }
        
        return await response.json();
        
    } catch (error) {
        throw new Error(`Error de conexión: ${error.message}`);
    }
}

// Extraer información específica de la especie del CSV
// Eliminar o comentar la función extractSpeciesInfo ya que no la necesitamos
// async function extractSpeciesInfo(csvData, speciesName) {
//     // Esta función ya no es necesaria porque Gemini procesa directamente
//     return {};
// }

// Actualizar la función displaySpeciesInfo original para mantener compatibilidad
function displaySpeciesInfo(info, category) {
    // Mantener esta función para compatibilidad, pero ahora usar la nueva función
    const mockResult = {
        success: true,
        species_name: 'Especie encontrada',
        category: category,
        species_info: info,
        csv_file: 'archivo.csv',
        analysis_method: 'legacy'
    };
    displaySpeciesInfoFromGemini(mockResult, category);
}

// Nueva función para mostrar información completa de Gemini
function displaySpeciesInfoFromGemini(result, category) {
    const categoryNames = {
        'reptiles': 'Reptiles',
        'aves': 'Aves', 
        'peces': 'Peces',
        'mamiferos': 'Mamíferos',
        'anfibios': 'Anfibios'
    };
    
    let html = `<div class="species-header">`;
    html += `<div class="category-badge">${categoryNames[result.category] || result.category}</div>`;
    html += `<h2>${result.species_name}</h2>`;
    html += `<div class="analysis-method">Análisis: ${result.analysis_method === 'gemini' ? 'Google Gemini AI' : 'Método de respaldo'}</div>`;
    html += `<div class="csv-file">Archivo: ${result.csv_file}</div>`;
    html += `</div>`;
    
    // Mostrar información de la especie
    if (result.species_info) {
        html += '<div class="species-info">';
        
        Object.entries(result.species_info).forEach(([key, value]) => {
            if (value && value.trim() !== '') {
                html += `
                    <div class="info-card">
                        <h3>${key}</h3>
                        <p>${value}</p>
                    </div>
                `;
            }
        });
        
        html += '</div>';
    }
    
    // Mostrar información adicional si hay errores de Gemini pero se usó respaldo
    if (result.gemini_error && result.analysis_method === 'backup_simple') {
        html += `
            <div class="warning-info">
                <h3>⚠️ Información adicional</h3>
                <p><strong>Nota:</strong> Se utilizó el método de respaldo debido a un problema con Gemini AI.</p>
                <p><strong>Error de Gemini:</strong> ${result.gemini_error}</p>
            </div>
        `;
    }
    
    speciesResults.innerHTML = html;
}

// Mostrar mensajes
function showMessage(message, type) {
    messages.innerHTML = `<div class="${type}">${message}</div>`;
    setTimeout(() => {
        messages.innerHTML = '';
    }, 5000);
}