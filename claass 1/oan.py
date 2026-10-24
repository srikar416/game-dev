import pygame
pygame.init()
WIDTH=1000
HEIGHT=600
rectx=700
recty=500
rect2_x= 500
rect2_y=300
rect3_x= 800
rect3_y= 300
rectw=100
recth=50
vel_x=5
vel_y=5
vel_x2=5
vel_y2=5
FPS=60
clock=pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
running=True
background= pygame.image.load(r"C:\Users\ratis\OneDrive\Documents\Image20260808162511.png")
scaledBg=pygame.transform.scale(background,(WIDTH,HEIGHT))
colorList=["RED", "BLUE", "GREEN", "YELLOW", "PINK"]
batRect= pygame.Rect(rectx,recty, 100,30)
ballRect= pygame.Rect(rect2_x, rect2_y, 30, 30)
ballRect2= pygame.Rect(rect3_x, rect3_y, 30, 30)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
  
    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and batRect.x > 0:
        batRect.x -=20
    if keys[pygame.K_RIGHT] and batRect.x < WIDTH-100:
        batRect.x += 20
    if batRect.colliderect(ballRect):
        vel_y= -vel_y
    ballRect.y +=vel_y
    ballRect.x +=vel_x
    if ballRect.y > HEIGHT-30 or ballRect.y <0:
        vel_y= -vel_y
    if ballRect.x > WIDTH-30 or ballRect.x < 0:
        vel_x= -vel_x
    if batRect.colliderect(ballRect2):
        vel_y2=-vel_y2
    ballRect2.y += vel_y2
    ballRect2.x += vel_x2
    if ballRect2.y > HEIGHT-30 or ballRect2.y < 0:
        vel_y2= -vel_y2
    if ballRect2.x > WIDTH-30 or ballRect2.x < 0:
        vel_x2= -vel_x2
    #Create another velocity x and y for homework for ballRect2
    
    screen.blit(scaledBg, (0,0))
    pygame.draw.rect(screen, "red", batRect)
    pygame.draw.rect(screen, "yellow", ballRect)
    pygame.draw.rect(screen, "yellow", ballRect2)
    pygame.display.update()

