var canSlide = true;
var emailRegex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
var userNameRegex = /^[a-zA-Z][a-zA-Z0-9]{5,24}$/; // starts with letter, between 6 and 25 chars long
var passwordRegex = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,25}/; // at least one number, one lower case letter, one upper case letter, and 6-25 chars long
var dateRegex = /^(\d){1,2}\/(\d){1,2}\/(\d){4}$/;
var urlRegex = /^([a-z][a-z0-9\*\-\.]*):\/\/(?:(?:(?:[\w\.\-\+!$&'\(\)*\+,;=]|%[0-9a-f]{2})+:)*(?:[\w\.\-\+%!$&'\(\)*\+,;=]|%[0-9a-f]{2})+@)?(?:(?:[a-z0-9\-\.]|%[0-9a-f]{2})+|(?:\[(?:[0-9a-f]{0,4}:)*(?:[0-9a-f]{0,4})\]))(?::[0-9]+)?(?:[\/|\?](?:[\w#!:\.\?\+=&@!$'~*,;\/\(\)\[\]\-]|%[0-9a-f]{2})*)?$/


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

    SetUpAuthValidation();
    SetUpEditGameValidation();
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
    if (ValidateLoginControls())
    {
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
    if (ValidateRegisterControls())
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

function ValidateRegisterControls() {
    var rv = true;
    if (!Validate($("#register_email"), emailRegex)) 
    {
        rv = false;
    }
    if (!Validate($("#register_username"), userNameRegex)) 
    {
        rv = false;
    }
    if (!Validate($("#register_password"), passwordRegex)) 
    {
        rv = false;
    }
    if (!Validate($("#register_confirm_password"), passwordRegex)) 
    {
        rv = false;
    }
    return rv;
}

function ValidateLoginControls() {
    var rv = true;
    if (!Validate($("#login_email"), emailRegex)) 
    {
        rv = false;
    }
    if (!Validate($("#login_password"), passwordRegex)) 
    {
        rv = false;
    }

    return rv;
}

function SetUpAuthValidation() {
    $("#register_email").keyup(function() {
        Validate($(this), emailRegex);
    });

    $("#login_email").keyup(function() {
        Validate($(this), emailRegex);
    });

    $("#register_username").keyup(function() {
        Validate($(this), userNameRegex);
    });

    $("#register_password").keyup(function() {
        Validate($(this), passwordRegex);
    });

    $("#register_confirm_password").keyup(function() {
        Validate($(this), passwordRegex, $("#register_password").val());
    });
    
    $("#login_password").keyup(function() {
        Validate($(this), passwordRegex);
    });
}

function IsValid(value, regex) {
    if (value == "" || !regex.test(value))
    {
        return false;
    }
    return true;
}

function Validate(input, regex, compareValue) {
    if (!IsValid(input.val(), regex) || (compareValue != undefined && input.val() != compareValue))
    {
        ToggleDisplayError(true, input);
        return false;
    }
    else
    {
        ToggleDisplayError(false, input);
        return true;
    }
}

function ToggleDisplayError(addError, element) {
    if (addError)
    {
        element.addClass("red-border");
    }
    else
    {
        element.removeClass("red-border");
    }
}

function DateValidate(input, regex, compareValue) {
    if (Validate(input, regex, compareValue))
    {
        var timeStamp = Date.parse(input.val());
        if (isNaN(timeStamp))
        {
            ToggleDisplayError(true, input);
            return false;
        }
        return true;
    }
    return false;
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


// Start Edit Game section //

function SaveGame() {
    if (ValidateEditGameControls())
    {
        var form = BuildGameForm();
        
        $.ajax({
            type:"POST",
            url:"http://0.0.0.0:8080/edit/games/",
            data:form,
            //dataType:"application/json;charset=UTF-8",
            success: function(response) {
                    ReadSaveGameReponse(response);
                }
        });
    }
}

function BuildGameForm() {
    var platforms = [];
    $(".game_platform_input").each(function() {
        if ($(this).prop("checked"))
        {
            platforms.push({ "id" : $(this).val() });
        }
    });
    return { "csrf_token" : $("#csrf_token").val(),
             "desc" : $("#game_desc").val(),
             "id" : $("#game_id").val(),
             "title" : $("#game_title").val(),
             "release_date" : $("#game_release_date").val(),
             "developer" : $("#game_developer").val(),
             "publisher" : $("#game_publisher").val(),
             "trailer" : $("#game_trailer").val(),
             "platforms" : platforms
           }
}

function SetUpEditGameValidation() {
    $("#game_release_date").keyup(function() {
        DateValidate($(this), dateRegex)
    });

    $("#game_trailer").keyup(function() {
        Validate($(this), urlRegex);
    });
}

function ValidateEditGameControls() {
    var returnValue = true;
    
    if (!DateValidate($("#game_release_date"), dateRegex))
    {
        returnValue = false;
    }
    if (!Validate($("#game_trailer"), urlRegex))
    {
        returnValue = false;
    }

    return returnValue;
}

function ReadSaveGameReponse(response) {
    alert(response);
}


// End Edit Game section //
