# Atribuição de variáveis
          
# Entrada de dados

a1 = float(input("Primeiro termo: "))
q = float(input("Razão: "))
n = int(input("Número de termos: "))

#Processamento de dados

an = a1*q**(n-1)
sum = (a1*((q**n)-1))/(q-1)
temp = (a1*(q**n-1))/(q-1)

# Saída de dados

print (an)
print (sum)
print (temp)