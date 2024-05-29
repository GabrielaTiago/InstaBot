from logs.logging import logging_config
from services.credenciamento import verifica_existencia_arquivo_com_credenciais, cria_arquivo_com_credenciais, recebe_credenciais_do_ususario, pega_credenciais_do_usuario, credenciais_validas

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

# [TO-DO]: Implementar lógica de login no Instagram
