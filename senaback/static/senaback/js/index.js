
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
                    <td>${consumible.nombre}</td>
                    <td>${consumible.categoria}</td>
                    <td>${consumible.serial}</td>
                    <td>${consumible.cantidad_total}</td>                    
                    <td>${consumible.valor}</td>
                    <td>${consumible.descripcion_elemento}</td>                                      
                    <td>
                    <button class='btn btn-sm btn-primary' data-id="${consumible.id}"><i class='fa-solid fa-pencil'></i></button>
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

document.querySelector("#datatables-consumibles").addEventListener("click", async (e) => {
    if (e.target && e.target.matches("button.btn.btn-sm.btn-primary")) {
        const consumibleId = e.target.getAttribute("data-id");
        
        if (e.target.id === "editarConsumibleButton") {
            // Llena el formulario con los datos del elemento consumible a editar
            await fillEditForm(consumibleId);
            
            const formularioEditarElemento = document.querySelector("#formulario-editar-elemento");
            formularioEditarElemento.style.display = "block";
        }
    }
});



document.querySelector("#datatables-consumibles").addEventListener("click", async (e) => {
    if (e.target && e.target.matches("button.btn.btn-sm.btn-primary") && e.target.id === "editarConsumibleButton") {
        const consumibleId = e.target.getAttribute("data-id");
        await fillEditForm(consumibleId);
        
        const formularioEditarElemento = document.querySelector("#formulario-editar-elemento");
        formularioEditarElemento.style.display = "block";
    }
});

const editConsumibleForm = document.querySelector("#editConsumible");
editConsumibleForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const consumibleId = editConsumibleForm.querySelector("[name='id']").value; // Obtiene el ID del formulario
    const formData = new FormData(editConsumibleForm);
    formData.append("id", consumibleId);
    await updateConsumible(formData);
    document.querySelector("#formulario-editar-elemento").style.display = "none";
    await listConsumables();
});




  // Traer los Datos del Elemento al FDormulario de Editar:

  // Agrega una función para llenar el formulario de edición con los datos del elemento consumible
    const fillEditForm = async (consumibleId) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/senaback/get_consumable_details/${consumibleId}`);
        const consumibleData = await response.json();
        
        // Llena los campos del formulario con los datos del elemento consumible
        document.querySelector("#username").value = consumibleData.nombre;
        document.querySelector("#categoria").value = consumibleData.categoria;
        document.querySelector("#serial").value = consumibleData.serial;
        document.querySelector("#cantidad").value = consumibleData.cantidad_total;
        document.querySelector("#valor").value = consumibleData.valor;
        document.querySelector("#descripcion").value = consumibleData.descripcion_elemento;
    } catch (ex) {
        console.warn(ex);
    }
};
