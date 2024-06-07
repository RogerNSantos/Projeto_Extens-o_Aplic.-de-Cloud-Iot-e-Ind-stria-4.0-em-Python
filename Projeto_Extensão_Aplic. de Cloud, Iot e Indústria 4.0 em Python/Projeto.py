import time
import csv

class SistemaMonitoramento:
    def __init__(self):
        self.dados = []

    def coletar_dados(self):
        temperatura = float(input("Digite a temperatura (em °C): "))
        ph = float(input("Digite o valor de pH: "))
        return {'Temperatura': temperatura, 'PH': ph, 'Timestamp': time.time()}

    def avaliar_qualidade_agua(self, temperatura, ph):
        if 0 <= temperatura <= 40 and 6.5 <= ph <= 8.5:
            return "Água adequada para consumo. Temperatura e pH dentro dos limites recomendados."
        else:
            razoes = []
            if temperatura < 0 or temperatura > 40:
                razoes.append("A temperatura está fora dos limites recomendados (0°C - 40°C).")
            if ph < 6.5 or ph > 8.5:
                razoes.append("O pH está fora dos limites recomendados (6.5 - 8.5).")
            return "Água não adequada para consumo. Razões: {}".format(", ".join(razoes))

    def salvar_dados(self):
        with open('dados_monitoramento.csv', 'a', newline='') as csvfile:
            fieldnames = ['Timestamp', 'Temperatura', 'PH']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:  # Verifica se o arquivo está vazio
                writer.writeheader()

            for dado in self.dados:
                writer.writerow(dado)

    def iniciar_monitoramento(self, duracao, intervalo):
        tempo_inicial = time.time()
        while (time.time() - tempo_inicial) < duracao:
            dados = self.coletar_dados()
            self.dados.append(dados)
            print("Dados coletados:", dados)
            temperatura = dados['Temperatura']
            ph = dados['PH']
            resultado_avaliacao = self.avaliar_qualidade_agua(temperatura, ph)
            print(resultado_avaliacao)
            self.salvar_dados()
            time.sleep(intervalo)

if __name__ == "__main__":
    sistema = SistemaMonitoramento()
    duracao_monitoramento = int(input("Digite a duração do monitoramento (em segundos): "))
    intervalo_leitura = int(input("Digite o intervalo entre as leituras (em segundos): "))
    sistema.iniciar_monitoramento(duracao_monitoramento, intervalo_leitura)
