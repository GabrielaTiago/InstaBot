from time import sleep

def aguarda_carregamento_lento():
    sleep(20)

def aguarda_carregamento_medio():
    sleep(10)

def aguarda_carregamento_rapido():
    sleep(2.5)

def pausa_automacao_24h():
    print('Aguardando 24h para continuar a automação...')
    sleep(86400)