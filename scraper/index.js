$(document).ready(function() {

  $.getJSON( "data.json", function( data ) {

    data.forEach(appendData);

    function appendData(item, index) {

      var url = item.url;
      var ad = item.ad;
      var loc = item.location;
      var title = item.title;

      var appendThis =

        "<div class='ad'><h2>" + title + "</h2><h3>" + loc + "</h3><p>" + ad + "</p></div>"
      $('#data-container').append(appendThis);
      console.log(item);
    }

  });

}) // close file
