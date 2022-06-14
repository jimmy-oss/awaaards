// Category Review Save
$("#addForm").submit(function(e){
   $.ajax({
           data:$(this).serialize(),
           method:$(this).attr('action'),
           dataType:'Json',
           success:function(res){
             if(res.bool==true){
                $(".ajaxRes").html('Data has been added');
             }
           }
   });
   e.preventDefault();
});
// end