function update_cost(){
    document.getElementById("booking_button").disabled = true;
    let output1 = document.getElementById('hotel_output')
    let date = document.getElementById('id_booking_date').value
    let adults = document.getElementById('id_booking_adults').value
    let children = document.getElementById('id_booking_children').value
    let oaps = document.getElementById('id_booking_oap').value

    let price = (adults * 20) + (children * 13) + (oaps * 17)

    output1.innerHTML = "Booking cost : £" + price
    
}
let adults = document.getElementById('id_booking_adults')
let children = document.getElementById('id_booking_children')
let oaps = document.getElementById('id_booking_oap')


adults.addEventListener("change", update_cost)
children.addEventListener("change", update_cost)
oap.addEventListener("change", update_cost)