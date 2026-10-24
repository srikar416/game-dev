import pygame
import random
pygame.init()
HEIGHT=600
WIDTH= 1000
FPS= 60
running=True
screen= pygame.display.set_mode((WIDTH,HEIGHT))
background= pygame.image.load(r"C:\Users\ratis\OneDrive\Documents\Image20260808162511.png")
scaledbg= pygame.transform.scale(background, (WIDTH, HEIGHT))
clock=pygame.time.Clock()
font= pygame.font.Font(None,25)
score=0
lives=5

class Bat(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image=pygame.image.load(r"C:\Users\ratis\OneDrive\Desktop\Gamby Labs, LLC\Roe Invoices\a-wooden-baseball-bat-is-displayed-horizontally-on-transparent-background-in-this-image-png.webp")
          self.image=pygame.transform.scale(self.image,(200,200))
          self.rect= self.image.get_rect(center=(600, HEIGHT-10))
          self.mask=pygame.mask.from_surface(self.image)
          self.batspeed= 20
         
     def moveLeft(self,leftKeyPressed):
          self.keys=pygame.key.get_pressed()
          if leftKeyPressed and self.rect.x>0:
               self.rect.x-=self.batspeed
     def moveRight(self,rightKeyPressed):
          self.keys=pygame.key.get_pressed()
          if rightKeyPressed and  self.rect.x<WIDTH-100:
                self.rect.x+=self.batspeed
     def update(self):
          self.keys=pygame.key.get_pressed()

          """if self.keys[pygame.K_LEFT]==True and self.rect.x>0:
               self.rect.x-=self.batspeed
          if self.keys[pygame.K_RIGHT]==True and self.rect.x<WIDTH-100:
               self.rect.x+=self.batspeed
               """
          self.moveLeft(self.keys[pygame.K_LEFT])
          self.moveRight(self.keys[pygame.K_RIGHT])
        

class Ball(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image=pygame.image.load(r"C:\Users\ratis\Downloads\OIP-removebg-preview.png")
          self.image=pygame.transform.scale(self.image,(50,50))
          self.rect=self.image.get_rect(center=(random.randint(0,WIDTH),30))
          self.velx= random.randint(3,10)
          self.vely=random.randint(3,10)
     def ballfalling(self):
          global lives
          global running
          self.rect.x += self.velx
          self.rect.y += self.vely
          if self.rect.x<=0 or self.rect.x>=WIDTH-50:
               self.velx=-self.velx
          if self.rect.y<=0 or self.rect.y>=HEIGHT-50:
               self.vely=-self.vely
          if self.rect.bottom>= HEIGHT:
               lives-=1
          if lives==0:
               running=False
     def update(self):
          self.ballfalling()
               
bat = Bat()
balls = []
ballGroup= pygame.sprite.Group()
for i in range(10):
    ball=Ball()
    ballGroup.add(ball)

batGroup = pygame.sprite.Group()
batGroup.add(bat)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.blit(scaledbg,(0,0))
    renderedScoretext=font.render(f"Score: {score}", False, "RED", "Black") 
    renderedLivestext=font.render(f"Lives: {lives}", False, "RED", "Black" )  
    screen.blit(renderedScoretext, (10,10))
    screen.blit(renderedLivestext, (10,30))
    batGroup.draw(screen)
    ballGroup.draw(screen)
    ballGroup.update()
    batGroup.update()
    collidedBalls=pygame.sprite.spritecollide(bat,ballGroup,False,pygame.sprite.collide_mask)
    for ball in collidedBalls:
         if ball.vely>0:
               ball.vely=-ball.vely
               score +=1
    pygame.display.update()
               

    
        