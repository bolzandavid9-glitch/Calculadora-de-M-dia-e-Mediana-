print("                                       ----Calculadora de Média e Mediana----")
def media(numeros):
    soma =sum(numeros)
    quan =len(numeros)
    if quan == 0:
        return
    return soma/quan

def mediana(lista):
    quantidade = len(lista)
    lista_crecente = sorted(lista)
    if quantidade == 0:
        raise ValueError ("A lista não pode estar vazia")
    if quantidade % 2 == 0:
        indice_par = quantidade / 2
        indice_par -= 1
        valor_sem_div = lista_crecente[indice_par]
        return valor_sem_div
    else:
        indice_impar1 = quantidade / 2
        indice_impar1 =  int(indice_impar1)
        indice_impar1 -= 1
        indice_impar2 = indice_impar1 + 1
        valor1 = lista_crecente [indice_impar1]
        valor2 = lista_crecente [indice_impar2]
        Mediana_impar = (valor1 + valor2) / 2
        return Mediana_impar

numerosinput = []
print("digite sair para receber o resultado")
while True:
    valoresinput = input("digite os numeros: ")
    if valoresinput.lower() =="sair":
        break
    try:
        valores = float(valoresinput)
        numerosinput.append(valores)
    except:
        print("digite um valor valido")
    
resultado = media(numerosinput)
MeResultado = mediana(numerosinput)

print (f"Numeros digitados: {numerosinput}")
print(f"Média desses numeros é: {resultado}")
print(f"A Mediana dos numeros digitado é: {MeResultado}")