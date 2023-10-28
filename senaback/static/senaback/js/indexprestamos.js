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
        const response = await fetch("http://127.0.0.1:8000/senaback/getlist_prestamos/");
        const data = await response.json();        
        let content = ``;
        data.prestamos.forEach((prestamos, index) => {                        
            
            content += `
                <tr>
                    <td>${prestamos.id}</td>
                    <td>${prestamos.elemento_prestamo_id}</td>
                    <td>${prestamos.responsable_prestamo_id}</td>  
                    <td>${prestamos.fecha_Prestamo}</td>
                    <td>${prestamos.fecha_Devolucion}</td>
                    <td>${prestamos.observaciones}</td>
                    <td>${prestamos.estado}</td>                  
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>                        
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
  
// Obtén el modal y los botones de abrir y cerrar
// var modalCrearEntrega = document.getElementById('formulario-crear-entrega');
// var abrirModalBoton = document.getElementById('abrir-modal');
// var cerrarModalBoton = document.getElementById('close-modal');
// var guardarModalBoton = document.getElementById('btn-guardar-crear');
// var cancelarModalBoton = document.getElementById('btn-no-guardar-crear'); // Agrega este botón

// // Agrega un evento click al botón de abrir para mostrar el modal
// abrirModalBoton.addEventListener('click', function() {
//   modalCrearEntrega.style.display = 'block';
// });

// // Agrega un evento click al botón de cerrar para ocultar el modal
// cerrarModalBoton.addEventListener('click', function() {
//     modalCrearEntrega.style.display = 'none';
// });

// // Agrega un evento click al botón de guardar para enviar el formulario y cerrar el modal
// guardarModalBoton.addEventListener('click', function() {
//   // Envía el formulario (puede que necesites agregar validación aquí)
//   document.querySelector('form').submit();

//   // Cierra el modal
//   modalCrearEntrega.style.display = 'none';
// });

// // Agrega un evento click al botón de cancelar para cerrar el modal
// cancelarModalBoton.addEventListener('click', function() {
//   // Cierra el modal sin enviar el formulario
//   modalCrearEntrega.style.display = 'none';
// });

// // Cierra el modal si se hace clic fuera del contenido del modal
// window.addEventListener('click', function(event) {
//   if (event.target == modalCrearEntrega) {
//     modalCrearEntrega.style.display = 'none';
//   }
// });
