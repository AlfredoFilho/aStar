'''
*******************Developed by********************************
    
Alfredo Albelis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januario - https://github.com/brendajanuario
Cleofas Peres Santos -  https://github.com/CleoPeres
Pedro Bernini - https://github.com/PedroBernini
Vinicius Abrantes - https://github.com/viniciusAbrantes

**************************************************************** 
'''

#import sys
from dataclasses import dataclass

tabuleiro = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),(0, 8),(0, 9),(0, 10),
             (1, 0),(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(1, 7),(1, 8),(1, 9),(1, 10),
             (2, 0),(2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),(2, 7),(2, 8),(2, 9),(2, 10),
             (3, 0),(3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 6),(3, 7),(3, 8),(3, 9),(3, 10),
             (4, 0),(4, 1),(4, 2),(4, 3),(4, 4),(4, 5),(4, 6),(4, 7),(4, 8),(4, 9),(4, 10),
             (5, 0),(5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 6),(5, 7),(5, 8),(5, 9),(5, 10),
             (6, 0),(6, 1),(6, 2),(6, 3),(6, 4),(6, 5),(6, 6),(6, 7),(6, 8),(6, 9),(6, 10),
             (7, 0),(7, 1),(7, 2),(7, 3),(7, 4),(7, 5),(7, 6),(7, 7),(7, 8),(7, 9),(7, 10),
             (8, 0),(8, 1),(8, 2),(8, 3),(8, 4),(8, 5),(8, 6),(8, 7),(8, 8),(8, 9),(8, 10),
             (9, 0),(9, 1),(9, 2),(9, 3),(9, 4),(9, 5),(9, 6),(9, 7),(9, 8),(9, 9),(9, 10),
             (10, 0),(10, 1),(10, 2),(10, 3),(10, 4),(10, 5),(10, 6),(10, 7),(10, 8),(10, 9),(10, 10)]

