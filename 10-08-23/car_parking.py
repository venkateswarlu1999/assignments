class ParkingLot:
    """It's contain local variable are number of floors and each floor capacity and also available spots in 
        each spot and how many types of  spots"""

    def __init__(self):
        self.floors = 3
        self.capacity_per_floor = 30
        self.available_spots ={
            'Compact':[[self.capacity_per_floor, []] for _ in range(self.floors)],
            'Large':[[self.capacity_per_floor, []] for _ in range(self.floors)],
            'Small':[[self.capacity_per_floor, []] for _ in range(self.floors)],
            'Electrical':[[self.capacity_per_floor, []] for _ in range(self.floors)],
        }
        
    def book_spot(self, user_name, vehicle_type):
        """this function about spot booking based on our vaichle and it's type.here it take vaiche and mapp the 
            it required type"""
        vehicle_mapping = {
            'car':'Compact',
            'van':'Large',
            'lory':'Large',
            'motorcycle':'Small',
            'electrical':'Electrical'
        }
        # here it take vaiche and give the vaichle type based on above dict mapping
        vehicle_type = vehicle_mapping.get(vehicle_type.lower())
        
        if not vehicle_type:
            # here user given vechicle not satisfy the above mapping it return a msg
            return "Invalid vehicle type"
        
        for floor in range(self.floors):
            """here above loop itarate the each floor in all floors and give me the how many spots are available
              or not.if no available spots then return the below msg"""
            if self.available_spots[vehicle_type][floor][0] > 0:
                 # in above it check either spots availeble or not base on vaichle type
                spot_number = self.capacity_per_floor - self.available_spots[vehicle_type][floor][0] +1
                self.available_spots[vehicle_type][floor][0] -= 1
                self.available_spots[vehicle_type][floor][1].append(spot_number)
                return f"Spot booked for {user_name}. Floor: {floor+1}, Spot Number: {spot_number}"
        return "No parking spots are available for the selected veichle type."
    
    def check_out(self, user_name, vehicle_type, floor, spot_number):
        """here it take vaichle type and floor and stop number and check first vaichle type is there 
            remove the blocked spots and append the available spots"""
        vehicle_mapping = {
            'car':'Compact',
            'van':'Large',
            'lory':'Large',
            'motorcycle':'Small',
            'electrical':'Electrical'
        }
        # here it convert based on vaichle name to vaichle type
        vehicle_type = vehicle_mapping.get(vehicle_type.lower())
        
        if not vehicle_type:
            # here vaichle type not in type then return below msg
            return "Invalid vehicle type"
        
        if self.available_spots[vehicle_type][floor - 1][0] == self.capacity_per_floor:
            # here it check available spots and capacity of floor is it same then retun below msg
            return "This spot is not allocated or already checked out."
        
        if spot_number in self.available_spots[vehicle_type][floor -1][1]:
             # here it check spot in availble spots or not if it is not in available spots then remove and add available spots
            self.available_spots[vehicle_type][floor - 1][0] += 1
            self.available_spots[vehicle_type][floor - 1][1].remove(spot_number)
            return f"Spot checked out for {user_name}."
        else:
            return "Spot not found."
        
    def display_available_spots(self):
        """this method is used to display the all available spots in the floor. in this it gives available spots 
           first it chek the all type of spots in floor one by one """
        for floor in range(self.floors):
            print(f"Floor {floor + 1} - Compact: {self.available_spots['Compact'][floor][0]}, Large: {self.available_spots['Large'][floor][0]}, Small: {self.available_spots['Large'][floor][0]},Electrical: {self.available_spots['Large'][floor][0]}")

class ParkingFeeCalculator:
    """here it calculate the parking fee based on our required ment and return the total fee"""
    def calculate_fee(self, hours):
        base_fee = 40
        extra_fee_per_hour = 15
        total_fee = base_fee+(hours -1)*extra_fee_per_hour
        return total_fee
    
parking_lot = ParkingLot()
fee_calculator = ParkingFeeCalculator()


while True:
    print("\nWell come to the venky parking lot..")
    print("\nHere maximun time of parking is 6 hours only kindly note it.")
    choice = int(input("1. Book Spot\n2. Check Out\n3. Customer Info\n4. Display Available Spots\n5. Exit\nEnter your choice: "))

    if choice == 1:
        user_name = input("Enter your name: ")
        vehicle_type = input("Enter your vehicle type (car/van/lory/'motorcycle/electrical): ")
        if vehicle_type.lower() not in ['car', 'van','lory', 'motorcycle', 'electrical']:
            print("Invalid vehicle type.")
            continue
        result = parking_lot.book_spot(user_name, vehicle_type)
        print(result)
        hours_parked = int(input("Enter hours parked: "))
        total_fee = fee_calculator.calculate_fee(hours_parked)
        print(f"Total parking fee: {total_fee} rupees")

    elif choice == 2:
        user_name = input("Enter your name: ")
        vehicle_type = input("Enter your vehicle type (car/van/lory/motorcycle/electrical): ")
        floor = int(input("Enter floor number: "))
        spot_number = int(input("Enter spot number: "))
        result = parking_lot.check_out(user_name, vehicle_type, floor, spot_number)
        print(result)

    elif choice == 3:
        user_name = input("Enter your name: ")
        mobile_number = input("Enter your mobile number: ")
        vehicle_type = input("Enter your vehicle type (car/van/lory/motorcycle/electrical): ")
        if vehicle_type.lower() not in ['car', 'van','lory', 'motorcycle', 'electrical']:
            print("Invalid vehicle type.")
            continue
        result = parking_lot.book_spot(user_name, vehicle_type)
        print(result)
        hours_parked = int(input("Enter hours parked: "))
        total_fee = fee_calculator.calculate_fee(hours_parked)
        print(f"Customer Info: Name: {user_name}, Mobile Number: {mobile_number}")
        print(f"Total parking fee: {total_fee} rupees")

    elif choice == 4:
        parking_lot.display_available_spots()

    elif choice == 5:
        break