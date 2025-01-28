function update_cost(){
    
    let output1 = document.getElementById('hotel_output')
    let adults = document.getElementById('id_booking_adults').value
    let children = document.getElementById('id_booking_children').value
    let oaps = document.getElementById('id_booking_oap').value
    let short = document.getElementById('short_path')
    let medium = document.getElementById('medium_path')
    let long = document.getElementById('long_path')
    let unchecked = 1 

    console.log(unchecked)
    
    routevalue = 0
    if (short.checked) {
        routevalue += 20
        document.getElementById("medium_path").disabled = true;
        document.getElementById("long_path").disabled = true;
        unchecked = 0

    } 
    
    else if (medium.checked) {
        routevalue += 35
        document.getElementById("short_path").disabled = true;
        document.getElementById("long_path").disabled = true;
        unchecked = 0
    }

    else if (long.checked) {
        routevalue += 50
        document.getElementById("short_path").disabled = true;
        document.getElementById("medium_path").disabled = true;
        unchecked = 0
    }
    else {
        document.getElementById("short_path").disabled = false;
        document.getElementById("medium_path").disabled = false; 
        document.getElementById("long_path").disabled = false; 
        unchecked = 1
        
    }
    
    if (adults > 0 && unchecked == 0){
        document.getElementById("booking_button").disabled = false;
    } 
    else{
        document.getElementById("booking_button").disabled = true; 
    }
    let price = (adults * 20) + (children * 13) + (oaps * 17) + routevalue
}


    output1.innerHTML = "Booking cost : £" + price
    



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

console.log("hello")