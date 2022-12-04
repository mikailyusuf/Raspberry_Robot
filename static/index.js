$(document).ready(function(){
    $("#forward").click(function(){
        // console.log("Testing 123")
        forward()
    });

    $("#backward").click(function(){
        backward()
    });

    $("#left").click(function(){
        left()
    });

    $("#right").click(function(){
        right()
    });

    $("#on").click(function(){
        // console.log("On was clicked again")
        on()
    });

    $("#off").click(function(){
        // console.log("Off was clicked")

        off()
    });
})

function on(){
    $.get( "/on", function( data ) {
      });
}

function off(){
    $.get( "/off", function( data ) {
      });
}

function forward(){
    $.get( "/forward", function( data ) {
    });
}


function backward(){
    $.get( "/backward", function( data ) {
    });
}

function left(){
    $.get( "/left", function( data ) {
    });
}

function right(){
    $.get( "/right", function( data ) {
    });
}