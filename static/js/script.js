$(function(){

    $('.fancybox').fancybox();

//var imageWidth = 719;
    var imageWidth = parseInt($(".slider_img img:first").attr('width'));
    var imageSum = $(".slider_img img").size();
    var imageReelWidth = imageWidth * imageSum;
    //Подстроить размер "холста" под новый размер
    $(".slider_img").css({'width' : imageReelWidth});

    var scroll = false;

    function slide_to_right(imageWidth){
        if(scroll == false)
        {
            scroll = true;
            var one_div = imageWidth;
            var container = parseInt($('.slider_img').css("width"));
            var cur_left = parseInt($('.slider_img').css('left'));
            var scroll_h = parseInt($('.slider_img').css("width"));

            var new_left = cur_left - one_div;

            if(Math.abs(cur_left) == (imageReelWidth - imageWidth))
            {
                $('.slider_img').animate({left: 0}, 200, function(){
                    scroll = false;
                    visible_el = $('.slide_article:visible');
                    $('.slide_article').hide();                    
                    $('.slide_article').first().show();
                });
                //new_left = cur_left;
                //scroll = false;
            }
            else
            {
                $('.slider_img').animate({left: new_left}, 100, function(){
                    scroll = false;
                    visible_el = $('.slide_article:visible');
                    $('.slide_article').hide();                    
                    visible_el.next().show();
                });
            }
        }
    }

    function slide_to_left(imageWidth){
        if(scroll == false)
        {
            scroll = true;
            var one_div = imageWidth;
            var container = parseInt($('.slider_img').css("width"));
            var cur_left = parseInt($('.slider_img').css("left"));
            var scroll_h = parseInt($('.slider_img').css("width"));

            var new_left = cur_left + one_div;

            if(Math.abs(cur_left) < imageWidth)
            {
                $('.slider_img').animate({left: -(imageReelWidth - imageWidth)}, 200, function(){
                    scroll = false;
                    visible_el = $('.slide_article:visible');
                    $('.slide_article').hide();                    
                    $('.slide_article').last().show();
                    
                });
            }
            else
            {
                $('.slider_img').animate({left: new_left}, 100, function(){
                    scroll = false;
                    visible_el = $('.slide_article:visible');
                    $('.slide_article').hide();                    
                    visible_el.prev().show();
               	});
            }
        }
    }

var myTimer = 0

function ScrollSlide(){
    clearInterval(myTimer); 
    myTimer = setInterval( function(){slide_to_right(imageWidth) } , 7000)    
    myTimer;
}

ScrollSlide();

    $('.slider_r').click(function(){
        slide_to_right(imageWidth);
        ScrollSlide();
    });

    $('.slider_l').click(function(){
        slide_to_left(imageWidth);
        ScrollSlide();
    });


});

