addFunction = (dish) => {
    var modal = document.getElementById("modal");
    var quantity = document.getElementById("quantity");
    var quantityList = document.getElementById("quantityList");
    var dishType = document.getElementById("dishType");
    var dishName = document.getElementById("dishName");

    dishType.innerHTML = dish.dataset.type
    dishName.innerHTML = dish.dataset.name

    dname = dish.dataset.name
    dtype = dish.dataset.type
    dprice = dish.dataset.price
    dsavings = dish.dataset.savings

    modal.classList.remove("remove");
    quantity.classList.remove("remove");

    quantityList.innerHTML = "";

    for (let i = 1; i <= 10; i++) {
        quantityList.innerHTML += `
            <li onclick = "confirmDrink('${dname}', '${i}', '${dprice}', '${dsavings}', '${dtype}')">${i}</li>
        `
    }
}

modalClose = () => {
    var modal = document.getElementById("modal");
    modal.classList.add("remove");

    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");
}

confirmDrink = (dname, dqty, dprice, dsavings, dtype) => {
    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");

    var dishName2 = document.getElementById("dishName2");
    dishName2.innerHTML = dname;

    var quantity1 = document.getElementById("quantity1");
    quantity1.innerHTML = "Quantity Choosen : " + dqty;

    var submitDish = document.getElementById("submitDish");

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