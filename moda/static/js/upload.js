/**
 * Created by haliun on 07.12.2015.
 */
/**
 * ���������� ����������, � ������� ����� ����� ������� ������ ������� ������ �� ����.
 * @field
 */

var DialogUploadClothes=null;
/***********************************************************************************************************************
 *                               "�����������" ������� ������� ������ �� ����.
 * @class DialogUploadClothes
 *
 **********************************************************************************************************************/
function UploadClothes() {
    // ����������� JQuery UI Dialog.
    this.el = $("#DialogUploadClothes");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        modal:true,
        width:400,
        buttons : [
            {
                text : "Upload",
                icons : {
                 primary : "ui-icon-check"
                },
                click: function() {
                    console.log( caller );
                    caller.upload_clothes();
                }

            }, {
                text : "Cancel",
                icons : {
                 primary : "ui-icon-circle-close"
                },
                click : function() {
                    // ��� ������� �� ������ "������" - ������ �� ����������, ������
                    // �������� ������ � ���.
                    $( this ).dialog( "close" );
                }
            }
        ]
    });
    this.dialog_clothes={
        el: $("#DialogUploadClothes"),
        clothes_name: $("#clothes_name"),
        clothes_type:$("#clothes_type"),
        clothes_size:$("#clothes_size"),
        clothes_gender:$("#clothes_gender"),
        clothes_material:$("#clothes_material"),
        clothes_color:$("#clothes_color"),
        clothes_brand:$("#clothes_brand"),
        clothes_season:$("#clothes_season"),
        clothes_situation:$("#clothes_situation"),
        clothes_price:$("#clothes_price"),
        clothes_description:$("#clothes_description"),
        clothes_image:$("#clothes_image")


    };
}
/***********************************************************************************************************************

 **********************************************************************************************************************/


UploadClothes.prototype.show = function () {

    this.el.dialog("open");

};


/***********************************************************************************************************************
 *
 * @memberOf DialogUploadClothes
 */

UploadClothes.prototype.upload_clothes = function() {
    var caller = this;
    var dlg = this.dialog_clothes;
    $.ajax({ // create an AJAX call...
        data: {
            csrfmiddlewaretoken:'{{csrf_token}}',
            clothes_name: dlg.clothes_name.val(),
            clothes_type: dlg.clothes_type.val(),
            clothes_size: dlg.clothes_size.val(),
            clothes_gender: dlg.clothes_gender.val(),
            clothes_material: dlg.clothes_material.val(),
            clothes_color: dlg.clothes_color.val(),
            clothes_brand: dlg.clothes_brand.val(),
            clothes_season: dlg.clothes_season.val(),
            clothes_situation: dlg.clothes_situation.val(),
            clothes_price: dlg.clothes_price.val(),
            clothes_description: dlg.clothes_description.val(),
            clothes_image: dlg.clothes_image.val()
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