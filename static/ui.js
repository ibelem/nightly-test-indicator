$(document).ready(function() {
   $('#chart').click(function() {
       $('div[id^="container"]').slideDown("slow");
       $("h5").slideUp("fast");
       $("table.reports").slideUp("fast");
       $('#chart').attr('class','dison');
       $('#data').removeClass('dison');
   }); 
   $('#data').click(function() {
       $('div[id^="container"]').slideUp("fast");
       $("h5").slideDown("slow");
       $("table.reports").slideDown("slow");
       $('#chart').removeClass('dison');
       $('#data').attr('class','dison');
   });  
  $('#plus').click(function() {
      $('#tog').toggleClass('notdisplay');
        if($('#plus').html() == '+') {
            $('#plus').html('-'); 
        } else {
            $('#plus').html('+'); 
            $('div[id^="container"]').slideDown("slow");
            $("h5").slideDown("slow");
            $("table.reports").slideDown("slow");
        }
  }); 
  $('#updown').click(function() {
      $('header').slideToggle();
      $('#bar').toggleClass('light');
      $('#filter').slideToggle();
      $('footer').slideToggle();
      $('nav').slideToggle();
        if($('#updown').html() == '↑') {
            $('#updown').html('↓'); 
        } else {
            $('#updown').html('↑'); 
        }
  }); 

  $('input[type=checkbox]').click(function() {
    $('#formquery').submit();   
  });      
});