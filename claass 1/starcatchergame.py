import pygame 
import random
import time
pygame.init()
HEIGHT=600
WIDTH=1000
FPS=60
running=True
screen= pygame.display.set_mode((WIDTH,HEIGHT))
background=pygame.image.load(r"C:\Users\ratis\OneDrive\Desktop\Gamby Labs, LLC\Roe Invoices\Invoices Oct 6th\360_F_59958917_1SvEPqvKnrGr68THJ35hqQUiHwQ6WhCN.jpg")
scaledBg=pygame.transform.scale(background, (WIDTH, HEIGHT))
clock= pygame.time.Clock()
font= pygame.font.Font(None, 25)
class basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(r"C:\Users\ratis\Downloads\k100_ms13_p-removebg-preview.png")
        self.image=pygame.transform.scale(self.image,(200,200))
        self.rect=self.image.get_rect(center=(600, HEIGHT-55))
        self.basketspeed=8
    def moveLeft(self,leftKeyPressed):
          self.keys=pygame.key.get_pressed()
          if leftKeyPressed and self.rect.x>0:
               self.rect.x-=self.basketspeed
    def moveRight(self,rightKeyPressed):
          self.keys=pygame.key.get_pressed()
          if rightKeyPressed and  self.rect.x<WIDTH-100:
                self.rect.x+=self.basketspeed
    def update(self):
          self.keys=pygame.key.get_pressed()
          self.moveLeft(self.keys[pygame.K_LEFT])
          self.moveRight(self.keys[pygame.K_RIGHT])
class star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load(r"C:\Users\ratis\Downloads\images-removebg-preview.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect(center=(random.randint(0,WIDTH),30))
        self.velx= random.randint(3,10)
        self.vely=random.randint(3,10)
    def starfalling(self):
          self.rect.y += self.vely

    def update(self):
          self.starfalling()
basket = basket()
stars = []
starGroup= pygame.sprite.Group()
for i in range(10):
    starGroup.add(star())

basketGroup = pygame.sprite.Group()
basketGroup.add(basket)
count=0
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(scaledBg, (0,0))
    basketGroup.draw(screen)
    starGroup.draw(screen)
    starGroup.update()
    basketGroup.update()
    collidedstars=pygame.sprite.spritecollide(basket,starGroup,False,pygame.sprite.collide_mask)
    for Star in collidedstars:
         if Star.vely>0:
            Star.vely=Star.vely
    count=+1
    if count>=10:
        for i in range(10):
            starGroup.add(star())    
        count=0
               
    pygame.display.update()

