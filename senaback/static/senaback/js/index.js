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
						<td><a href='/edicion_elemento/${consumible.id}/' class="btn btn-info edit-button" data-id="${consumible.id}">Editar</a></td>
						</td>
		
					</tr>`;
			});


			// document.addEventListener("click", (e) => {

			// 	if (e.target && e.target.classList.contains("edit-button")) {
			// 		const id = e.target.getAttribute("data-id");
			// 		window.location.href = `/senaback/templates/senaback/editarElementos.html/${id}/`;  
			// 	}

			// 	window.location.href = `/senaback/templates/senaback/editarElementos.html/${id}/`;
			// });
			

			// Agregar contenido a la tabla
			$("#datatables-consumibles tbody").html(content);
		} catch (ex) {
			console.warn(ex);
		}
	};

	window.addEventListener("load", async () => {
		await initDataTable();
	});




