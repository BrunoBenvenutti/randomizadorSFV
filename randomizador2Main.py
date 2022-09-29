import random
import pygame
from time import sleep
pygame.init()

#ORIGINAL
c1 = str("Ryu")
c2 = str("Chun-Li")
c3 = str("Nash")
c4 = str("M. Bison")
c5 = str("Cammy")
c6 = str("Birdie")
c7= str("Ken")
c8 = str("Necalli")
c9 = str("Vega")
c10 = str("R. Mika")
c11 = str("Rashid")
c12 = str("Karin")
c13 = str("Zangief")
c14 = str("Laura")
c15 = str("Dhalsim")
c16 = str("F.A.N.G")

#SEASON 1
c17 = str("Alex")
c18 = str("Guile")
c19 = str("Ibuki")
c20 = str("Balrog")
c21 = str("Juri")
c22 = str("Urien")

#SEASON 2
c23 = str("Akuma")
c24 = str("Kolin")
c25 = str("Ed")
c26 = str("Abigail")
c27 = str("Menat")
c28 = str("Zeku")

#SEASON 3
c29 = str("Sakura")
c30 = str("Blanka")
c31 = str("Falke")
c32 = str("Cody")
c33 = str("G")
c34 = str("Sagat")

#SEASON 4
c35 = str("Kage")
c36 = str("Poison")
c37 = str("E. Honda")
c38 = str("Lucia")
c39 = str("Gill")
c40 = str("Seth")



n = ""
while (n != "n"):
    n = input("Street Fighter V Character Randomizer. Aperte S para sortear um personagem e N para cancelar.")


    if (n == "s"):

      pygame.mixer.music.load('tambor.mp3')
      pygame.mixer.music.play()

      lista = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21,
               c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40]
      escolhido = random.choice(lista)
      print("\n")
      print("Você Jogará de...")
      sleep(8)
      print("\n")
      print("Jogue de {}".format(escolhido))
      print("\n")

    elif (n == "n"):
        print("\n")
        print("Programa Encerrado")
    elif (n != "n" or "s"):
        print("Resposta inválida")








