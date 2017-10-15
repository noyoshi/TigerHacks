// home.js
// javascript files for managing homt component.

articleButton = document.getElementById("articleIcon");
redditButton = document.getElementById("redditIcon");

articleButton.addEventListener("click", function(){
  window.location.href = window.location.origin + "/article";
});

redditButton.addEventListener("click", function(){
  window.location.href = window.location.origin + "/reddit";
});
