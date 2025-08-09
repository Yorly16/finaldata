// Datos de las categorías
const categories = [
  {
    id: "animales",
    name: "ANIMALES",
    icon: "fas fa-paw",
    subcategories: [
      {
        id: "vertebrados-terrestres-marinos",
        name: "Vertebrados Terrestres y Marinos",
        description: "Amphibia, Aves, Peces, Mamíferos, Reptiles",
      },
      {
        id: "amphibia",
        name: "Amphibia",
        description: "Anfibios de las Galápagos",
      },
      {
        id: "aves",
        name: "Aves",
        description: "Aves de las Galápagos",
      },
      {
        id: "peces",
        name: "Peces",
        description: "Peces marinos y de agua dulce",
      },
      {
        id: "mamiferos",
        name: "Mamíferos",
        description: "Mamíferos terrestres y marinos",
      },
      {
        id: "reptiles",
        name: "Reptiles",
        description: "Reptiles terrestres y marinos",
      },
    ],
  },
  {
    id: "invertebrados-terrestres",
    name: "INVERTEBRADOS TERRESTRES",
    icon: "fas fa-bug",
    subcategories: [
      {
        id: "anelidos",
        name: "Anélidos - Lombrices de tierra",
      },
      {
        id: "hormigas-leon",
        name: "Hormigas león, crisopas",
      },
      {
        id: "hormigas",
        name: "Hormigas",
      },
      {
        id: "hormigas-abejas-avispas",
        name: "Hormigas, abejas, avispas y otros grupos relacionados",
      },
      {
        id: "aracnidos",
        name: "Arácnidos",
      },
      {
        id: "escarabajos",
        name: "Escarabajos",
      },
      {
        id: "piojos-corteza",
        name: "Piojos de la corteza, piojos de los libros",
      },
      {
        id: "mariposas-polillas",
        name: "Mariposas y polillas",
      },
      {
        id: "ciempies",
        name: "Ciempiés",
      },
      {
        id: "cucarachas",
        name: "Cucarachas, mantidos y termitas",
      },
      {
        id: "libelulas",
        name: "Libélulas, caballitos del diablo",
      },
      {
        id: "tijeretas",
        name: "Tijeretas",
      },
      {
        id: "moscas-mosquitos",
        name: "Moscas y mosquitos",
      },
      {
        id: "sinfilas",
        name: "Sinfilas",
      },
      {
        id: "saltamontes",
        name: "Saltamontes, langostas y grillos",
      },
      {
        id: "piojos",
        name: "Piojos",
      },
      {
        id: "milpies",
        name: "Milpiés",
      },
      {
        id: "gusanos-terciopelo",
        name: "Gusanos de terciopelo",
      },
      {
        id: "insectos-escama",
        name: "Insectos escama",
      },
      {
        id: "pececitos-plata",
        name: "Pececitos de plata",
      },
      {
        id: "colembolos",
        name: "Colémbolos",
      },
      {
        id: "caracoles-terrestres",
        name: "Caracoles terrestres",
      },
      {
        id: "crustaceos-terrestres",
        name: "Crustáceos terrestres",
      },
      {
        id: "nematodos-terrestres",
        name: "Nematodos terrestres",
      },
      {
        id: "trips",
        name: "Trips",
      },
      {
        id: "chinches",
        name: "Chinches",
      },
      {
        id: "mohos-mucilaginosos",
        name: "Mohos mucilaginosos verdaderos",
      },
    ],
  },
  {
    id: "invertebrados-marinos",
    name: "INVERTEBRADOS MARINOS",
    icon: "fas fa-fish",
    subcategories: [
      {
        id: "animales-notochord",
        name: "Animales con notochord",
      },
      {
        id: "quetognatos",
        name: "Quetognatos",
      },
      {
        id: "briozoos",
        name: "Briozoos",
      },
      {
        id: "ctenoforos",
        name: "Ctenóforos",
      },
      {
        id: "corales-gorgonias",
        name: "Corales, gorgonias, anémonas de mar y hydroides",
      },
      {
        id: "equinodermos",
        name: "Equinodermos",
      },
      {
        id: "gusanos-marinos",
        name: "Gusanos Marinos",
      },
      {
        id: "aracnidos-marinos",
        name: "Arácnidos marinos",
      },
      {
        id: "crustaceos-marinos",
        name: "Crustáceos Marinos",
      },
      {
        id: "moluscos-marinos",
        name: "Moluscos Marinos",
      },
      {
        id: "nematodos-marinos",
        name: "Nematodos marinos",
      },
      {
        id: "aranas-mar",
        name: "Arañas de mar",
      },
      {
        id: "esponjas",
        name: "Esponjas",
      },
      {
        id: "zooplancton",
        name: "Zooplancton",
      },
    ],
  },
]

