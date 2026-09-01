import pandas as pd
import os

class CreateDataFrame:
    """
    Uma classe para criar um DataFrame pandas e salvá-lo em um arquivo CSV.
    """
    
    def __init__(self):
        """
        Inicializa a classe CreateDataFrame com um DataFrame vazio.
        """
        self.df = None

    def create_dataframe(self):
        """
        Cria um DataFrame pandas com dados de exemplo.
        """
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }
        self.df = pd.DataFrame(data)
        return self.df

    def save_to_csv(self, filename):
        """
        Salva o DataFrame em um arquivo CSV.
        Cria o diretório de saída se ele não existir.

        Args:
            filename (str): O caminho completo do arquivo CSV a ser salvo.
        """
        if self.df is not None:
            output_dir = os.path.dirname(filename)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
            self.df.to_csv(filename, index=False)
        else:
            raise ValueError("DataFrame está vazio. Crie o DataFrame antes de salvar em CSV.")

    def execute(self, filename):
        """
        Executa o processo de criação e salvamento do DataFrame.

        Args:
            filename (str): O caminho completo do arquivo CSV a ser salvo.
        """
        self.create_dataframe()
        self.save_to_csv(filename)


#create_csv = CreateDataFrame()
#create_csv.execute('entrada/output.txt')