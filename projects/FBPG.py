def generate_boarding_pass(passenger_name,flight_number,gate_number,seat_class="economy",baggage_allowed="1 piece"):
    print(f" name={passenger_name} \n flight number={flight_number} \n gate number={gate_number} \n seat class={seat_class} \n baggage allowed={baggage_allowed}" )



name=input("enter your full name:")
flight_no=input("enter your flight number:")
gate_no=input("enter your gate number:")
seat_t=input("enter your seat type:")

generate_boarding_pass(name,flight_no,gate_no,seat_t)