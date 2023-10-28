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
	console.log('Inicializando tabla');

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
						<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
							Editar Elemento
						</button>
						
					</td>
				</tr>`;
		});
		// Agregar contenido a la tabla
		$("#datatables-consumibles tbody").html(content);
	} catch (ex) {
		console.warn(ex);
	}
};

window.addEventListener("load", async () => {
	await initDataTable();
});





//-------------  Editar Elemento -------------------------------------

$(document).ready(function () {
	// Agrega un evento click al botón "Editar Elemento" de la tabla
	$('#datatables-consumibles').on('click', '.btn-primary', function () {
	  // Abre el modal con el id "formulario-editar-elemento"
	  $('#formulario-editar-elemento').modal('show');
	});
  
	// Agrega un evento click al botón "Guardar" dentro del modal
	$('#btn-guardar-editar').click(function () {

		
	  $('#formulario-editar-elemento').modal('hide');
	});
  
	// Agrega un evento click al botón "Cancelar" dentro del modal
	$('#btn-no-guardar-editar').click(function () {
	  // Realiza las acciones que deseas al hacer clic en "Cancelar"
	  // Por ejemplo, puedes restablecer los valores del formulario
	  // Luego, cierra el modal
	  $('#formulario-editar-elemento').modal('hide');
	});
  });
  

