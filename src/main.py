from logs.logging import logging_config
from services.credenciamento import verifica_existencia_arquivo_com_credenciais, cria_arquivo_com_credenciais, recebe_credenciais_do_ususario, pega_credenciais_do_usuario, credenciais_validas
from services.login import navega_para_pagina_login, seleciona_campo_de_login, preenche_campos, clica_no_botao_de_login, clica_no_botao_agora_nao_navegador
from services.interacao_perfil import seleciona_barra_de_pesquisa, preenche_barra_de_pesquisa, clica_no_perfil, seleciona_ultima_postagem, iterage_com_ultima_postagem
from services.temporizadores import aguarda_carregamento_medio, aguarda_carregamento_rapido, pausa_automacao_24h
from services.logout import logout

SITE = 'https://www.instagram.com'
PERFIL = 'adele'
COMENTARIO = 'Love you! Please come to Brasil '
EMOJIS = '💚💛'

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

aguarda_carregamento_medio()

seleciona_campo_de_login()

preenche_campos(email, senha)

clica_no_botao_de_login()

aguarda_carregamento_rapido()

clica_no_botao_agora_nao_navegador()

# INTERAÇÃO COM O PERFIL E POSTAGENS
seleciona_barra_de_pesquisa()

preenche_barra_de_pesquisa(PERFIL)

clica_no_perfil()

aguarda_carregamento_rapido()

seleciona_ultima_postagem()

iterage_com_ultima_postagem(comentario=COMENTARIO, emojis=EMOJIS)

logout()

pausa_automacao_24h()
