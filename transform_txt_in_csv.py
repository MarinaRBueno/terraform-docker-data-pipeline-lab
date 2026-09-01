import pandas as pd
import os
from create_file_txt import CreateDataFrame

class TransformTxtToCsv:
    """
    Uma classe para transformar um arquivo de texto (TXT) em um arquivo CSV.
    """
    
    def __init__(self, input_file, output_file):
        """
        Inicializa a classe TransformTxtToCsv.

        Args:
            input_file (str): O caminho para o arquivo de texto de entrada.
            output_file (str): O caminho para o arquivo CSV de saída.
        """
        self.input_file = input_file
        self.output_file = output_file

    def transform(self):
        """
        Lê o arquivo de texto de entrada, transforma-o em um DataFrame e o salva como um arquivo CSV.
        Cria o diretório de saída se ele não existir.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Arquivo de entrada não encontrado: {self.input_file}")

        # Read the text file into a DataFrame
        df = pd.read_csv(self.input_file, delimiter=',')  # Assuming comma-separated values in the text file
        
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        # Save the DataFrame to a CSV file
        df.to_csv(self.output_file, index=False)
# Example usage
#if __name__ == "__main__":
#    transformer = TransformTxtToCsv('entrada/output.txt', 'saida/output.csv')
#    transformer.transform()
