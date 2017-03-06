/**
 * Created by haliun on 27.03.2016.
 */

var Dialogadd=null;
/***********************************************************************************************************************
 *                               "�����������" ������� ������� ������ �� ����.
 * @class Dialogadd
 *
 **********************************************************************************************************************/
function AddSomething() {
    // ����������� JQuery UI Dialog.
    this.el = $("#Dialogadd");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        modal:true,
        width:400,
        buttons : [
            {
                text : "Cancel",
                icons : {
                 primary : "ui-icon-circle-close"
                },
                click : function() {

                    $( this ).dialog( "close" );
                }
            }
        ]
    });

}
/***********************************************************************************************************************

 **********************************************************************************************************************/


AddSomething.prototype.show = function () {

    this.el.dialog("open");

};


/***********************************************************************************************************************
 *
 * @memberOf Dialogadd
 */

AddSomething.prototype.addsomething = function() {
    var caller = this;
    var dlg = this.dialog_clothes;
    $.ajax({ // create an AJAX call...
        data: {

        }, // get the form data
        type: "GET", // $(this).attr('method'), // GET or POST
        dataType : "json",
        async:true,
        url: "/uploadclothes/", // $(this).attr('action'), // the file to call
        success: function(data) { // on success..
            console.log(data);
            if ( data.result === "true" ) {
                caller.el.dialog( "close" );
                document.location = "/";
            } else {
                console.log( data );
                document.location = "/";
                var alertstr="Your clothes was successfully uploaded!";
                alert(alertstr);
                caller.el.dialog({ title : data.description });

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
