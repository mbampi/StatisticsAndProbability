import math
import statistics
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy import stats as st
import numpy as np

# --------------------------------------------FUNCTIONS------------------------------------------------------ #


def permutation(n, p):
    return math.factorial(n) / math.factorial(n-p)


def circular_permutation(n):
    return math.factorial(n-1)


def combination(n, p):
    return math.factorial(n) / (math.factorial(p) * math.factorial(n-p))


def binomial_distribution(x, n, p):
    return combination(n, x) * pow(p, x) * pow(1 - p, n - x)


def poisson_distribution(x, p):
    return pow(math.e, -p) * pow(p, x) / math.factorial(x)


def hypergeometric_distribution(x: float, n: float, N: float, N1: float):
    N2 = float(N - N1)
    return (combination(N1, x) * combination(N2, float(n - x))) / combination(N, n)


def mean_confidence_interval(sample_mean, sample_size, confidence_level, v=None, standard_deviation=None):
    if sample_size > 30 or standard_deviation is not None:
        z = normal_distribution_area(confidence_level/2)
        confidence_variation = z * standard_deviation / math.sqrt(sample_size)
        return sample_mean, confidence_variation

    # TODO
    elif sample_size <= 30 and standard_deviation is None:
        t = student_distribution_area(v, confidence_level/2)
        confidence_variation = t * standard_deviation / math.sqrt(sample_size)
        return sample_mean, confidence_variation


def normal_probability_density(x):
    constant = 1.0 / math.sqrt(2*math.pi)
    return constant * math.exp((-x**2) / 2.0)


def normal_distribution_area(z):
    area, _ = quad(normal_probability_density, 0, z)
    return area


# TODO
def student_distribution_area(v, t):
    area, _ = quad(normal_probability_density, 0, t)
    return area


# --------------------------------------------MAIN------------------------------------------------------ #


while True:
    print("--- Statistics and Probability ---")
    print("1- Media, Mediana, Moda e Desvio Padrao \n "
          "2- Permutacao \n "
          "3- Permutacao Circular \n "
          "4- Combinacao \n "
          "5- Distribuicao Binomial \n "
          "6- Distribuicao Poisson \n "
          "7- Distribuicao Hipergeometrica \n"
          "8- Normal Distribution Area \n"
          "0- Sair")
    op = int(input("-> "))

    if op == 0:
        break

    elif op == 1:
        print("Media")
        s = input("Numeros [divididos por ',' (virgula)] = ")
        numbers = s.split(',')
        for index, item in enumerate(numbers):
            numbers[index] = float(item)

        mean = statistics.mean(numbers)
        mode = statistics.mode(numbers)
        median = statistics.median(numbers)
        std_deviation = statistics.stdev(numbers)

        numbers.sort()
        range = (numbers[0]-1, numbers[len(numbers)-1]+1)
        plt.hist(numbers, color='blue', range=range, histtype='bar', rwidth=0.8)
        plt.xlabel("Dados")
        plt.ylabel("No. de ocorrencias")
        plt.show()

        print("Media = " + str(mean))
        print("Mediana = " + str(median))
        print("Moda = " + str(mode))
        print("Desvio Padrao= " + str(std_deviation))

    elif op == 2:
        print("Permutacao - P(n, p)")

        m = float(input("n (total) = "))
        p = float(input("p (selecionados) = "))

        result = permutation(n, p)
        result = round(result, 4)
        print("P(" + str(n) + ", " + str(p) + ") = " + str(result))

    elif op == 3:
        print("Permutacao Circular - PC(n)")

        m = float(input("n (total) = "))

        result = circular_permutation(n)
        result = round(result, 4)
        print("PC(" + str(n) + ") = " + str(result))

    elif op == 4:
        print("Combinacao - C(n, p)")

        m = float(input("n (total) = "))
        p = float(input("p (selecionados) = "))

        result = combination(n, p)
        result = round(result, 4)
        print("C(" + str(n) + ", " + str(p) + ") = " + str(result))

    elif op == 5:
        print("Distribuicao Binomial")

        n = float(input("n (numero de repeticoes do experimento de bernoulli) = "))
        p = float(input("p (numero medio de sucessos) = "))
        x = float(input("x (numero de sucessos) = "))

        result = binomial_distribution(x, n, p)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 6:
        print("Distribuicao Poisson")

        x = float(input("x (numero de sucessos) = "))
        p = float(input("p (numero medio de sucessos) = "))

        result = poisson_distribution(x, p)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 7:
        print("Distribuicao Hipergeometrica")

        n = float(input("n (numero de repeticoes do experimento) = "))
        N = float(input("N (tamanho da populacao) = "))
        N1 = float(input("N1 (tamanho da sub-populacao de interesse) = "))
        x = float(input("x (variavel) = "))

        result = hypergeometric_distribution(x, n, N, N1)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 8:
        print("Normal Distribution Area - Table")

        x = float(input("z = "))
        area = round(normal_distribution_area(x), 5)
        print("Area(0, z)=" + str(area))

    else:
        print("Comando invalido!")
