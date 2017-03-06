////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//   В этот файл я бы собрал обработку элементов, имеющих отношение к логину, регистрации, чему-то может быть еще.
//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/**
 * Глобальная переменная, в которую будет потом посажен объект диалога захода на сайт.
 * @field
 */

var DialogLogin = null;
var DialogRegister=null;
/***********************************************************************************************************************
 *                               "Конструктор" объекта диалога захода на сайт.
 * @class CDialogLogin
 *
 **********************************************************************************************************************/

function CDialogLogin() {
    // Конструктор JQuery UI Dialog.
    this.el = $("#DialogLogin");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        modal: true,
        closeOnEscape: true,
        okOnEnter:true,
        buttons : [
            {
                text : "Login",
                width: 100,
                icons : {
                 primary : "ui-icon-check"
                },
                click: function() {
                    console.log( caller );
                    caller.really_login();
                }

            }, {
                text : "Cancel",
                width: 100,
                icons : {
                 primary : "ui-icon-circle-close"
                },
                click : function() {
                    // При нажатии на кнопку "Отмена" - ничего не происходит, просто
                    // скрываем диалог и все.
                    $( this ).dialog( "close" );
                }
            }
        ]
    });
}
function Register() {
    // Конструктор JQuery UI Dialog.
    this.el = $("#DialogRegister");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        modal: true,
        closeOnEscape: true,
        buttons : [
            {
                text : "Register",
                width: 100,
                icons : {
                 primary : "ui-icon-check"
                },
                click: function() {
                    console.log( caller );
                    caller.really_register();
                }

            }, {
                text : "Cancel",
                width: 100,
                icons : {
                 primary : "ui-icon-circle-close"
                },
                click : function() {
                    // При нажатии на кнопку "Отмена" - ничего не происходит, просто
                    // скрываем диалог и все.
                    $( this ).dialog( "close" );
                }
            }
        ]
    });
}
/***********************************************************************************************************************
 * Появление диалога авторизации на экране.
 * @memberOf CDialogLogin
 **********************************************************************************************************************/

CDialogLogin.prototype.show = function () {
    // Появление диалога на экране.
    this.el.dialog("open");
    // @todo "Затемнение" основного тела страницы.
};

Register.prototype.show = function () {
    // Появление диалога на экране.
    $("#DialogLogin").hide();
    this.el.dialog("open");
    // @todo "Затемнение" основного тела страницы.
};


/***********************************************************************************************************************
 * Запрос на авторизацию.
 * @memberOf CDialogLogin
 */


CDialogLogin.prototype.really_login = function() {
    var caller = this;
        $.ajax({ // create an AJAX call...
                data: {
                    username : $("#username").val(),
                    password : $("#password").val()
                    // $(this).serialize()
                }, // get the form data
                type: "POST", // $(this).attr('method'), // GET or POST
                dataType : "json",
                url: "/ajax_login/", // $(this).attr('action'), // the file to call
                success: function(data) { // on success..
                   // window.location = response;
                    // alert("success");
                    console.log( data );
                    if ( data.result === "true" ) {
                        caller.el.dialog( "close" );
                        document.location = "/";
                    } else {
                        console.log( data );
                        caller.el.dialog({ title : data.description });
                        // @todo Сделать красным фон шапки диалога
                    }

                },
                error : function(request, status, thError ) {
                    global_error( request, status, thError );
                    console.log("on error");
                    console.log( request );
                    console.log( status );
                    console.log( thError );
                }
            });


};
Register.prototype.really_register = function() {
    var caller = this;
        $.ajax({ // create an AJAX call...
                data: $('form#Register').serialize(), // get the form data
                type: "POST", // $(this).attr('method'), // GET or POST
                dataType : "json",

                url: "/register/", // $(this).attr('action'), // the file to call
                success: function(data) { // on success..
                   // window.location = response;
                    // alert("success");

                    console.log( data );
                    if ( data.result === "true" ) {
                        caller.el.dialog( "close" );
                        document.location = "/";
                    } else {
                        console.log( data );
                        caller.el.dialog({ title : data.description });
                        // @todo Сделать красным фон шапки диалога
                    }

                },
                error : function(request, status, thError ) {
                    global_error( request, status, thError );
                    console.log("on error");
                    console.log( request );
                    console.log( status );
                    console.log( thError );
                }
            });


};