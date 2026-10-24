import pygame
pygame.init()
WIDTH=1000
HEIGHT=600
rectx=700
recty=400
rectw=100
recth=50
FPS=60
clock=pygame.time.Clock()
screen=pygame.dsiplay.set_mode((WIDTH,HEIGHT))
running=True
background= pygame.image.load(r"C:\Users\ratis\OneDrive\Documents\Image20260808162511.png")
scaledBg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
colorList=["RED", "BLUE", "GREEN", "YELLOW", "PINK"]
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
        
            if event.type==pygame.K_RIGHT:
            rectx += 20
            if event.type==pygame.K_LEFT:
            rectx -=20
    