import pygame
from snake import Snake
from food import Food
from player import Player 

class Game:
    def __init__(self):
        self.snake=Snake()
        self.food=Food()
        self.player=Player()
        self.ancho=400
        self.largo=400
        self.screen=pygame.display.set_mode((self.ancho,self.largo))
        self.clock=pygame.time.Clock()
        self.fps=60
    
    #Revisar las teclas que se oprimen
    def checkKeys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]: self.fps+=5
        elif keys[pygame.K_a]: self.fps-=5
        elif keys[pygame.K_UP]: self.snake.direction="UP"
        elif keys[pygame.K_DOWN]: self.snake.direction="DOWN"
        elif keys[pygame.K_RIGHT]: self.snake.direction="RIGHT"
        elif keys[pygame.K_LEFT]: self.snake.direction="LEFT"
    
    #Revisar si la serpiente come
    def checkEat(self):
        self.foodRect=pygame.Rect(self.food.x, self.food.y, self.food.size, self.food.size)
        self.snakeHeadRect=pygame.Rect(self.snake.body[0][0], self.snake.body[0][1], 10, 10)
        if pygame.Rect.colliderect(self.foodRect, self.snakeHeadRect):
            self.food.status = "active"
            self.snake.eat()
            self.player.score+=1
    
    #Dibujar el score
    def drawScore(self, screen):
        font=pygame.font.SysFont("arial", 18)
        font2=pygame.font.SysFont("arial", 14)
        text=font.render("Score: "+str(self.player.score), True, (255,255,255))
        text2=font.render("Player: "+str(self.player.name), True, (255,255,255))
        text3=font2.render("Speed: "+str(self.fps)+" FPS", True, (255,255,255))
        screen.blit(text, (2,20))
        screen.blit(text2, (2,0))
        screen.blit(text3, (2,384))

     
    def run (self):
        pygame.init()

        while True:
            #Definir el color de la pantalla
            self.screen.fill((0,0,0))
            
            #Revisar los eventos y mirar si oprimen el boton cerrar
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            #Dibujar la serpiente
            for celda in self.snake.body:
                pygame.draw.rect(self.screen, self.snake.color, (celda[0],celda[1],10,10))
                
            #Dibujar la comida
            pygame.draw.rect(self.screen, self.food.color, (self.food.x,self.food.y,10,10))
            if self.food.status == "active":
                self.food.put_food(380,380)
                self.food.status = "inactive"
                
            #morir si chocas contigo mismo o con los bordes
            if self.snake.body[0] in self.snake.body[1:] or self.snake.body[0][0] > 390 or self.snake.body[0][0] < 0 or self.snake.body[0][1] > 390 or self.snake.body[0][1] < 0:
                return (False)
            
            #Llamar todas las funciones
            self.snake.move()
            self.clock.tick(self.fps)
            self.drawScore(self.screen)
            self.checkKeys()
            self.checkEat()

            #Actualizar la pantalla
            pygame.display.update()
            pygame.display.flip()


mygame=Game()
mygame.run()