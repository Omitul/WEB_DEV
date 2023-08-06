$(document).ready(function(){
   $('#click').click(function(){
     $('#Box').slideDown(6000);
   });
   $('#stop').click(function(){
      $('#Box').stop();
   });
});