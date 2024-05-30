from time import sleep

from logs.logging import logging_config
from services.credenciamento import verifica_existencia_arquivo_com_credenciais, cria_arquivo_com_credenciais, recebe_credenciais_do_ususario, pega_credenciais_do_usuario, credenciais_validas
from services.login import navega_para_pagina_login, seleciona_campo_de_login, preenche_campos, clica_no_botao_de_login, clica_no_botao_agora_nao_navegador

SITE = 'https://www.instagram.com'

# CONFIGURAÇÕES DE LOGS
logging_config()

# CREDENCIAIS
if(verifica_existencia_arquivo_com_credenciais()):
    email, senha = pega_credenciais_do_usuario()

    if credenciais_validas(email, senha) is False:
        email, senha = recebe_credenciais_do_ususario()
        cria_arquivo_com_credenciais(email, senha)
else:
    email, senha = recebe_credenciais_do_ususario()
    cria_arquivo_com_credenciais(email, senha)

# LOGIN
navega_para_pagina_login(SITE)

sleep(8)

seleciona_campo_de_login()

preenche_campos(email, senha)

clica_no_botao_de_login()

sleep(5)

clica_no_botao_agora_nao_navegador()

