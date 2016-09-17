jQuery(function(f){
    var element = f('#mainNav');
    f(window).scroll(function(){
        element['fade'+ (f(this).scrollTop() > 200 ? 'In': 'Out')](500);           
    });
});

$( "#target" ).click(function() {
  alert( "Handler for .click() called." );
});