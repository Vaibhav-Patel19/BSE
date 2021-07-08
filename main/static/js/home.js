
changePannel = (liElement, pannel) => {
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

exploreSwitch = (clickedTab, type) => {
    var exploreTabs = document.getElementsByClassName("exploreTab");

    for(let i = 0; i < exploreTabs.length; i++){
        exploreTabs[i].classList.remove("active");
    }

    clickedTab.classList.add("active");

    var c = document.getElementsByClassName("cusines");

    for(let i = 0; i < c.length; i++){
        c[i].classList.remove("active");
    }
    var t = document.getElementById(type);
    t.classList.add("active");

}







