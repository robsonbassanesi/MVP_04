import pandas as pd

url_certo = "database/cancer_data.csv"


class Carregador:

    def carregar_dados(self, url: str, atributos: list):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros 
        no read_csv que poderiam ser utilizados para dar opções 
        adicionais.
        """

        return pd.read_csv(url, names=atributos, skiprows=1, delimiter=',')
