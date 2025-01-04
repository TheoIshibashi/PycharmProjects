#Faca um programa em Python que abra e reproduza o audio de um arquivo mp3
import pygame
from pygame import mixer

mixer.init()

mixer.music.load('likehim.mp3')
mixer.music.play()
x = input('Digite algo para parar: ')

