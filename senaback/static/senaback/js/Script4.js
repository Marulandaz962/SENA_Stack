
  //------------------------ Crear elemento Devolutivo-------------------------------------------------------
  
document.addEventListener("DOMContentLoaded", function () {
// Obtén el modal y los botones de abrir y cerrar
var modalCrearElemento = document.getElementById('formulario-crear-elemento');
var abrirModalBoton = document.getElementById('abrir-modal');
var cerrarModalBoton = document.getElementById('close-modal');
var guardarModalBoton = document.getElementById('btn-guardar-crear');
var cancelarModalBoton = document.getElementById('btn-no-guardar-crear'); // Agrega este botón

// Agrega un evento click al botón de abrir para mostrar el modal
abrirModalBoton.addEventListener('click', function() {
  modalCrearElemento.style.display = 'block';
});

// Agrega un evento click al botón de cerrar para ocultar el modal
cerrarModalBoton.addEventListener('click', function() {
  modalCrearElemento.style.display = 'none';
});

// Agrega un evento click al botón de guardar para enviar el formulario y cerrar el modal
guardarModalBoton.addEventListener('click', function() {
  // Envía el formulario (puede que necesites agregar validación aquí)
  document.querySelector('form').submit();

  // Cierra el modal
  modalCrearElemento.style.display = 'none';
});

// Agrega un evento click al botón de cancelar para cerrar el modal
cancelarModalBoton.addEventListener('click', function() {
  // Cierra el modal sin enviar el formulario
  modalCrearElemento.style.display = 'none';
});

// Cierra el modal si se hace clic fuera del contenido del modal
window.addEventListener('click', function(event) {
  if (event.target == modalCrearElemento) {
    modalCrearElemento.style.display = 'none';
  }
});

});



