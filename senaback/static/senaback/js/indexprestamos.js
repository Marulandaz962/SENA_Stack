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

    await listPrestamos();
    
    dataTable = $("#datatables-prestamos").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};
const listPrestamos = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/senaback/getlist_prestamos");
        const data = await response.json();     
        let content = ``;
        data.prestamos.forEach((prestamo, index) => {                        
            
            content += `
                <tr>
                    <td>${prestamo.id}</td>
                    <td>${prestamo.elemento_prestamo_id}</td>
                    <td>${prestamo.responsable_prestamo_id}</td>  
                    <td>${prestamo.fecha_Prestamo}</td>
                    <td>${prestamo.fecha_Devolucion}</td>
                    <td>${prestamo.observaciones}</td>
                    <td>${prestamo.estado}</td>                  
                    <td><a href='/edicion_elemento_devolutivo/${prestamo.id}/' class="btn btn-info edit-button" data-id="${prestamo.id}">Editar</a></td>
                    </td>
                </tr>`;
        });
        tableBody_prestamos.innerHTML = content;
    } catch (ex) {
        console.warn(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});


//------------------------ Crear elemento -------------------------------------------------------
  
document.addEventListener("DOMContentLoaded", function () {
    var btnAbrirModal = document.getElementById("abrir-modal");
    var modal = document.getElementById("formulario-crear-prestamo");
    var btnCancelar = document.getElementById("btn-no-guardar-prestamo");
    var btnGuardar = document.getElementById("btn-guardar-prestamo");

    if (btnAbrirModal && modal && btnCancelar && btnGuardar) {
        btnAbrirModal.addEventListener("click", function () {
            modal.style.display = "block";
        });

        btnCancelar.addEventListener("click", function () {
            modal.style.display = "none";
        });

        btnGuardar.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }
});
