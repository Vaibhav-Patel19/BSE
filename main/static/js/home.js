
function changePannel(liElement, pannel) {
    var liEl = document.getElementsByClassName("liEl");
    for (let i = 0; i < liEl.length; i++) {
        liEl[i].classList.remove("active");
    }

    liElement.classList.add("active");

    var pannel1 = document.getElementsByClassName("pannel");
    var pannel = document.getElementById(pannel);

    for (let i = 0; i < pannel1.length; i++) {
        pannel1[i].style.display = "none";
    }   
    
    pannel.style.display = "block";
    }