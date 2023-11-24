""" Desafio 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. """

# Importação de bibliotecas
import pygame

# Inicialização do pygame
pygame.init()

# Carrega o arquivo mp3
pygame.mixer.music.load('guanacast-33.mp3')

# Inicia a reprodução
pygame.mixer.music.play()

# Mantém o programa rodando até que a música termine
input()  # A nova versão exige o uso de input(
pygame.event.wait()
