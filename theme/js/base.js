window.addEventListener('load', function () {
    $('#tableid').DataTable( {
		scrollY:        "400px",
		//scrollX:        true,
		scrollCollapse: true,
		paging:         false,
		info:			false,
		/*fixedColumns:   {
			leftColumns: 1,
		}*/
	} );
});