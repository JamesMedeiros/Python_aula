tempo = float(input("Quantos minutos utilizados: "))
if tempo < 200:
tarifa = 0.20
elif tempo <= 400:
tarifa = 0.18
elif tempo <= 600:
tarifa = 0.15
else:
tarifa = 0.08
print ("O valor da conta será de R$%6.2f"%(tempo * tarifa)) 
