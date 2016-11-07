import pygame, sys, os, time

while True:
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_a]:
		print "a"
