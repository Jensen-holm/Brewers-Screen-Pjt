function sortTable(table, col = "", asc = true) {
    const dirModifier = asc ? 1 : -1;
    const body = table.tBodies[0];
    const rows = Array.from(body.querySelectorAll("tr"))

    // now sort them
    var sortedRows = rows.sort((a, b) => {
        const aTxt = a.querySelector(`td:nth-child(${column + 1})`).textContent.trim()
        const bTxt = b.querySelector(`td:nth-child(${column + 1})`).textContent.trim()

    })
}

