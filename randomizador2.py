import random
import PySimpleGUI as sg
from randomizador2chars import lista
import pygame

play = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByElEQVRoge3ZMWsUQRjG8Z8RFSKCgoJp0qSJjVpoZ2clkk8g5CtYpU+TD5DSUkvbVCFNYiM2dhZqY6GFQooEISGai8Xu4HgmcnM3c+su+4fj2L2dmedhb+Z95x16enp6hljBxaZF5OAE7/GoaSGTchJ9tnCrWTnjE0zs19+HWMPlJkWNQzAyh2c4rq+/YBnnmpOWRjASuIfX0f0d3GlAVzLDRmBG9Ta+1r8d4wVuTFdaGqcZCVzFOn7Uz+ziKc5PR1oa/zISWMRm9OxbPCisK5lRjASW8Clqs4H5MrLSSTECs1jFQd3ue319KbewVFKNBBbwMmr/EY8z6kpmXCOBh3gX9dNYdjCpEbigWs326r6OVKvdlQn7TSKHkcCcKt4MNJAd5DQSuI83Ud87uJ15jL8oYYTf2cE3f2YH1wuMhXJGAtdU8+WnwtlBaSOBu3gVjZc9O5iWEapJ/wSf6zEHeI6bZzWYmY6u/4v+rzUirZ/snVh+hwPitpYFxNanKJ1IGk9L4xcz6Eom18bqg5ZtrDqx1Y2LDwPVG2lV8aH15aDWF+jOKpkWi8o5GKWIXTwq56BzxwqdOejpxNFbJw5DO3M83dPT02J+AbN50HbYDxzCAAAAAElFTkSuQmCC'
stop = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAaklEQVRoge3ZQQqAMAxFwSre/8p6AZFUiXzKzLqLPNJVOwYAvLcVzpztU9Q8zrr/NUW3Y+JsZXsdSjdimY0ISSMkjZA0QtIISSMkjZA0QtIISSMkjZA0QtIISSMkzcxrfMo/ya1lNgIAX1zq+ANHUjXZuAAAAABJRU5ErkJggg=='
bg = sg.LOOK_AND_FEEL_TABLE[sg.CURRENT_LOOK_AND_FEEL]['BACKGROUND']


class TelaPython():
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('audios/guile.mp3')
        pygame.mixer.music.play()

        sg.change_look_and_feel('DarkBrown4')

        layout = [
            [sg.Text('Digite seu nome e clique em Rolar para sortear um personagem!')],
            [sg.Text('Seu Nome:', size=(10, 0)), sg.Input(size=(25, 0), key='nome')],
            [sg.Button('Rolar', size=(20, 0), button_color=(sg.YELLOWS[0], sg.BLUES[0]))],
            [sg.Button('Sair', size=(20, 0), button_color=(sg.YELLOWS[0], sg.BLUES[0]))],
            [sg.Output(size=(50, 5))],
            [sg.Text('Música ON/OFF: '), sg.Text(size=(12, 1))],
            [sg.Button(image_data=play, key='Play', border_width=0, button_color=(bg, bg)),
             sg.Button(image_data=stop, key='Stop', button_color=(bg, bg), border_width=0)]
        ]
        self.janela = sg.Window("RandomizadorSFV").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == 'Rolar':
                nome = self.values['nome']
                escolhido = random.choice(lista)
                print(f'{nome} jogue de {escolhido}')
            if self.button == 'Stop':
                pygame.mixer.music.stop()
            if self.button == 'Play':
                pygame.mixer.music.play()
            if self.button == 'Sair':
                break






tela = TelaPython()
tela.Iniciar()





























