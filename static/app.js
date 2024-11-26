// Manejo del formulario de texto (Matriz de texto)
document.getElementById("wordsearch-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const matrixInput = document.getElementById("matrix").value.trim();
    const wordsInput = document.getElementById("words").value.trim();

    if (!matrixInput || !wordsInput) {
        alert("Por favor, completa todos los campos.");
        return;
    }

    const matrix = matrixInput.split("\n").map(row => row.trim());
    const words = wordsInput.split(",").map(word => word.trim());

    try {
        const response = await fetch("/solve", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ matrix, words }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.error}`);
            return;
        }

        const results = await response.json();

        // Mostrar resultados en el modal
        showHighlightedMatrix(matrix, results.coordinates, results.found, results.not_found);

        // Activar botón de descarga
        const downloadBtn = document.getElementById("download-btn");
        downloadBtn.style.display = "block";
        downloadBtn.onclick = () => downloadResults(results);

    } catch (error) {
        console.error("Error en la solicitud:", error);
        alert("Hubo un error al procesar la solicitud.");
    }
});

// Manejo del formulario de imagen (Reconocimiento de matriz)
document.getElementById("process-image-btn").addEventListener("click", async () => {
    const imageInput = document.getElementById("image-input");

    if (!imageInput.files[0]) {
        alert("Por favor, sube una imagen.");
        return;
    }

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);

    try {
        console.log("Enviando imagen al servidor...");
        const response = await fetch("/process-image", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(`Error: ${errorData.error}`);
            return;
        }

        const result = await response.json();
        console.log("Respuesta del servidor:", result);

        // Actualizar el campo de texto con la matriz extraída
        document.getElementById("generated-matrix").value = result.matrix;

    } catch (error) {
        console.error("Error al procesar la imagen:", error);
        alert("Hubo un error al procesar la imagen.");
    }
});

// Funciones adicionales
function generateUniqueColors(n) {
    const colors = new Set();
    while (colors.size < n) {
        // Generar un color hexadecimal aleatorio
        const color = `#${Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0')}`;
        colors.add(color);
    }
    return Array.from(colors);
}

function showHighlightedMatrix(matrix, coordinates, foundWords, notFoundWords) {
    const modal = document.getElementById("matrix-modal");
    const highlightedMatrixDiv = document.getElementById("highlighted-matrix");
    const notFoundList = document.getElementById("not-found-list");
    const foundList = document.getElementById("found-list");

    // Limpiar contenido previo
    highlightedMatrixDiv.innerHTML = "";
    notFoundList.innerHTML = "";
    foundList.innerHTML = "";

    // Crear la matriz resaltada con colores para palabras encontradas
    const wordColors = {};
    const uniqueColors = generateUniqueColors(foundWords.length);
    foundWords.forEach((word, index) => {
        wordColors[word] = uniqueColors[index];
    });

    matrix.forEach((row, rowIndex) => {
        const rowDiv = document.createElement("div");
        row.split(",").forEach((cell, colIndex) => {
            const cellDiv = document.createElement("div");
            cellDiv.className = "cell";
            cellDiv.textContent = cell;

            for (const word in coordinates) {
                coordinates[word].forEach(([r, c]) => {
                    if (r === rowIndex && c === colIndex) {
                        cellDiv.classList.add("highlighted");
                        cellDiv.style.backgroundColor = wordColors[word];
                        cellDiv.style.color = "white"; // Para contraste
                    }
                });
            }

            rowDiv.appendChild(cellDiv);
        });
        highlightedMatrixDiv.appendChild(rowDiv);
    });

    // Agregar las palabras no encontradas
    notFoundWords.forEach(word => {
        const wordItem = document.createElement("li");
        wordItem.textContent = word;
        wordItem.style.color = "red"; 
        notFoundList.appendChild(wordItem);
    });

    // Agregar las palabras encontradas
    foundWords.forEach(word => {
        const wordItem = document.createElement("li");
        wordItem.textContent = word;
        wordItem.style.color = wordColors[word]; 
        foundList.appendChild(wordItem);
    });

    // Mostrar modal
    modal.style.display = "flex";

    // Cerrar modal
    document.querySelector(".close").onclick = () => {
        modal.style.display = "none";
    };
    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
}

function downloadResults(results) {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(results));
    const downloadAnchor = document.createElement("a");
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", "results.json");
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
}

// Cambiar entre las pestañas
document.querySelectorAll(".tab-button").forEach(button => {
    button.addEventListener("click", () => {
        const activeTab = document.querySelector(".tab-button.active");
        const activeContent = document.querySelector(".tab-content.active");

        // Desactivar la pestaña activa y el contenido correspondiente
        activeTab.classList.remove("active");
        activeContent.classList.remove("active");

        // Activar la nueva pestaña y su contenido
        button.classList.add("active");
        document.getElementById(button.getAttribute("data-tab")).classList.add("active");
    });
});
