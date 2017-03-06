////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//   В этот файл я бы собрал обработку элементов, имеющих отношение к логину, регистрации, чему-то может быть еще.
//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/**
 * Глобальная переменная, в которую будет потом посажен объект диалога захода на сайт.
 * @field
 */

var Dialogadd = null;

function Addsthing() {
    // Конструктор JQuery UI Dialog.
    this.el = $("#Dialogadd");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        width:400,
        modal: true,
        closeOnEscape: true,
        okOnEnter:true,
        buttons : [
            {
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

Addsthing.prototype.show = function () {
    // Появление диалога на экране.
    this.el.dialog("open");
    // @todo "Затемнение" основного тела страницы.
};

Addsthing.prototype.add = function() {
    var caller = this;
        $.ajax({ // create an AJAX call...
                data: {

                    // $(this).serialize()
                }, // get the form data
                type: "POST", // $(this).attr('method'), // GET or POST
                dataType : "json",
                url: "/", // $(this).attr('action'), // the file to call
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
