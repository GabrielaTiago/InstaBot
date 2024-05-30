import pyautogui

from services.temporizadores import aguarda_carregamento_rapido

def clica_no_perfil():
    pyautogui.leftClick(1233, 685, duration=1.3)

def clica_na_engrenagem():
    pyautogui.leftClick(954, 188, duration=1.5)

def clica_em_sair():
    pyautogui.leftClick(998, 529, duration=1.4)

def logout():
    clica_no_perfil()
    clica_na_engrenagem()
    aguarda_carregamento_rapido()
    clica_em_sair()

