from typing import List, Tuple


class Armazem:
    def __init__(self, localizacao: Tuple[int, int], estoque_minimo: int):
        self.localizacao = localizacao
        self.estoque_minimo = estoque_minimo


class Individuo:
    def __init__(self, veiculos: int, capacidade: int, rota: List[int]):
        self.veiculos = veiculos
        self.capacidade = capacidade
        self.rota = rota

    def __repr__(self):
        return f"Veiculos: {self.veiculos}, Capacidade: {self.capacidade}, Rota: {self.rota}"
    
    def calcular_fitness(self, capacidade_armazem_cidades: List[int], dist_matrix: List[List[float]]) -> float:
        capacidade_veiculo = self.capacidade
        rota = self.rota
        quantidade_veiculos = self.veiculos
        
        itens_por_armazem = [0] * len(capacidade_armazem_cidades) # Inicializa a quantidade de itens em cada armazem

        velocidade = 120 - capacidade_veiculo # A velocidade do veiculo diminui conforme a capacidade aumenta

        tempo_total = 0

        while True:

            rota_a_percorrer = []

            for i in range(len(rota)):
                armazem = rota[i]

                if itens_por_armazem[armazem] < capacidade_armazem_cidades[armazem]:
                    rota_a_percorrer.append(armazem)

            if not rota_a_percorrer:
                break

            #print (f"Armazens: {itens_por_armazem} - Rota: {rota_a_percorrer} - Veiculos: {quantidade_veiculos} - Capacidade: {capacidade_veiculo}")

            for i in range(len(rota_a_percorrer)):
                armazem = rota_a_percorrer[i]

                itens_por_armazem[armazem] += capacidade_veiculo * quantidade_veiculos

                if i == len(rota_a_percorrer) - 1:
                    distancia = dist_matrix[rota_a_percorrer[i]][0] # Volta para o primeiro armazem
                else:
                    distancia = dist_matrix[rota_a_percorrer[i]][rota_a_percorrer[i+1]]

                tempo = round(distancia / velocidade, 2)

                tempo_total += tempo * quantidade_veiculos

        return round(tempo_total, 2)