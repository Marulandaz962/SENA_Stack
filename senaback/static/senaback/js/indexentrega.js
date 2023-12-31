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

    await listEntregas();
    
    dataTable = $("#datatables-entregas").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};
const listEntregas = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/senaback/getlist_entregas/");
        const data = await response.json();        
        let content = ``;
        
        data.entregas.forEach((entrega, index) => {                        
            
            content += `
                <tr>
                    <td>${entrega.id}</td>
                    <td>${entrega.elemento_entrega_id}</td>
                    <td>${entrega.fecha_Entrega}</td>
                    <td>${entrega.cantidad}</td>
                    <td>${entrega.responsable_entrega_id}</td>                    
                    <td>${entrega.observaciones}</td>                                        
                    <td><a href='/edicion_elemento_devolutivo/${entrega.id}/' class="btn btn-info edit-button" data-id="${entrega.id}">Editar</a></td>
                    </td>
                </tr>`;
        });
        tableBody_entrega.innerHTML = content;
    } catch (ex) {
        console.warn(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
    
});


//------------------------ Crear entrega -------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
    var btnAbrirModal = document.getElementById("abrir-modal");
    var modal = document.getElementById("formulario-crear-entrega");
    var btnCancelar = document.getElementById("btn-no-guardar-entrega");
    var btnGuardar = document.getElementById("btn-guardar-entrega");

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
