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

    await listDevolutivos();

    dataTable = $("#datatables-devolutivos").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listDevolutivos = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/senaback/getlist_devolutivos/");
        const data = await response.json();
        console.log(data);

        let content = ``;
        data.devolutivos.forEach((devolutivo, index) => {
            content += `
                <tr>
                    <td>${devolutivo.id}</td>
                    <td>${devolutivo.nombre_devolutivo}</td>
                    <td>${devolutivo.categoria_devolutivo}</td>
                    <td>${devolutivo.serial}</td>
                    <td>${devolutivo.serial_sena}</td>
                    <td>${devolutivo.descripcion_devolutivo}</td>
                    <td>${devolutivo.valor_devolutivo}</td>
                    <td><a href='/edicion_elemento_devolutivo/${devolutivo.id}/' class="btn btn-info edit-button" data-id="${devolutivo.id}">Editar</a></td>
                    </td>
    
                </tr>`;
        });


        $("#datatables-devolutivos tbody").html(content);
    } catch (ex) {
        console.warn(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});




// Crear Elemento Devolutivo

document.addEventListener("DOMContentLoaded", function () {
    // Obtén el modal y los botones de abrir y cerrar
    const modalCrearElementoDevolutivo = document.getElementById('formulario-crear-elemento_devolutivo');
    const abrirModalBotonDevolutivo = document.getElementById('abrir-modal-devolutivo');
    const cerrarModalBotonDevolutivo = document.getElementById('close-modal-devolutivo');
    const guardarModalBotonDevolutivo = document.getElementById('btn-guardar-devolutivo');
    const cancelarModalBotonDevolutivo = document.getElementById('btn-no-guardar-devolutivo'); 
    
    // Agrega un evento click al botón de abrir para mostrar el modal
    abrirModalBotonDevolutivo.addEventListener('click', function() {
        modalCrearElementoDevolutivo.style.display = 'block';
    });
    
    // Agrega un evento click al botón de cerrar para ocultar el modal
    cerrarModalBotonDevolutivo.addEventListener('click', function() {
        modalCrearElementoDevolutivo.style.display = 'none';
    });
    
    // Agrega un evento click al botón de guardar para enviar el formulario y cerrar el modal
    guardarModalBotonDevolutivo.addEventListener('click', function() {
      // Envía el formulario (puede que necesites agregar validación aquí)
      document.querySelector('form').submit();
    
      // Cierra el modal
      modalCrearElementoDevolutivo.style.display = 'none';
    });
    
    // Agrega un evento click al botón de cancelar para cerrar el modal
    cancelarModalBotonDevolutivo.addEventListener('click', function() {
      // Cierra el modal sin enviar el formulario
      modalCrearElementoDevolutivo.style.display = 'none';
    });
    
    // Cierra el modal si se hace clic fuera del contenido del modal
    window.addEventListener('click', function(event) {
      if (event.target == modalCrearElementoDevolutivo) {
        modalCrearElementoDevolutivo.style.display = 'none';
      }
    });
    
    });