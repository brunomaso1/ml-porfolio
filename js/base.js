function setTableID() {
		document.getElementsByTagName("table")[0].setAttribute("id","tableid");
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
	} onload = setTableID;