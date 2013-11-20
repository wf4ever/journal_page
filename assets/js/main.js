$(function() {
  //authors url
  var new_author_div = $("#author_group").clone();
  $("#add_author_button").click(function(){
    new_author_div.appendTo( "#authors_list");
    new_author_div = new_author_div.clone();
  });
  //
  $(":file").filestyle();
  $(".bootstrap-filestyle").children().first().css("height","30px");
  $(".bootstrap-filestyle").children().first().css("width","40%");
  $($(".bootstrap-filestyle").children().get(1)).addClass("btn-primary");
  $($(".bootstrap-filestyle").children().get(1)).css("width","100px")
  $($(".bootstrap-filestyle").children().get(1)).css("margin-top","-9px")
  $(".icon-folder-open").each(function(){
  	$(this).remove();
  });
});