function openNav() {
    $( ".navbar" ).css( "width", "250px" );
    $( ".section" ).css( "z-index", "-1" );
  }
  
  function closeNav() {
    $( ".navbar" ).css( "width", "0" );
    $( ".section" ).css( "z-index", "0" );
    $( ".section" ).css( "transition", "0.5s" );
  }