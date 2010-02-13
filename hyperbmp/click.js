$("td").click(function() {
	var link = $(this).attr('href');
	if( link ) {
	    document.location = link;
	};
    });