// Variables globales
let selectedCategory = null
const downloadStatus = {}

// URLs de ejemplo para simular PDFs encontrados
const samplePDFs = [
  "checklist_amphibia_2023.pdf",
  "species_list_aves_galapagos.pdf",
  "marine_reptiles_inventory.pdf",
  "terrestrial_mammals_guide.pdf",
  "fish_species_catalog.pdf",
  "invertebrates_classification.pdf",
  "endemic_species_report.pdf",
  "biodiversity_assessment.pdf",
]

// Inicializar la aplicación
document.addEventListener("DOMContentLoaded", () => {
  loadCategories()
})

// Cargar categorías
function loadCategories() {
  const categoriesList = document.getElementById("categoriesList")
  categoriesList.innerHTML = ""

  categories.forEach((category) => {
    const categoryElement = document.createElement("div")
    categoryElement.className = "category-item"
    categoryElement.onclick = () => selectCategory(category.id)

    categoryElement.innerHTML = `
            <div class="category-icon">
                <i class="${category.icon}"></i>
            </div>
            <div class="category-info">
                <h3>${category.name}</h3>
                <p>${category.subcategories.length} subcategorías</p>
            </div>
        `

    categoriesList.appendChild(categoryElement)
  })
}

// Seleccionar categoría
function selectCategory(categoryId) {
  selectedCategory = categoryId

  // Actualizar UI de categorías
  document.querySelectorAll(".category-item").forEach((item) => {
    item.classList.remove("active")
  })
  event.currentTarget.classList.add("active")

  // Cargar subcategorías
  loadSubcategories(categoryId)
}

// Cargar subcategorías
function loadSubcategories(categoryId) {
  const category = categories.find((c) => c.id === categoryId)
  const panel = document.getElementById("subcategoriesPanel")

  panel.innerHTML = `
        <div class="panel-header">
            <h2><i class="fas fa-file-alt"></i> Subcategorías - ${category.name}</h2>
            <p>Haz clic en "Descargar PDFs" para obtener todos los archivos de esa subcategoría</p>
        </div>
        <div class="subcategories-grid" id="subcategoriesGrid">
        </div>
    `

  const grid = document.getElementById("subcategoriesGrid")

  category.subcategories.forEach((subcategory) => {
    const subcategoryElement = document.createElement("div")
    subcategoryElement.className = "subcategory-item"

    subcategoryElement.innerHTML = `
            <div class="subcategory-header">
                <div class="subcategory-info">
                    <h4>${subcategory.name}</h4>
                    ${subcategory.description ? `<p>${subcategory.description}</p>` : ""}
                </div>
                <div class="status-badge ${getStatusClass(subcategory.id)}" id="status-${subcategory.id}">
                    ${getStatusText(subcategory.id)}
                </div>
            </div>
            <div class="subcategory-actions">
                <button class="btn btn-primary" onclick="downloadPDFs('${subcategory.id}', '${subcategory.name}')" 
                        id="btn-${subcategory.id}">
                    <i class="fas fa-download"></i>
                    Descargar PDFs
                </button>
            </div>
        `

    grid.appendChild(subcategoryElement)
  })
}

// Obtener clase de estado
function getStatusClass(subcategoryId) {
  const status = downloadStatus[subcategoryId] || "idle"
  return `status-${status}`
}

// Obtener texto de estado
function getStatusText(subcategoryId) {
  const status = downloadStatus[subcategoryId] || "idle"
  switch (status) {
    case "downloading":
      return "Descargando..."
    case "completed":
      return "Completado"
    case "error":
      return "Error"
    default:
      return ""
  }
}

