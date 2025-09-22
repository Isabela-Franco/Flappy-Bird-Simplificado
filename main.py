import pygame 
import random

#Inicializar o pygame
pygame.init()

#Configurar a tela 
LARGURA = 600
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Flappy Bird Simplificado')

#Cores
BRANCO = (255, 255, 255)
AZUL = (0, 150, 255)
VERDE = (0, 200, 0)
VERMELHO = (255, 0, 0)

#Variáveis do pássaro
passaro_x = 50
passaro_y = ALTURA // 2
velocidade = 0 
gravidade = 0.5
pulo = -7
raio_passaro = 15


#Variáveis do cano
largura_cano = 70
espaco = 150
velocidade_cano = 3
canos = []

#Função para criar canos
def criar_cano():
    altura_cano = random.randint(100, ALTURA - 100 - espaco)
    canos.append({'x': LARGURA, 'topo': altura_cano, 'baixo': altura_cano + espaco})

#Função para desenhar canos
def desenhar_canos():
    for c in canos:
        pygame.draw.rect(tela, VERDE, (c['x'], 0, largura_cano, c['topo']))
        pygame.draw.rect(tela, VERDE, (c['x'], c['baixo'], largura_cano, ALTURA - c['baixo']))

#Função para detectar colisão
def colisao():
    for c in canos:
        if passaro_x + raio_passaro > c['x'] and passaro_x - raio_passaro < c['x'] + largura_cano:
            if passaro_y - raio_passaro < c['topo'] or passaro_y + raio_passaro > c['baixo']:
                return True
            return False
         
criar_cano()
pontuacao = 0
rodando = True
relogio = pygame.time.Clock()

#Loop principal
while rodando:
    relogio.tick(60)
    tela.fill(AZUL)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade = pulo

    #Movimento do pássaro 
    velocidade += gravidade
    passaro_y += velocidade
    pygame.draw.circle(tela, VERMELHO, (passaro_x, int(passaro_y)), raio_passaro)

    #Movimento do cano 
    for c in canos:
        c['x'] -= velocidade_cano
        if canos[0]['x'] + largura_cano < 0:
            canos.pop(0)
            criar_cano()
            pontuacao += 1

    #Desenhar
    desenhar_canos()

    #Verificar colisão 
    if colisao():
        passaro_y = ALTURA // 2 
        velocidade = 0
        canos = []
        pontuacao = 0
        spawn_timer = 0
        criar_cano()  

    #Pontuação 
    fonte = pygame.font.SysFont(None, 40)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO) 
    tela.blit(texto, (10,10))   

    pygame.display.update()
pygame.quit()