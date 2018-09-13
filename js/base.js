function setTableID() {
		document.getElementsByTagName("table")[0].setAttribute("id","tableid");
		$('#tableid').DataTable( {
			scrollY:        "200px",
			scrollX:        true,
			scrollCollapse: true,
			paging:         false,
			fixedColumns:   {
				leftColumns: 1,
			}
		} );
	} onload = setTableID;