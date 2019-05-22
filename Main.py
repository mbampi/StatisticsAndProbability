import math
import statistics

# --------------------------------------------FUNCTIONS------------------------------------------------------ #

def combination(m: float, p: float):
    result = math.factorial(m) / (math.factorial(p) * math.factorial(m-p))
    return result


def hypergeometric_distribution(x: float, n: float, N: float, N1: float):

    N2 = float(N - N1)
    result = (combination(N1, x) * combination(N2, float(n - x))) / combination(N, n)
    return result


# --------------------------------------------MAIN------------------------------------------------------ #

while True:
    print("Statistics and Probability")
    print(" 1- Media, Mediana, Moda, Desvio Padrao \n 4- Combinacao \n 5- Distribuicao Hipergeometrica")
    op = int(input("-> "))

    if op == 0:
        break

    elif op == 1:
        print("Media")
        s = input("Numeros [divididos por ',' (virgula)] = ")
        numbers = s.split(',')

        mean = statistics.mean(numbers)
        mode = statistics.mode(numbers)
        median = statistics.median(numbers)
        std_deviation = statistics.stdev(numbers)

        print("Media = " + mean)
        print("Mediana = " + median)
        print("Moda = " + mode)
        print("Desvio Padrao= " + std_deviation)

    elif op == 4:
        print("Combinacao")
        print("C(m,p) = m! / p!(m-p!)")

        m = float(input("m= "))
        p = float(input("p= "))

        result = combination(m, p)
        result = round(result, 4)
        print("C(" + str(m) + ", " + str(p) + ") = " + str(result))

    elif op == 5:
        print("Distribuicao Hipergeometrica")
        print("P(x) = C(N1, x)*C(N2, n-x) / C(N, n)")

        n = float(input("n (numero de repeticoes do experimento) = "))
        N = float(input("N (tamanho da populacao) = "))
        N1 = float(input("N1 (tamanho da sub-populacao de interesse) = "))
        x = float(input("x (variavel) = "))

        result = hypergeometric_distribution(x, n, N, N1)
        result = round(result, 4)
        print(" = " + str(result))

    else:
        print("Comando invalido!")
