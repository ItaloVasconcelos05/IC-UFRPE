from sympy import symbols

# Calcular o produto interno
def InnerProduct (vetor1, vetor2):
    try: 

        if not isinstance(vetor1, list) or not isinstance(vetor2, list):
            raise TypeError("Ambos os vetores devem ser do tipo lista.")

        if len(vetor1) != len(vetor2):
            raise ValueError("Os vetores devem ter o mesmo comprimento.")

        vetor1 = [symbols(x) if isinstance(x, str) else x for x in vetor1]
        vetor2 = [symbols(x) if isinstance(x, str) else x for x in vetor2]

        result = sum( x * y for x, y in zip(vetor1, vetor2[:-1])) - vetor1[-1] * vetor2[-1]

        print (str(result).replace("*", ""))

    except TypeError as e:
        print(f"Erro de tipo: {e}")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


InnerProduct(['a', 'b', 'c'], ['d', 'e', 'f'])


