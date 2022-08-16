import pygame

pygame.init()

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
RAIO = 5
VELOCIDADE = 0.2

tela = pygame.display.set_mode((640, 480), 0)
x: int = 320
y: int = 240
vel_x: float = VELOCIDADE
vel_y: float = VELOCIDADE

while True:

    # Regras

    # ===== Movimento =====
    x += vel_x
    y += vel_y

    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE

    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE

    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (x, y), 30, 0)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
