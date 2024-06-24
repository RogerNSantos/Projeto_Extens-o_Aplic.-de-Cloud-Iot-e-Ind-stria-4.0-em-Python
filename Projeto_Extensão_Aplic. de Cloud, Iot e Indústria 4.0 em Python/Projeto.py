import tkinter as tk
from tkinter import messagebox
import time
import csv

class SistemaMonitoramento:
    def __init__(self):
        self.dados = []

    def coletar_dados(self, temperatura, ph):
        timestamp = time.time()
        return {'Temperatura': temperatura, 'PH': ph, 'Timestamp': timestamp}

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
            temperatura, ph = self.obter_dados_gui()
            dados = self.coletar_dados(temperatura, ph)
            self.dados.append(dados)
            print("Dados coletados:", dados)
            resultado_avaliacao = self.avaliar_qualidade_agua(temperatura, ph)
            print(resultado_avaliacao)
            self.salvar_dados()
            time.sleep(intervalo)

    def obter_dados_gui(self):
        # Aqui você poderá implementar a interface gráfica para obter os dados
        # Por enquanto, vamos retornar valores fixos para fins de demonstração
        return 25.0, 7.0  # Exemplo de temperatura e pH fixos

def iniciar_monitoramento_gui():
    duracao_monitoramento = int(entry_duracao.get())
    intervalo_leitura = int(entry_intervalo.get())
    sistema.iniciar_monitoramento(duracao_monitoramento, intervalo_leitura)

# Configuração da interface gráfica usando tkinter
root = tk.Tk()
root.title("Monitoramento de Qualidade da Água")

label_duracao = tk.Label(root, text="Digite a duração do monitoramento (segundos):")
label_duracao.pack()
entry_duracao = tk.Entry(root)
entry_duracao.pack()

label_intervalo = tk.Label(root, text="Digite o intervalo entre as leituras (segundos):")
label_intervalo.pack()
entry_intervalo = tk.Entry(root)
entry_intervalo.pack()

button_iniciar = tk.Button(root, text="Iniciar Monitoramento", command=iniciar_monitoramento_gui)
button_iniciar.pack()

sistema = SistemaMonitoramento()

root.mainloop()
