import random

class Food:
    def __init__(self):
        self.color=(250,0,0)
        self.x=random.randint(0, 380)
        self.y=random.randint(0, 380)
        self.size=10
        self.status="inactive"
    
    def put_food(self,x_max, y_max):
        #generar una x random 
        self.x=random.randint(0, x_max)
        self.y=random.randint(0, y_max)

        return(self.x, self.y)