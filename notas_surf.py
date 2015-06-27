f = open('surf.txt', 'r')
notas = {}

for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)] = nome
f.close()
for nota in sorted(notas, reverse=True):
    print('%s tem notas %4.2f'%(notas[nota], nota))
