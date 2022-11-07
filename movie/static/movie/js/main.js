function myFunc(){
    var x=document.getElementById("mynav")
    if(x.className === "nav"){
        x.className += " responsive"
    }else(x.className = "nav")
    }


    $('.video').parent().click(function () {
  if($(this).children(".video").get(0).paused){        $(this).children(".video").get(0).play();   $(this).children(".playpause").fadeOut();
    }else{       $(this).children(".video").get(0).pause();
  $(this).children(".playpause").fadeIn();
    }
});