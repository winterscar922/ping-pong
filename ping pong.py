import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))

font = pygame.font.Font("freesansbold.ttf", 30)

playerone = 0
playertwo = 0


def playeronescore():
    playeronescore = font.render("score : " + str(playerone), True, (255, 0, 0))
    screen.blit(playeronescore, (0, 0))


def playertwoscore():
    playertwoscore = font.render("score : " + str(playertwo), True, (255, 0, 0))
    screen.blit(playertwoscore, (0, 550))


posx = 0
rectx = 0
parax = 0
paray = 0
# rect1
x = 400
y = 0
# rect2
a = 400
d = 570

ballx = 400
bally = 300


def boundary():
    global x
    global y
    global a
    if x < 0:
        x = 0
    if x > 760:
        x = 760
    if a < 0:
        a = 0
    if a > 760:
        a = 760


while True:
    screen.fill((0, 0, 0))
    circle = pygame.draw.circle(screen, (255, 0, 0), (ballx, bally), 10)
    rect1 = pygame.draw.rect(screen, (0, 0, 255), (x, y, 40, 30))
    rect2 = pygame.draw.rect(screen, (0, 0, 255), (a, d, 40, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                posx += 0.6
            if event.key == pygame.K_LEFT:
                posx -= 0.6
            if event.key == pygame.K_d:
                rectx += 0.6
            if event.key == pygame.K_a:
                rectx -= 0.6
            if event.key == pygame.K_b:
                parax -= 0.18
                paray += 0.18
            if event.key == pygame.K_ESCAPE:
                quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
                posx = 0
                rectx = 0

    if rect2.colliderect(circle):
        paray = -1 * paray
    if rect1.colliderect(circle):
        paray = -1 * paray
    if ballx > 790:
        parax = -1*parax
    if ballx < 10:
        parax = -1 * parax
    if bally < 0:
        playertwo += 1
        ballx = 400
        bally = 300
    if bally > 600:
        playerone += 1
        ballx = 400
        bally = 300
    x += posx
    a += rectx
    ballx += parax
    bally += paray
    boundary()
    playeronescore()
    playertwoscore()
    pygame.display.update()
