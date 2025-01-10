function update_cost(){
    //document.getElementById("booking_button").disabled = true;
    let output1 = document.getElementById('hotel_output')
    let adults = document.getElementById('id_booking_adults').value
    let children = document.getElementById('id_booking_children').value
    let oaps = document.getElementById('id_booking_oap').value
    let short = document.getElementById('short_path')
    let medium = document.getElementById('medium_path')
    let long = document.getElementById('long_path')

    routevalue = 0
    if (short.checked) {
        routevalue += 20
        document.getElementById("medium_path").disabled = true;
        document.getElementById("long_path").disabled = true;
    } 
    
    else if (medium.checked) {
        routevalue += 35
        document.getElementById("short_path").disabled = true;
        document.getElementById("long_path").disabled = true;
    }

    else if (long.checked) {
        routevalue += 50
        document.getElementById("short_path").disabled = true;
        document.getElementById("medium_path").disabled = true;
    }
    else {
        document.getElementById("short_path").disabled = false;
        document.getElementById("medium_path").disabled = false; 
        document.getElementById("long_path").disabled = false;
    }
    let price = (adults * 20) + (children * 13) + (oaps * 17) + routevalue

    output1.innerHTML = "Booking cost : £" + price
    
}

let adults = document.getElementById('id_booking_adults')
let children = document.getElementById('id_booking_children')
let oaps = document.getElementById('id_booking_oap')
let short = document.getElementById('short_path')
let medium = document.getElementById('medium_path')
let long = document.getElementById('long_path')


adults.addEventListener("change", update_cost)
children.addEventListener("change", update_cost)
oaps.addEventListener("change", update_cost)
short.addEventListener("change", update_cost)
medium.addEventListener("change", update_cost)
long.addEventListener("change", update_cost)
