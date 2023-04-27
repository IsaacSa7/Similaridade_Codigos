import torch
from transformers import AutoTokenizer, AutoModel
from codigos import vetor_similar, vetor_nao_similar

# importa o tokenizador e o modelo CodeBERT
tokenizador = AutoTokenizer.from_pretrained("microsoft/codebert-base")
modelo = AutoModel.from_pretrained("microsoft/codebert-base")

#codigo
codigo1 = '''
for i in range(1,10,1):
    x = 5 + i
    print(i)
'''

code = '''
x = input("Insira o seu nome: ")
nome = x
print("O seu nome é "+ nome)
'''

#vetores de entrada
entrada = [codigo1, code]

# tokeniza e codifica os códigos
tokens = tokenizador(entrada, return_tensors='pt', padding=True, truncation=True)

# calcula a similaridade
embendding = modelo(input_ids=tokens['input_ids'], attention_mask=tokens['attention_mask'])
vetor_saida = embendding.last_hidden_state

similarity = torch.cosine_similarity(vetor_saida[0].mean(dim=0), vetor_saida[1].mean(dim=0), dim=0)

#coloca a similaridade entre o intervalo 0 e 1
similarity = (similarity + 1) / 2

# imprime a similaridade
print(f"A similaridade entre os códigos é: {similarity.item()}") # esse item retorna um float
