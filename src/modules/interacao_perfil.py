import pyautogui
import pyperclip

from modules.temporizadores import aguarda_carregamento_rapido

def seleciona_barra_de_pesquisa():
    pyautogui.click(1128, 142, duration=1.5)

def preenche_barra_de_pesquisa(perfil: str):
    pyautogui.write(perfil, interval=0.4)

def clica_no_perfil():
    pyautogui.click(1174, 256, duration=1.2)

def seleciona_ultima_postagem():
    pyautogui.click(825, 548, duration=1.4)
    aguarda_carregamento_rapido()

def verifica_curtida():
    try:
        img = pyautogui.locateOnScreen('src/assets/curtida.png')
        if img is not None:
            return True
    except pyautogui.ImageNotFoundException:
        return False

def adiciona_curtida():
    pyautogui.doubleClick(1033, 427, duration=1.2)

def adiciona_comentario(comentario: str, emojis: str):
    pyautogui.click(928, 581, duration=1.5)
    pyautogui.click(1016, 657, duration=1)
    pyautogui.write(comentario, interval=0.6)
    pyperclip.copy(emojis)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

def iterage_com_ultima_postagem(comentario: str, emojis: str):
    if verifica_curtida() is False:
        adiciona_curtida()
        adiciona_comentario(comentario, emojis)
