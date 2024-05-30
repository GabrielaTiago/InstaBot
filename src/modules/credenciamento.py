import os
import pyautogui
from logs.logging import error, info, warning

TITTE = 'Informações de login'
FILE_PATH = 'src/credenciais.txt'

def verifica_existencia_arquivo_com_credenciais():
    if os.path.exists(FILE_PATH):
        info('Arquivo de credenciais encontrado')
        return True
    else:
        return False

def cria_arquivo_com_credenciais(email: str, senha: str):
    path = 'src/credenciais.txt'
    with open(path, 'w') as file:
        file.write(f'EMAIL = {email}\nSENHA = {senha}')
        info('Arquivo de credenciais criado com sucesso')

def recebe_credenciais_do_ususario():
    pyautogui.alert(title=TITTE, text='Digite suas credenciais')
    email = recebe_email()
    senha = recebe_senha()
    if credenciais_validas(email, senha) is False:
        return recebe_credenciais_do_ususario()
    return email, senha

def recebe_email():
    email = pyautogui.prompt(title=TITTE, text='Digite seu email:')
    while digitou_credencial(email) is False:
        warning('Email nao digitada')
        email = pyautogui.prompt(title='Informação de Email é Necessária', text='Digite seu email:')
    return email

def recebe_senha():
    senha = pyautogui.password(title=TITTE, text='Digite sua senha:', mask='*')
    while digitou_credencial(senha) is False:
        warning('Senha nao digitada')
        senha = pyautogui.password(title='Informação de Email é Necessária', text='Digite sua senha:', mask='*')
    return senha

def digitou_credencial(credencial: str):
    return credencial != '' and credencial is not None

def credenciais_validas(email: str, senha: str):
    # [TO-DO]: Implementar validação de credenciais
    if email == '' or senha == '':
        error('Credenciais invalidas')
        return False
    info('Credenciais validas')
    return True

def pega_credenciais_do_usuario():
    with open(FILE_PATH, 'r') as file:
        email = file.readline().split('=')[-1].strip()
        senha = file.readline().split('=')[-1].strip()
        return email, senha
