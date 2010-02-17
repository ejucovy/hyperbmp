var serialize = function() {
    var data = table_to_csv();
    $("#resource_body").attr('value', data);
};

var table_to_csv = function() {
    var data = '';
    $("table tr").each(function() {

	    $(this).children("td").each(function() {
		    var color = $(this).attr('class');
		    var href = $(this).attr('href');
		    if( href ) color = color + '>' + href;
		    data = data + color + ',';
		});
	    data = data.replace(/,$/g, '\n');
	});
    return data;
};

var paint_square = function() {
    var color = $("input[name=brush]:checked")[0].value;
    if( color == 'link' ) {
        $(this).attr('href', $("input#hyperlink").attr('value'));
    } else {
      if( color == 'custom' ) {
        color = $("input#customcolor").attr('value');
      }
      $(this).css({backgroundColor: color});
      $(this).attr('class', color);
    };
};

var go = function() {
    var link = $(this).attr('href');
    if( link ) {
        document.location = link;
    };
};
