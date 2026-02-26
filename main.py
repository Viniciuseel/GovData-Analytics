from etl.camara import tratar_deputados, extrair_deputados_brutos, salvar_dados_banco


def iniciar_pipeline():
    dados_sujos = extrair_deputados_brutos()
    print(dados_sujos)
    dados_limpos = tratar_deputados(dados_sujos)

    salvar_dados_banco(dados_limpos)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iniciar_pipeline()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

