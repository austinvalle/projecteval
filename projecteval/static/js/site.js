var canSlide = true;

$(document).ready(function(){
    $(".search-img").mouseenter(function() {
        SlideSearch(false);
    });
    
    $("#header-search-text-box").mouseleave(function() {
        SlideSearch(true);
    });

    $("#login-container a").click(function() {
        ToggleLoginDisplay();
    });

});

// Login section //

function ToggleLoginDisplay() {
    if ($("#login-form-container").css("display") == "none")
    {
        $("#login-form-container").css("display", "inline-block");
        var maxHeight = $("#login-form-container").height();
        $("#login-form-container").css("height", "0px")
        $("#login-form-container").animate({"height":"+=" + maxHeight}, 500, function() {
                $("#login-form-container").css("height", "auto");
            });
    }
    else
    {
        var maxHeight = $("#login-form-container").height();
        $("#login-form-container").animate({"height":"-=" + maxHeight}, 500, function() {
                $("#login-form-container").css("height", "auto");
                $("#login-form-container").css("display", "none");
            });
    }
}

function Login() {
    var form = { "email": $("#login_email").val(), "password": $("#login_password").val(), "csrf_token" : $("#csrf_token").val() };
    
    $.ajax({
        type:"POST",
        url:"http://0.0.0.0:8080/login/",
        data:form,
        //dataType:"application/json;charset=UTF-8",
        success: function(response) {
                ReadLoginResponse(response, true);
            }
    });
}

function ReadLoginResponse(response, isLogin) {
    var jsonResponse = $.parseJSON(JSON.stringify(response));
    if (jsonResponse.success == "true")
    {
        // redirect or something (can decide later)
        window.location.reload();
    }
    else
    {
        // Output errors
        var login_errors = ( isLogin ? "#login_errors" : "#register_errors" );
        $(login_errors).empty();
        $(jsonResponse.errors).each(function(index) {
            var error = $("<li/>").text(this);
            $(login_errors).append(error);
            });
    }
}

function Register() {
    if ($("#register_password").val() == $("#register_confirm_password").val())
    {
        var form = { "email": $("#register_email").val(), "username": $("#register_username").val(), "password": $("#register_password").val(), "csrf_token" : $("#csrf_token").val() };
        
        $.ajax({
            type:"POST",
            url:"http://0.0.0.0:8080/register/",
            data:form,
            //dataType:"application/json;charset=UTF-8",
            success: function(response) {
                    ReadLoginResponse(response, false);
                }
        });
    }
    else
    {
        ReadLoginResponse({ "success" : false, "errors" : ["Your passwords didn't match"] }, false);
    }
}

// End login section //


// Log out section //

function Logout() {
    $.ajax({
    type:"POST",
    url:"http://0.0.0.0:8080/logout/",
    data: { "csrf_token" : $("#csrf_token").val() },
    //dataType:"application/json;charset=UTF-8",
    success: function(response) {
            window.location.reload();
        }
    });
}

// End log out section //


// Search Button section //
function JustSlid() {
    FlipSlide();
    setTimeout('FlipSlide()', 2000);
}

function FlipSlide() {
    canSlide = !canSlide;
}

function SlideSearch(slideLeft) {
    if (canSlide == false)
    {
        return;
    }

    if ($("#header-search-text-box").css("display") == "none" && slideLeft == false)
    {   
        JustSlid();
        $("#header-search-text-box").css("display", "inline-block");
        $("#header-search-text-box").css("width", "0px");
        $("#header-search-text-box").animate({"width":"+=150"}, 500);
        
    }
    else
    if ($("#header-search-text-box").val() == "" && slideLeft == true)
    {
        JustSlid();
        $("#header-search-text-box").animate({"width":"-=150"}, 500, function() {
            $("#header-search-text-box").css("display", "none");
        });
    }
}
// End search button section //
