import math
import statistics

# --------------------------------------------FUNCTIONS------------------------------------------------------ #


def permutation(n, p):
    return math.factorial(n) / math.factorial(n-p)


def combination(n, p):
    return math.factorial(n) / (math.factorial(p) * math.factorial(n-p))


def binomial_distribution(x, n, p):
    return combination(n, x) * pow(p, x) * pow(1 - p, n - x)


def poisson_distribution(x, p):
    return pow(math.e, -p) * pow(p, x) / math.factorial(x)


def hypergeometric_distribution(x: float, n: float, N: float, N1: float):
    N2 = float(N - N1)
    return (combination(N1, x) * combination(N2, float(n - x))) / combination(N, n)


# --------------------------------------------MAIN------------------------------------------------------ #

while True:
    print("--- Statistics and Probability ---")
    print("1- Media, Mediana, Moda e Desvio Padrao \n "
          "2- Combinacao \n "
          "3- Permutacao \n "
          "4- Distribuicao Binomial \n "
          "5- Distribuicao Poisson \n "
          "6- Distribuicao Hipergeometrica \n"
          "0- Sair")
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

    elif op == 2:
        print("Combinacao - C(n, p)")

        m = float(input("n (total) = "))
        p = float(input("p (selecionados) = "))

        result = combination(n, p)
        result = round(result, 4)
        print("C(" + str(n) + ", " + str(p) + ") = " + str(result))

    elif op == 3:
        print("Permutacao - P(n, p)")

        m = float(input("n (total) = "))
        p = float(input("p (selecionados) = "))

        result = permutation(n, p)
        result = round(result, 4)
        print("P(" + str(n) + ", " + str(p) + ") = " + str(result))

    elif op == 4:
        print("Distribuicao Binomial")

        n = float(input("n (numero de repeticoes do experimento de bernoulli) = "))
        p = float(input("p (numero medio de sucessos) = "))
        x = float(input("x (numero de sucessos) = "))

        result = binomial_distribution(x, n, p)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 5:
        print("Distribuicao Poisson")

        x = float(input("x (numero de sucessos) = "))
        p = float(input("p (numero medio de sucessos) = "))

        result = poisson_distribution(x, p)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 6:
        print("Distribuicao Hipergeometrica")

        n = float(input("n (numero de repeticoes do experimento) = "))
        N = float(input("N (tamanho da populacao) = "))
        N1 = float(input("N1 (tamanho da sub-populacao de interesse) = "))
        x = float(input("x (variavel) = "))

        result = hypergeometric_distribution(x, n, N, N1)
        result = round(result, 4)
        print(" = " + str(result))

    else:
        print("Comando invalido!")
