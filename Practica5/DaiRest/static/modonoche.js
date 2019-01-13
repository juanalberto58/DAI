$(document).ready(function(){
    $('.nav-link').click(function(){
      if($(this).attr('id')=='noche'){
        $('body').css('background-color','#221f20');
        $('#logo').attr('src','/static/logo_modo_noche2.png');
      }
    });

});