def distance(gato, saida) :
    diference = saida[1] - gato [1] # Diferenca de colunas
    if(gato[0] == saida[0]) :
        return abs(diference)

    if(gato[0] % 2 == 1) : # Caso o gato estiver em linha ímpar
        if(abs(gato[0] - saida[0]) == 1) : # Diferenca de 1 linha
            if(diference <= 0) :
                return abs(diference) + 1
            else :
                return abs(diference)
            
        if(abs(gato[0] - saida[0]) == 2) : # Diferenca de 2 linhas
            if(diference == 0) :
                return 2
            else :
                return abs(diference) + 1
            
        if(abs(gato[0] - saida[0]) == 3) : # Diferenca de 3 linhas
            if(diference >= -1 and diference <= 2) :
                return 3
            elif(diference > 0) :
                return abs(diference) + 1
            elif(diference < 0) :
                return abs(diference) + 2
               
        if(abs(gato[0] - saida[0]) == 4) : # Diferenca de 4 linhas
            if(diference >= -2 and diference <= 2) :
                return 4
            else :
                return abs(diference) + 2
           
        if(abs(gato[0] - saida[0]) == 5) : # Diferenca de 5 linhas
            if(diference >= -2 and diference <= 3) :
                return 5
            elif(diference > 0) :
                return abs(diference) + 2
            elif(diference < 0) :
                return abs(diference) + 3
           
        if(abs(gato[0] - saida[0]) == 6) : # Diferenca de 6 linhas
            if(diference >= -3 and diference <= 3) :
                return 6
            else :
                return abs(diference) + 3
            
        if(abs(gato[0] - saida[0]) == 7) : # Diferenca de 7 linhas
            if(diference >= -3 and diference <= 4) :
                return 7
            elif(diference > 0) :
                return abs(diference) + 3
            elif(diference < 0) :
                return abs(diference) + 4
           
        if(abs(gato[0] - saida[0]) == 8) : # Diferenca de 8 linhas
            if(diference >= -4 and diference <= 4) :
                return 8
            else :
                return abs(diference) + 4
            
        if(abs(gato[0] - saida[0]) == 9) : # Diferenca de 9 linhas
            if(diference >= -4 and diference <= 5) :
                return 9
            elif(diference > 0) :
                return abs(diference) + 4
            elif(diference < 0) :
                return abs(diference) + 5
           
    else : # Caso o gato estiver em linha par
        if(abs(gato[0] - saida[0]) == 1) : # Diferenca de 1 linha
            if(diference >= 0) :
                return abs(diference) + 1
            else :
                return abs(diference)
            
        if(abs(gato[0] - saida[0]) == 2) : # Diferenca de 2 linhas
            if(diference == 0) :
                return 2
            else :
                return abs(diference) + 1
            
        if(abs(gato[0] - saida[0]) == 3) : # Diferenca de 3 linhas
            if(diference >= -2 and diference <= 1) :
                return 3
            elif(diference > 0) :
                return abs(diference) + 2
            elif(diference < 0) :
                return abs(diference) + 1
               
        if(abs(gato[0] - saida[0]) == 4) : # Diferenca de 4 linhas
            if(diference >= -2 and diference <= 2) :
                return 4
            else :
                return abs(diference) + 2
           
        if(abs(gato[0] - saida[0]) == 5) : # Diferenca de 5 linhas
            if(diference >= -3 and diference <= 2) :
                return 5
            elif(diference > 0) :
                return abs(diference) + 3
            elif(diference < 0) :
                return abs(diference) + 2
           
        if(abs(gato[0] - saida[0]) == 6) : # Diferenca de 6 linhas
            if(diference >= -3 and diference <= 3) :
                return 6
            else :
                return abs(diference) + 3
            
        if(abs(gato[0] - saida[0]) == 7) : # Diferenca de 7 linhas
            if(diference >= -4 and diference <= 3) :
                return 7
            elif(diference > 0) :
                return abs(diference) + 4
            elif(diference < 0) :
                return abs(diference) + 3
           
        if(abs(gato[0] - saida[0]) == 8) : # Diferenca de 8 linhas
            if(diference >= -4 and diference <= 4) :
                return 8
            else :
                return abs(diference) + 4
            
        if(abs(gato[0] - saida[0]) == 9) : # Diferenca de 9 linhas
            if(diference >= -5 and diference <= 4) :
                return 9
            elif(diference > 0) :
                return abs(diference) + 5
            elif(diference < 0) :
                return abs(diference) + 4
           
        if(abs(gato[0] - saida[0]) == 10) : # Diferenca de 10 linhas
            if(diference >= -5 and diference <= 5) :
                return 10
            else :
                return abs(diference) + 5
    
@dataclass
class celula:
    def __init__(self, coordenada, distancia, pai):
        self.coordenada = coordenada
        self.distancia = distancia
        self.pai = pai

gato = (5, 5)
bloqueados = []
saida = (5, 6)
lista_aberta = []
lista_fechada = []
listaStructAbertas = []
        

#lista com as celulas inicias em volta do gato
em_volta = [((gato[0], gato[1] + 1)),
           ((gato[0] + 1, gato[1] + 1)),
           ((gato[0] + 1, gato[1])),
           ((gato[0], gato[1] - 1)),
           ((gato[0] - 1, gato[1])),
           ((gato[0] - 1, gato[1] + 1))]

#Verificar se as celulas iniciais em volta não são bloqueados e não estão fora do limite do tabuleiro para poder iniciar a lista aberta
for el in em_volta:
    if el not in bloqueados and el[0] >= 0 and el[0] <= 10 and el[1] >=0 and el[1] <= 10:
        lista_aberta.append(el)

#preencher struct com posicao,distancia e o pai (que ainda é a posição do gato)
for el in lista_aberta:
    dist = distance(el, saida)
    listaStructAbertas.append(celula(el, dist, gato))
    
for el in listaStructAbertas:
    print("----------------")
    print("Pai:     ", el.pai)
    print("Posição: ", el.coordenada)
    print("Saida:   ", saida)
    print("Distancia: ", el.distancia)
    print("----------------")
    print("\n")
    
