
function modal(dish) {

    var modal = document.getElementById("modal");
    var quantity = document.getElementById("quantity");
    var quantityList = document.getElementById("quantityList");
    var dishType = document.getElementById("dishType");
    var dishName = document.getElementById("dishName");

    dishType.innerHTML = dish.dataset.type;
    dishName.innerHTML = dish.dataset.name;

    dname = dish.dataset.name;
    dtype = dish.dataset.type;
    dprice = dish.dataset.price;
    dcuisine = dish.dataset.cuisine;

    modal.classList.remove("remove");
    quantity.classList.remove("remove");

    quantityList.innerHTML = "";

    for (let i = 1; i <= 10; i++) {
        quantityList.innerHTML += `
            <li onclick = "confirmDish('${dname}', '${i}', '${dprice}', '${dcuisine}')">${i}</li>
        `
    }
}

function confirmDish(dname, dqty, dprice, dcuisine) {

    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");

    var dishName1 = document.getElementById("dishName1");
    var quantity1 = document.getElementById("quantity1");
    var submitDish = document.getElementById("submitDish");

    submitDish.innerHTML = `
    <button id="submitDish" 
    onclick="yesConfirm('${dname}', '${dqty}', '${dprice}', '${dcuisine}')"> 
    Yes </button>
    <button onclick="noConfirm()"> No </button>`

    dishName1.innerHTML = dname;
    quantity1.innerHTML = "Quantity Choosen : " + dqty;


    var confirm = document.getElementById("confirm");
    confirm.classList.remove("remove");

}