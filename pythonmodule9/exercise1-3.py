class Car:
    def __init__(self,registration_number:str,maximum_speed:int,travelled_distance=0,current_speed=0):
        self.travelled_distance=travelled_distance
        self.registration_number=registration_number
        self.current_speed=current_speed
        self.maximum_speed=maximum_speed
    def accelerate(self,acce):
        self.acce=acce
    def change_speed(self,change):
        self.current_speed+=change
        if self.current_speed>self.maximum_speed:
            self.current_speed=self.maximum_speed
    def brake(self,brake):
        self.current_speed+=brake
        if self.current_speed<self.maximum_speed:
            self.current_speed=0
    def time_drive(self,time):
        self.travelled_distance+=self.current_speed*time
car1=Car("ABC-123",142)
print("Car's registration number:",car1.registration_number)
print("Car's maximum speed:",car1.maximum_speed)
print("Car's current speed:",car1.current_speed)
print("Car's travelled distance:",car1.travelled_distance)
car1.change_speed(30)
car1.change_speed(50)
car1.change_speed(70)
print("Car's current speed after acceleration:",car1.current_speed)
car1.time_drive(30)
car1.time_drive(20)
print(f"Final distance the {car1.registration_number} had travelled: {car1.travelled_distance}km.")
car1.brake(-200)
print("Car's current speed after break:",car1.current_speed)