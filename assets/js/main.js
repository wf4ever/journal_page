$(function() {
  $("#add_author_button").click(function(){
    $("#author_group").clone().appendTo( "#authors_list");
  });
});