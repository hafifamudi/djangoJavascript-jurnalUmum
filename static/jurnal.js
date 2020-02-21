$(function(){

    var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-jurnal").modal("show");
      },
      success: function (data) {
        $("#modal-jurnal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#jurnal-table tbody").html(data.html_daftar_jurnal);
          $("#modal-jurnal").modal("hide");
        }
        else {
          $("#modal-jurnal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };
  
  // //handler for Jurnal Transaksi I
  var linkDetail = function(){
    var btn2 = $(this).attr("href");
    location.href = btn2
    console.log(btn2)
  }

  var linkDetail2 = function(){
    var btn = $(this).attr("href");
    location.href = btn;
  }
    
  //handler for Jurnal Transaksi II
 
 
 
  //Jurnal Javascript Code I
  $(".jurnalDaftar").click(linkDetail)
  //Jurnal Javascript Code II
  $(".js-buat-jurnalTransaksi").click(linkDetail2)
  $(".indexTransaksi").click(linkDetail2)
  $(".js-update-jurnal").click(linkDetail2)
  $(document).on("click",".js-delete-jurnal2",function(){
    var btn = $(this).attr("href");
    bootbox.confirm("Apakah anda Yakin untuk menghapus data Jurnal Transaksi ini ?",function(result){
      if(result){
        location.href = btn;
      }
    })
  })

 
  // Create Jurnal
  $(".js-buat-jurnal").click(loadForm);
  $("#modal-jurnal").on("submit", ".js-jurnal-buat-form", saveForm);

  // Update Jurnal
  $("#jurnal-table").on("click",".js-update-jurnal2",loadForm);
  $("#modal-jurnal").on("submit", ".js-jurnal-update-form", saveForm);
  
  //Delete Jurnal
  $("#jurnal-table").on("click",".js-delete-jurnal",loadForm);
  $("#modal-jurnal").on("submit", ".js-jurnal-delete-form", saveForm);

})

