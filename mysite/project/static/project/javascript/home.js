// home.js
// javascript files for managing homt component.

redditText = document.getElementById("link");
articleText = document.getElementById("textarea1");
redditLabel = document.getElementById("redditLabel");
articleLabel = document.getElementById("articleLabel");
redditForm = document.getElementById("redditForm");
articleForm = document.getElementById("articleForm");

activeForm = null;

btnSubmit = document.getElementById("submit");

articleText.addEventListener("focus", function(){
  articleLabel.style.visibility="hidden";
  activeForm = articleForm;
});

articleText.addEventListener("blur", function(){
  articleText.value = "";
  articleLabel.style.visibility="visible";
});

articleText.addEventListener("keypress", function(e){
  console.log("KEY");
  console.log($('#textarea1'))
});

redditText.addEventListener("keypress", function(e){
  if (e.keyCode === 13) {
    e.preventDefault();
  }
});

redditText.addEventListener("focus", function(){
  redditLabel.style.visibility="hidden";
  console.log(redditForm);
  activeForm = redditForm;
});

redditText.addEventListener("blur", function(){
  redditText.value = "";
  redditLabel.style.visibility="visible";
});

btnSubmit.addEventListener("click", function(){
  console.log(activeForm);
  if(activeForm !== null){
    activeForm.submit();  
  }
});
