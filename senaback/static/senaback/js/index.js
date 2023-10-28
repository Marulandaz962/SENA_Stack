
// logica de la tabla de Boostrap
let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
	dom: '<lf<t>ip>B',
	buttons: [
		'pdf'
	],
	columnDefs: [
		{ className: "centered", targets: [0, 1, 2, 3, 4, 5, 6] },
		{ orderable: false, targets: [5, 6] },
		{ searchable: false, targets: [0, 5, 6] }
	],
	pageLength: 4,
	destroy: true
};

const initDataTable = async () => {
	console.log('inicializando tabla');

	if (dataTableIsInitialized) {
		dataTable.destroy();
		
	}

	await listConsumables();
	
	dataTable = $("#datatables-consumibles").DataTable(dataTableOptions);

	dataTableIsInitialized = true;
};
const listConsumables = async () => {
	try {
		const response = await fetch("http://127.0.0.1:8000/senaback/getlist_consumables/");
		const data = await response.json();

		let content = ``;
		data.consumibles.forEach((consumible, index) => {
			content += `
				<tr>
					<td>${consumible.id}</td>
					<td>${consumible.nombre_consumible}</td>
					<td>${consumible.categoria}</td>
					<td>${consumible.serial}</td>
					<td>${consumible.cantidad_total}</td>                    
					<td>${consumible.valor}</td>
					<td>${consumible.descripcion_elemento}</td>                                      
					<td>

					<button type="button" id="editar-elemento" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
					Launch static backdrop modal
					</button>					
					</td>
				</tr>`;
		});
		tableBody_consumables.innerHTML = content;
	} catch (ex) {
		console.warn(ex);
	}
};

window.addEventListener("load", async () => {
	await initDataTable();
	
});




//-------------  Editar Elemento -------------------------------------

// Obtén el modal y los botones de abrir y cerrar
var modalEditarElemento = document.getElementById('formulario-editar-elemento');
var abrirModalBotonEditar = document.getElementById('boton-editar');
var cerrarModalBoton = document.getElementById('close-modal');
var guardarModalBoton = document.getElementById('btn-guardar-editar');
var cancelarModalBoton = document.getElementById('btn-no-guardar-editar'); // Agrega este botón

// Agrega un evento click al botón de abrir para mostrar el modal
abrirModalBotonEditar.addEventListener('click', function() {
  modalEditarElemento.style.display = 'block';
});

// Agrega un evento click al botón de cerrar para ocultar el modal
cerrarModalBoton.addEventListener('click', function() {
  modalEditarElemento.style.display = 'none';
});

// Agrega un evento click al botón de guardar para enviar el formulario y cerrar el modal
guardarModalBoton.addEventListener('click', function() {
  // Envía el formulario (puede que necesites agregar validación aquí)
  document.querySelector('form').submit();

  // Cierra el modal
  modalEditarElemento.style.display = 'none';
});

// Agrega un evento click al botón de cancelar para cerrar el modal
cancelarModalBoton.addEventListener('click', function() {
  // Cierra el modal sin enviar el formulario
  modalEditarElemento.style.display = 'none';
});

// Cierra el modal si se hace clic fuera del contenido del modal
window.addEventListener('click', function(event) {
  if (event.target == modalEditarElemento) {
	modalEditarElemento.style.display = 'none';
  }
});


