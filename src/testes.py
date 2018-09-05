Importjogovelha
importsys

erroInicializar= False
jogo = jogovelha.inicializar()

iflen(jogo) != 3:
    erroInicializar= True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar= True
        else:
            for elemento in linha:
                if elemento != '.':
                    erroInicializar= True
iferroInicializar:
    sys.exit(1)
else:
    sys.exit(0)