$(document).ready(function(){
    $('.nav-link').click(function(){

        if($(this).attr('id') == 'grande'){
            $('body').css('font-size','20px');
        }
        else if(this.id == 'pequena'){
            $('body').css('font-size','9px');
        }
        else if(this.id == "normal"){
            $('body').css('font-size','');
        }
    });
});
