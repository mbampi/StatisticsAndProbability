
import statistics
import matplotlib.pyplot as plt
import functions as ps

while True:
    print("\n --- Statistics and Probability --- \n")
    print(" 1- Media, Mediana, Moda e Desvio Padrao \n"
          " 2- Permutacao \n"
          " 3- Permutacao Circular \n"
          " 4- Combinacao \n"
          " 5- Distribuicao Binomial \n"
          " 6- Distribuicao Poisson \n"
          " 7- Distribuicao Hipergeometrica \n"
          " 8- Padronizar (X -> Z) \n"
          " 9- Normal Distribution Area \n"
          " 0- Sair \n")
    op = int(input(" -> "))

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

        result = ps.permutation(n, p)
        result = round(result, 4)
        print("P(" + str(n) + ", " + str(p) + ") = " + str(result))

    elif op == 3:
        print("Permutacao Circular - PC(n)")

        m = float(input("n (total) = "))

        result = ps.circular_permutation(n)
        result = round(result, 4)
        print("PC(" + str(n) + ") = " + str(result))

    elif op == 4:
        print("Combinacao - C(n, p)")

        m = float(input("n (total) = "))
        p = float(input("p (selecionados) = "))

        result = ps.combination(n, p)
        result = round(result, 4)
        print("C(" + str(n) + ", " + str(p) + ") = " + str(result))

    elif op == 5:
        print("Distribuicao Binomial")

        n = float(input("n (numero de repeticoes do experimento de bernoulli) = "))
        p = float(input("p (numero medio de sucessos) = "))
        x = float(input("x (numero de sucessos) = "))

        result = ps.binomial_distribution(x, n, p)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 6:
        print("Distribuicao Poisson")

        p = float(input("p (numero medio de sucessos) = "))
        x = float(input("x (numero de sucessos) = "))

        result = ps.poisson_distribution(x, p)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 7:
        print("Distribuicao Hipergeometrica")

        n = float(input("n (numero de repeticoes do experimento) = "))
        N = float(input("N (tamanho da populacao) = "))
        N1 = float(input("N1 (tamanho da sub-populacao de interesse) = "))
        x = float(input("x (variavel) = "))

        result = ps.hypergeometric_distribution(x, n, N, N1)
        result = round(result, 4)
        print(" = " + str(result))

    elif op == 8:
        print("Padronizar (X->Z)")

        x = float(input("x = "))
        mean = float(input("media = "))
        std = float(input("desvio padrao = "))

        z = round(ps.standardizing(x, mean, std), 5)
        print("z=" + str(z))

    elif op == 9:
        print("Normal Distribution Area - Table")

        z = float(input("z = "))
        area = round(ps.normal_distribution_area(z), 5)
        print("Area(0, z)=" + str(area))

    else:
        print("Comando invalido!")
