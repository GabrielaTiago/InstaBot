import pyautogui

from modules.temporizadores import aguarda_carregamento_rapido

def fecha_postagem_em_aberto():
    pyautogui.leftClick(1237, 248, duration=1.5)

def clica_no_perfil():
    pyautogui.leftClick(1233, 688, duration=1.3)

def clica_na_engrenagem():
    pyautogui.leftClick(929, 182, duration=1.5)

def clica_em_sair():
    pyautogui.leftClick(996, 517, duration=1.4)

def logout():
    fecha_postagem_em_aberto()
    clica_no_perfil()
    clica_na_engrenagem()
    aguarda_carregamento_rapido()
    clica_em_sair()

