var canSlide = true;

$(document).ready(function(){
    $(".search-img").mouseenter(function() {
        if ($("#header-search-text-box").css("display") == "none" && canSlide == true)
        {   
            JustSlid();
            $("#header-search-text-box").css("display", "inline-block");
            $("#header-search-text-box").css("width", "0px");
            $("#header-search-text-box").animate({"width":"+=150"}, 500);
            
        }
    });
    
    $("#header-search-text-box").mouseleave(function() {
        if ($("#header-search-text-box").val() == "" && canSlide == true)
        {
            JustSlid();
            $("#header-search-text-box").animate({"width":"-=150"}, 500, function() {
                $("#header-search-text-box").css("display", "none");
            });
        }
    });

});
function JustSlid() {
    FlipSlide();
    setTimeout('FlipSlide()', 2000);
}

function FlipSlide() {
    canSlide = !canSlide;
}
