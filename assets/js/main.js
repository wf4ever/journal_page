$(function() {
  var new_author_div = $("#author_group").clone();
  $("#add_author_button").click(function(){
    new_author_div.appendTo( "#authors_list");
    new_author_div = new_author_div.clone();
  });
});