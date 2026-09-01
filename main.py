import os
from create_file_txt import CreateDataFrame
from transform_txt_in_csv import TransformTxtToCsv

class DataPipeline:
    """
    Orquestra as etapas de criação e transformação de dados.
    """
    def __init__(self, input_txt_path, output_csv_path):
        """
        Inicializa a pipeline de dados com os caminhos dos arquivos de entrada e saída.

        Args:
            input_txt_path (str): Caminho para o arquivo TXT de entrada.
            output_csv_path (str): Caminho para o arquivo CSV de saída.
        """
        self.input_txt_path = input_txt_path
        self.output_csv_path = output_csv_path
        self.create_data_frame_instance = CreateDataFrame()
        self.transform_txt_to_csv_instance = TransformTxtToCsv(input_txt_path, output_csv_path)

    def run_pipeline(self):
        """
        Executa a pipeline de dados completa: cria o DataFrame, salva em TXT e transforma em CSV.
        """
        print(f"Iniciando a pipeline de dados...")

        # 1. Criar DataFrame e salvar em arquivo TXT
        print(f"Criando DataFrame e salvando em {self.input_txt_path}...")
        self.create_data_frame_instance.execute(self.input_txt_path)
        print(f"DataFrame salvo com sucesso em {self.input_txt_path}.")

        # 2. Transformar arquivo TXT em CSV
        print(f"Transformando {self.input_txt_path} em {self.output_csv_path}...")
        self.transform_txt_to_csv_instance.transform()
        print(f"Transformação concluída. Arquivo CSV salvo em {self.output_csv_path}.")

        print("Pipeline de dados concluída com sucesso!")

if __name__ == "__main__":
    INPUT_TXT = 'entrada/output.txt'
    OUTPUT_CSV = 'saida/output.csv'

    pipeline = DataPipeline(INPUT_TXT, OUTPUT_CSV)
    pipeline.run_pipeline()