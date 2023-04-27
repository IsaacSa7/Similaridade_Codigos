import torch
from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM
from typing import List
import os 
from codigos import vetor_nao_similar, vetor_meio_similar, vetor_similar

#Declaração de vetores
similar = vetor_similar
meio_similar = vetor_meio_similar
nao_similar = vetor_nao_similar

#Vetor de entrada para a verificação de clonagem
entrada = vetor_nao_similar

# importa o tokenizador e o modelo CodeBERT
tokenizador = AutoTokenizer.from_pretrained("microsoft/codebert-base-mlm")
os.system("clear")
modelo = AutoModel.from_pretrained("microsoft/codebert-base-mlm")
os.system("clear")

def calcular_similaridade(codigos: List[str]) -> float:
    # tokeniza e codifica os códigos
    tokens = tokenizador(codigos, return_tensors='pt', padding=True, truncation=True)
    # gera as máscaras de preenchimento
    mascara1 = tokens['input_ids'][0] != tokenizador.pad_token_id
    mascara2 = tokens['input_ids'][1] != tokenizador.pad_token_id
    # passa os códigos pelo modelo e pega os embeddings da última camada
    saida = modelo(**tokens).last_hidden_state
    # seleciona apenas os embeddings dos tokens dos códigos e ignora os demais (com índice 1 na máscara)
    vetor_saida1 = saida[0][mascara1]
    vetor_saida2 = saida[0][mascara2]
    # calcula a distância Euclidiana
    distancia = torch.dist(vetor_saida1.mean(dim=0), vetor_saida2.mean(dim=0), p=2)
    # coloca a similaridade entre o intervalo 0 e 1
    similaridade = 1.0 / (1.0 + distancia.item())
    return similaridade

similaridade = calcular_similaridade(entrada)
s = similaridade * 100

#imprimindo dados
print("SIMILARIDADE: %.2f%%" %(s))
