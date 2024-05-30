import pyautogui
import webbrowser

def navega_para_pagina_login(site: str):
    webbrowser.open_new(site)

def seleciona_campo_de_login():
    pyautogui.click(987, 295, duration=1.5)

def preenche_campos(email: str, senha: str):
    pyautogui.write(email, interval=0.4)
    pyautogui.press('tab', interval=1)
    pyautogui.write(senha, interval=0.4)

def clica_no_botao_de_login():
    pyautogui.click(991, 374, duration=1.2)

def clica_no_botao_agora_nao_navegador():
    pyautogui.click(999, 305, duration=1.3)
