
addFunction = (dish) => {

    // Quantity selection box will become active
    var modal = document.getElementById("modal");
    modal.classList.remove("remove");

    // quantity List
    var quantity = document.getElementById("quantity");
    quantity.classList.remove("remove");

    // Set the Cuisine Name 
    var dishType = document.getElementById("dishType");
    dishType.innerHTML = dish.dataset.type;

    // Set the Dish Name 
    var dishName = document.getElementById("dishName");    
    dishName.innerHTML = dish.dataset.name;

    dname = dish.dataset.name;
    dtype = dish.dataset.type;
    dprice = dish.dataset.price;
    dcuisine = dish.dataset.cuisine;

    var quantityList = document.getElementById("quantityList");
    quantityList.innerHTML = "";

    //This Part - 1
    for (let i = 1; i <= 10; i++) {
        quantityList.innerHTML += `
            <li name="dqty" onclick = "confirmDish('${dname}', '${i}', '${dprice}', '${dcuisine}')">
                ${i}
            </li>
        `
    }
}

function modalClose() {
    var modal = document.getElementById("modal");
    modal.classList.add("remove");

    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");
}

confirmDish = (dname, dqty, dprice, dcuisine) => {

    // Remove qunatity list
    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");

    // Set dish name in confirm box
    var dishName2 = document.getElementById("dishName2");
    dishName2.innerHTML = dname;

    // Set chosen quautity for confirmation
    var quantity1 = document.getElementById("quantity1");
    quantity1.innerHTML = "Quantity Choosen : " + dqty;

    var submitDish = document.getElementById("submitDish");

    //  Yes No confirms Box Appears
    var confirm = document.getElementById("confirm");
    confirm.classList.remove("remove");

    // JSON Object
    submitDish.innerHTML = `
    <button id="submitDish" onclick="yesConfirm('${dname}', '${dqty}', '${dprice}', '${dcuisine}')"> 
        Yes 
    </button>

    <button onclick="noConfirm()">
        No 
    </button>`
}

noConfirm = () => {

    // Qunatity List Appears
    var quantity = document.getElementById("quantity");
    quantity.classList.remove("remove");

    // Yes No confirms Box Disappers
    var confirm = document.getElementById("confirm");
    confirm.classList.add("remove");
}

function yesConfirm(dname, dqty, dprice, dcuisine){

    // shorthand Ajax function
    
    $.ajax({
        type: "POST",
        url: "{% url 'showMenu' 'asd' %}".replace('asd', dcuisine),
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            state: "inactive",
            dname: dname,
            dqty: parseInt(dqty, 10),
            dprice: parseInt(dprice, 10),
        }, 
        success: function () {
            window.location.href = '/explore/'
        }, 
        dataType: "json"
    });

    // console.log(dname);
}