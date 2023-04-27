# códigos de entrada
codigo1 = '''
for i in range(1,10,1):
    a = i + 1
    b = i + 4

    soma = a + b
    print(soma)
'''

#codigo com alta similaridade
codigo2 = '''
for a in range(1,10,1):
    x = a + 1
    y = a + 4

    saida = x + y
    print(saida)
'''

#codigo com média similaridade
codigo3 = '''
for a in range(1,10,1):
    x = int(input())
    y = int(input())

    saida = x + y
    print(saida)
'''

codigo4 ='''
saida = input()
print("Ola "+ saida)
'''

#codigo com baixa similaridade


vetor_similar = [codigo1, codigo2]
vetor_meio_similar = [codigo1, codigo3]
vetor_nao_similar = [codigo1, codigo4]
