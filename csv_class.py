import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    ## receber um str str[] - vetor de strings
    def filtrar(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        
        else:
            return self.filtrar(colunas[1:], atributos[1:])
        
    #     self.df_filtrado = self.df[self.df[coluna] == atributo]
    #     return self.df_filtrado
    
    # def sub_filtro(self, coluna, atributo):
    #     return self.df_filtrado[self.df[coluna] == atributo]
        

