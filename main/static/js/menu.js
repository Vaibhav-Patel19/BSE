
function addFunction(dish) {

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

    //This Part - 1
    for (let i = 1; i <= 10; i++) {
        quantityList.innerHTML += `
            <li onclick = "confirmDish('${dname}', '${i}', '${dprice}', '${dcuisine}')">
                ${i}
            </li>
        `
    }
}

function modalClose() {
    var modal = document.getElementById("modal");
    var quantity = document.getElementById("quantity");

    modal.classList.add("remove");
    quantity.classList.add("remove");
}

function confirmDish(dname, dqty, dprice, dcuisine) {

    var quantity = document.getElementById("quantity");
    quantity.classList.add("remove");

    var dishName2 = document.getElementById("dishName2");
    dishName2.innerHTML = dname;

    var quantity1 = document.getElementById("quantity1");
    quantity1.innerHTML = "Quantity Choosen : " + dqty;

    var submitDish = document.getElementById("submitDish");

    submitDish.innerHTML = `
    <button id="submitDish" onclick="yesConfirm('${dname}', '${dqty}', '${dprice}', '${dcuisine}')"> 
        Yes 
    </button>

    <button onclick="noConfirm()">
        No 
    </button>`


    var confirm = document.getElementById("confirm");
    confirm.classList.remove("remove");

}

function noConfirm() {

    var quantity = document.getElementById("quantity");
    quantity.classList.remove("remove");


    var confirm = document.getElementById("confirm");
    confirm.classList.add("remove");

}

// function yesConfirm(dname, dqty, dprice, dcuisine) {

//     $.ajax({
//         type: "POST",
//         url: "{% url 'showMenu' 'asd' %}".replace('asd', dcuisine),
//         data: {
//             csrfmiddlewaretoken: "{{ csrf_token }}",   // < here 
//             state: "inactive",
//             dname: dname,
//             dqty: parseInt(dqty, 10),
//             dprice: parseInt(dprice, 10),
//         },
//         success: function () {
//             window.location.href = '/home/1/'
//         }
//     });

// }