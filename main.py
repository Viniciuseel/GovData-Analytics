from etl.camara import tratar_deputados, extrair_deputados_brutos, salvar_dados


def iniciar_pipeline():
    dados_sujos = extrair_deputados_brutos()

    dados_limpos = tratar_deputados(dados_sujos)

    salvar_dados(dados_limpos)
    print(dados_limpos)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iniciar_pipeline()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

