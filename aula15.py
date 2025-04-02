'''import pygame
#criar tela
pygame.init()
pygame.display.flip()

pygame.init()
tela = pygame.display.set_mode((1900,1000))
quadrado = pygame.rect(250,250,50,50)
clock = pygame.time.Clock()

run = False

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            quadrado.move_ip([2,0])
        if event.key == pygame.K_LEFT:
            quadrado.move_ip([2,0])
        if event.key == pygame.K_DOWN:
            quadrado.move_ip([2,0])
        if event.key == pygame.K_UP:
            quadrado.move_ip([2,0])

    tela.fill("white")
    pygame.draw.rect (tela, ('red'), quadrado)
    pygame.display.update ()'''


import pygame

pygame.init()

tela  = pygame.display.set_mode((500,500)) 
quadrado = pygame.Rect(250,250,50,50)
clock = pygame.time.Clock()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
            pygame.quit()

# movimento através de eventos Keydown - pressionar tecla 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                quadrado.move_ip([20,0])
            if event.key == pygame.K_LEFT:
                quadrado.move_ip([-20,0])
            if event.key == pygame.K_DOWN:
                quadrado.move_ip([0,20])
            if event.key == pygame.K_UP:
                quadrado.move_ip([0,-20])
    
    tela.fill('red')
    pygame.draw.rect(tela, ('blue'),quadrado)  
    pygame.display.update()
                          
  

    # pygame.draw.circle(tela,('yellow'), (900,250),200)
    # pygame.draw.ellipse(tela, ('pink'),(750, 650, 540,200 ))
    # pygame.draw.line(tela, ('black'), (400, 800), (200,200),10)
    # pygame.display.flip() 
    # utilize a biblioteca para desenhar:
    # circulo
    # elipse
