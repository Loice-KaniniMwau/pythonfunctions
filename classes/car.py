class Car:
    def __init__(self,make,model, speed,color,reg_no):
        self.make=make
        self.model=model
        self.speed=speed
        self.color=color
        self.reg_no=reg_no
    def car_description(self):
        return(f"{self.color} {self.make} {self.model}")
    def car_acceleration(self,accelerate):
        speed=self.speed+accelerate
        return(speed)
    def car_decceleration(self,decelerate):
        speed=self.speed-decelerate
        return speed
    