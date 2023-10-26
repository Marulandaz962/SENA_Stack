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
                    <td>${entrega.elemento_entrega}</td>
                    <td>${entrega.fecha_Entrega}</td>
                    <td>${entrega.cantidad}</td>
                    <td>${entrega.responsable_entrega}</td>                    
                    <td>${entrega.observaciones}</td>                    
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>                        
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