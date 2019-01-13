$(document).ready(function(){
    $('.nav-link').click(function(){
      if($(this).attr('id') == 'dia'){
        $('body').css('background-color','white');
        $('#logo').attr('src','/static/logo-UGR-color-vertical.jpg');
      }
    });
});
