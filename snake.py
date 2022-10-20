class Snake:
    def __init__(self):
        self.color=(0,255,0)
        self.direction="RIGHT"


        self.body=[(202,202),(201,201),(200,200)]


    def updateCoordinates(self,x,y):
        if self.direction=="UP":
            y-=1
        if self.direction=="DOWN":
            y+=1
        if self.direction=="RIGHT":
            x+=1
        if self.direction=="LEFT":
            x-=1
        
        return (x,y)


    def eat (self):
        for i in range (10):
            (x,y)=self.body[0]
            x,y = self.updateCoordinates(x,y)
            self.body.insert(0,(x,y))


    def move (self):
        #vamos a ponerle la cabeza a la snake
        (x,y)=self.body[0]
        x,y = self.updateCoordinates(x,y)
        self.body.insert(0,(x,y))
    

        #remove the tail
        self.body.pop()