from sympy import sympify

# Escrever os Vetores
def ReadVector (vetor):
    vetor = []

    for i in range (3):
        entrada = input(f"Digite a entrada {i+1}: ")
        vetor.append(sympify(entrada))

    return vetor

# Calcular o produto interno
def InnerProduct (vetor1, vetor2):
    result = vetor1[0]*vetor2[0] + vetor1[1]*vetor2[1] - vetor1[2]*vetor2[2]
    return result



vetorA = 0
vetorB = 0

print("Primeiro Vetor")
vetorA = ReadVector(vetorA)
print("\n")

print("Segundo Vetor")
vetorB = ReadVector(vetorB)
print("\n")

resultado = InnerProduct(vetorA, vetorB)

print (str(resultado).replace("*", ""))

