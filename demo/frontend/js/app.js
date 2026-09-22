/**
 * Demo funcional de RecomendaBook (frontend)
 *
 * Consulta el backend (FastAPI) y dibuja el catalogo de libros, comics y
 * manga. Incluye filtros simples por tipo de obra.
 *
 * Si el backend no esta corriendo, o esta en otra direccion, cambia
 * la constante API_URL de abajo.
 */
const API_URL = "http://127.0.0.1:8000";

const catalogoEl = document.getElementById("catalogo");
const estadoEl = document.getElementById("estado");
const filtros = document.querySelectorAll(".filtro");

async function cargarLibros(tipo) {
  estadoEl.textContent = "Cargando catalogo...";
  estadoEl.style.display = "block";
  catalogoEl.innerHTML = "";

  try {
    const url = tipo ? `${API_URL}/libros?tipo=${tipo}` : `${API_URL}/libros`;
    const respuesta = await fetch(url);

    if (!respuesta.ok) {
      throw new Error(`El backend respondio con estado ${respuesta.status}`);
    }

    const libros = await respuesta.json();
    dibujarCatalogo(libros);
  } catch (error) {
    estadoEl.textContent =
      "No se pudo conectar con el backend. Verifica que este corriendo en " +
      API_URL + " (revisa el README del demo).";
    console.error(error);
  }
}

function dibujarCatalogo(libros) {
  if (libros.length === 0) {
    estadoEl.textContent = "No hay obras para este filtro.";
    return;
  }

  estadoEl.style.display = "none";
  catalogoEl.innerHTML = libros.map(tarjetaHTML).join("");
}

function tarjetaHTML(libro) {
  return `
    <article class="tarjeta">
      <span class="etiqueta">${libro.tipo}</span>
      <h2>${libro.titulo}</h2>
      <p class="autor">${libro.autor} &middot; ${libro.genero}</p>
      <p class="calificacion">Calificacion: ${libro.calificacion} / 5</p>
    </article>
  `;
}

filtros.forEach((boton) => {
  boton.addEventListener("click", () => {
    filtros.forEach((b) => b.classList.remove("activo"));
    boton.classList.add("activo");
    cargarLibros(boton.dataset.tipo);
  });
});

cargarLibros("");
