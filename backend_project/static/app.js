

function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}


function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}

// function checkCookies() {                                                //Added to darkCheck() to allow both to work correctly
//     let text = ""
//     if (navigator.cookiesEnabled == true) {
//         text = "cookies are enabled";
//     } else {
//         text = "cookies are not enabled";
//     }
//     document.getElementById("cookie").innerHTML = text;
// }

function mOver(obj) {
    obj.innerHTML = "<br> HELLO"
}


function mOut(obj) {
    obj.innerHTML = ""
}


function sendAlert() {
    alert(location.hostname);
}


function darkMode() {
    let element = document.body;
    let state = localStorage.getItem("state");
    element.classList.toggle("dark-mode");

    if (state !=="dark") {
        localStorage.setItem("state", "dark");
    } else {
        localStorage.setItem("state", "light");
    }
}


function darkCheck() {                                                     //function to check is darkmode was toggled on the main page and set to local
    let element = document.body;                                           //storage. checkCookies functionality added to this function as html can only
    let state = localStorage.getItem("state");                             //run one onload event per page.

    if (state == "dark") {
        element.classList.toggle("dark-mode");
    }

    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
    
}