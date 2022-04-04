addFunction = (drink) => {
    var modal = document.getElementById("modal");
    var quantity = document.getElementById("quantity");
    var quantityList = document.getElementById("quantityList");
    var dishType = document.getElementById("dishType");
    var dishName = document.getElementById("dishName");

    dishType.innerHTML = drink.dataset.type
    dishName.innerHTML = drink.dataset.name

    dname = drink.dataset.name
    dtype = drink.dataset.type
    dprice = drink.dataset.price

    modal.classList.remove("remove");
    quantity.classList.remove("remove");

    quantityList.innerHTML = "";

    for (let i = 1; i <= 10; i++) {
        quantityList.innerHTML += `
            <li onclick = "confirmDrink('${dname}', '${i}', '${dprice}', '${dtype}')">
            ${i}
            </li>
        `
    }
}

modalClose = () => {
    var modal = document.getElementById("modal");
    modal.classList.add("remove");

    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");
}

confirmDrink = (dname, dqty, dprice, dtype) => {
    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");

    var dishName2 = document.getElementById("dishName2");
    dishName2.innerHTML = dname;

    var quantity1 = document.getElementById("quantity1");
    quantity1.innerHTML = "Quantity Choosen : " + dqty;

    var submitDish = document.getElementById("submitDish");

    // JSON Object
    submitDish.innerHTML = `
    <button id="submitDish" onclick="yesConfirm('${dname}', '${dqty}', '${dprice}', '${dtype}')"> 
        Yes 
    </button>

    <button onclick="noConfirm()">
        No 
    </button>`

    var confirm = document.getElementById("confirm");
    confirm.classList.remove("remove");

}

noConfirm = () => {

    var quantity = document.getElementById("quantity");
    quantity.classList.remove("remove");


    var confirm = document.getElementById("confirm");
    confirm.classList.add("remove");

}

function yesConfirm(dname, dqty, dprice, dtype) {

    // shorthand Ajax function
    $.ajax({
        type: "POST",
        url: "{% url 'showBarMenu' 'asd' %}".replace('asd', dtype),
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            state: "inactive",
            dname: dname,
            dtype: dtype,
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