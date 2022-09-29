import random
import PySimpleGUI as sg
from chars import lista
#from playsound import playsound

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')

        layout = [
            [sg.Text('Digite seu nome e clique em Rolar para sortear um personagem!')],
            [sg.Text('Seu Nome:', size=(10, 0)), sg.Input(size=(25, 0), key='nome')],
            [sg.Button('Rolar', size=(20, 0), button_color=(sg.YELLOWS[0], sg.BLUES[0]))],
            [sg.Output(size=(50, 5))],
            #[sg.Image(r'juri.png')],

        ]
        self.janela = sg.Window("RandomizadorSFV").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            escolhido = random.choice(lista)
            print(f'{nome} jogue de {escolhido}')

tela = TelaPython()
tela.Iniciar()