// Función principal de descarga de PDFs
async function downloadPDFs(subcategoryId, subcategoryName) {
  updateDownloadStatus(subcategoryId, "downloading")
  showProgressModal()

  try {
    // Obtener la categoría seleccionada
    const category = categories.find((c) => c.id === selectedCategory)
    
    // Actualizar progreso
    updateProgress(10, "Conectando con el servidor...")
    addLog("Iniciando solicitud al servidor", "info")
    
    // Realizar solicitud al servidor
    const response = await fetch('/api/scrape', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        category: selectedCategory,
        subcategory: subcategoryId,
        subcategoryName: subcategoryName,
        mode: 'live' // Cambiar a 'test' para modo de prueba
      }),
    })
    
    if (!response.ok) {
      throw new Error(`Error en la respuesta del servidor: ${response.status}`)
    }
    
    // Procesar respuesta
    const result = await response.json()
    
    // Actualizar progreso
    updateProgress(50, "Procesando resultados...")
    addLog(`Encontrados ${result.files_found} archivos PDF`, "success")
    updateStats(result.files_found, 0)
    
    // Mostrar resultados de descarga
    if (result.download_results && result.download_results.length > 0) {
      updateProgress(75, "Descargando archivos...")
      
      // Simular descarga progresiva para la UI
      for (let i = 0; i < result.download_results.length; i++) {
        const file = result.download_results[i]
        await new Promise(resolve => setTimeout(resolve, 300))
        
        if (file.success) {
          addLog(`Descargado: ${file.filename}`, "success")
        } else {
          addLog(`Error al descargar: ${file.filename} - ${file.error}`, "error")
        }
        
        updateStats(result.files_found, i + 1)
      }
    }
    
    // Finalizar
    updateProgress(100, "Proceso completado")
    addLog(`Proceso completado: ${result.files_downloaded}/${result.files_found} archivos descargados`, "success")
    
    updateDownloadStatus(subcategoryId, "completed")
    showToast("Descarga completada", `Se procesaron los PDFs de ${subcategoryName}`, "success")
  } catch (error) {
    console.error("Error en la descarga:", error)
    addLog(`Error: ${error.message}`, "error")
    updateDownloadStatus(subcategoryId, "error")
    showToast("Error en la descarga", "Hubo un problema al procesar los archivos.", "error")
  }
}

// Simular el proceso de web scraping
async function simulateWebScraping(subcategoryName) {
  const steps = [
    { text: "Conectando con el servidor de Darwin Foundation...", progress: 10 },
    { text: "Analizando la página web...", progress: 25 },
    { text: "Buscando enlaces PDF...", progress: 40 },
    { text: "Filtrando por subcategoría...", progress: 55 },
    { text: "Descargando archivos encontrados...", progress: 70 },
    { text: "Organizando archivos...", progress: 85 },
    { text: "Finalizando descarga...", progress: 100 },
  ]

  // Simular archivos encontrados
  const foundFiles = Math.floor(Math.random() * 8) + 3 // Entre 3 y 10 archivos
  const downloadedFiles = Math.floor(foundFiles * 0.8) // 80% de éxito en descargas

  updateStats(foundFiles, 0)

  for (let i = 0; i < steps.length; i++) {
    const step = steps[i]

    // Simular tiempo de procesamiento
    await new Promise((resolve) => setTimeout(resolve, 800 + Math.random() * 400))

    updateProgress(step.progress, step.text)

    // Agregar logs específicos
    switch (i) {
      case 0:
        addLog("Estableciendo conexión HTTPS...", "info")
        break
      case 1:
        addLog(`Página cargada: ${Math.floor(Math.random() * 500 + 200)}KB`, "info")
        break
      case 2:
        addLog(`Encontrados ${foundFiles} enlaces PDF`, "success")
        updateStats(foundFiles, 0)
        break
      case 3:
        addLog(`Filtrados por "${subcategoryName}"`, "info")
        break
      case 4:
        // Simular descarga progresiva
        for (let j = 1; j <= downloadedFiles; j++) {
          await new Promise((resolve) => setTimeout(resolve, 200))
          const fileName = samplePDFs[Math.floor(Math.random() * samplePDFs.length)]
          addLog(`Descargado: ${fileName}`, "success")
          updateStats(foundFiles, j)

          // Simular descarga de archivo real
          await downloadFile(fileName, subcategoryName)
        }
        break
      case 5:
        addLog(
          `Archivos organizados en carpeta: ${selectedCategory}/${subcategoryName.toLowerCase().replace(/\s+/g, "-")}`,
          "info",
        )
        break
      case 6:
        addLog(`Proceso completado: ${downloadedFiles}/${foundFiles} archivos descargados`, "success")
        break
    }
  }
}

