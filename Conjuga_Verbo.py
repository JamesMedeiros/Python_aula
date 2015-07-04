pessoas = ['Eu ','Tu ','Ele ','Nos ','Vos ','Eles ']
conjuga_ar = ['o','as','a','amos', 'ais', 'am']
conjuga_er = ['o','es','e','emos','eis','em']
conjuga_ir = ['o','es','e','imos','is','em']
#pedimos ao usuario o verbo
verbo = input('Digite o infinitivo de um verbo regular:')
#separa a terminaçao do verbo
termina_em=verbo[-2:]
#agora, de acordo com a terminaçao do verbo, conjuga apropiadamente
if termina_em=='ar' :
    for i in range(6): #repete seis vezes, percorrendo a lista
        print(pessoas[i]+''+verbo[:-2]+conjuga_ar[i])
elif termina_em =='er' :
    for i in range(6): #repete seis vezes, percorrendo a lista
        print(pessoas[i]+''+verbo[:-2]+conjuga_er[i])
elif termina_em=='ir':
    for i in range(6): #repete seis vezes, percorrendo a lista
        print(pessoas[i]+''+verbo[:-2]+conjuga_er[i])
else:
    print('Tem certeza que'+verbo.upper+'e um verbo regular?')
    

