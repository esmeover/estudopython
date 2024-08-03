import pygame
import os

pygame.init()
pygame.mixer.init()

caminho_musica = 'C:/musica/musica.mp3'
caminho_imagem = 'c:/musica/player.png'

tela = pygame.display.set_mode((911, 700 ))
pygame.display.set_caption('Reproduzir música')

if not os.path.exists(caminho_musica):
    print(f'aquivo de musica nao encontrado: {caminho_musica}')
    quit()

if not os.path.exists(caminho_imagem):
    print(f'arquivo de imagem nao encontrado: {caminho_imagem}')
    quit()

pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play()

imagem = pygame.image.load(caminho_imagem)

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.blit(imagem, (0,0))
    pygame.display.flip()
pygame.quit()