// Simular descarga de archivo
async function downloadFile(fileName, subcategoryName) {
  // Crear contenido de ejemplo para el PDF
  const pdfContent = generateSamplePDFContent(fileName, subcategoryName)

  // Crear blob y descargar
  const blob = new Blob([pdfContent], { type: "application/pdf" })
  const url = window.URL.createObjectURL(blob)

  // Crear enlace de descarga
  const a = document.createElement("a")
  a.href = url
  a.download = fileName
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)

  // Limpiar URL
  window.URL.revokeObjectURL(url)
}

// Generar contenido de ejemplo para PDF
function generateSamplePDFContent(fileName, subcategoryName) {
  return `%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj

4 0 obj
<<
/Length 200
>>
stream
BT
/F1 16 Tf
50 750 Td
(Darwin Foundation - ${subcategoryName}) Tj
0 -30 Td
/F1 12 Tf
(Archivo: ${fileName}) Tj
0 -20 Td
(Fecha: ${new Date().toLocaleDateString()}) Tj
0 -40 Td
(Este es un archivo de ejemplo generado por) Tj
0 -20 Td
(Darwin Foundation Data Scraper) Tj
0 -40 Td
(Contenido de muestra para ${subcategoryName}) Tj
ET
endstream
endobj

xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000206 00000 n 
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
450
%%EOF`
}

// Actualizar estadísticas de descarga
function updateStats(found, downloaded) {
  document.getElementById("filesFound").textContent = found
  document.getElementById("filesDownloaded").textContent = downloaded
}

// Actualizar estado de descarga
function updateDownloadStatus(subcategoryId, status) {
  downloadStatus[subcategoryId] = status

  const statusElement = document.getElementById(`status-${subcategoryId}`)
  const buttonElement = document.getElementById(`btn-${subcategoryId}`)

  if (statusElement) {
    statusElement.className = `status-badge ${getStatusClass(subcategoryId)}`
    statusElement.textContent = getStatusText(subcategoryId)
  }

  if (buttonElement) {
    if (status === "downloading") {
      buttonElement.disabled = true
      buttonElement.innerHTML = '<div class="loading"></div> Descargando...'
    } else {
      buttonElement.disabled = false
      buttonElement.innerHTML = '<i class="fas fa-download"></i> Descargar PDFs'
    }
  }
}

// Mostrar modal de progreso
function showProgressModal() {
  const modal = document.getElementById("progressModal")
  modal.style.display = "block"

  // Limpiar logs y estadísticas
  document.getElementById("downloadLogs").innerHTML = ""
  updateStats(0, 0)
  updateProgress(0, "Iniciando proceso...")
}

// Cerrar modal
function closeModal() {
  const modal = document.getElementById("progressModal")
  modal.style.display = "none"
}

// Actualizar progreso
function updateProgress(percentage, text) {
  document.getElementById("progressFill").style.width = percentage + "%"
  document.getElementById("progressText").textContent = text
}

// Agregar log
function addLog(message, type = "info") {
  const logsContainer = document.getElementById("downloadLogs")
  const logEntry = document.createElement("div")
  logEntry.className = `log-entry log-${type}`
  logEntry.textContent = `[${new Date().toLocaleTimeString()}] ${message}`
  logsContainer.appendChild(logEntry)
  logsContainer.scrollTop = logsContainer.scrollHeight
}

// Mostrar toast
function showToast(title, message, type = "success") {
  const toastContainer = document.getElementById("toastContainer")
  const toast = document.createElement("div")
  toast.className = `toast ${type}`

  toast.innerHTML = `
        <div class="toast-header">${title}</div>
        <div class="toast-body">${message}</div>
    `

  toastContainer.appendChild(toast)

  // Auto-remove after 5 seconds
  setTimeout(() => {
    toast.remove()
  }, 5000)
}

// Cerrar modal al hacer clic fuera
window.onclick = (event) => {
  const modal = document.getElementById("progressModal")
  if (event.target === modal) {
    closeModal()
  }
}
