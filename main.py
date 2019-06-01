import matplotlib.pyplot as plt
import functions as ps
import pandas as pd


while True:
    print("\n --- Statistics and Probability --- \n")
    print(" 1- Media, Mediana, Moda, Variacao e Desvio Padrao \n"
          " 2- Permutacao \n"
          " 3- Permutacao Circular \n"
          " 4- Combinacao \n"
          " 5- Distribuicao Binomial \n"
          " 6- Distribuicao Poisson \n"
          " 7- Distribuicao Hipergeometrica \n"
          " 8- Padronizar (x->z) \n"
          " 9- Area da Distribuicao Normal (0,z) \n"
          " 10- z a partir da Area da Distribuicao Normal (%->z)\n"
          " 11- Area da Distribuicao t de Student (limites bilaterais) \n"
          " 12- Distribuicao Amostral (Media, Variacao e Desvio Padrao) \n"
          " 13- Intervalo de Confianca para Media (z) \n"
          " 14- Intervalo de Confianca para Media (t) (TODO) \n"
          " 0- Sair \n")
    op = int(input(" -> "))

    if op == 0:
        break

    elif op == 1:
        print("Media, Mediana, Moda, Variacao e Desvio Padrao")
        s = input("Numeros [divididos por ',' (virgula)] = ")
        x_list = s.split(',')
        for index, item in enumerate(x_list):
            x_list[index] = float(item)

        print(x_list)
        smallest = min(x_list)
        biggest = max(x_list)
        mean = ps.mean(x_list)
        mode = ps.mode(x_list)
        median = ps.median(x_list)
        var = ps.variation(x_list)
        std_deviation = ps.standard_deviation(x_list)

        print("Maior = " + str(biggest))
        print("Menor = " + str(smallest))
        print("Media = " + str(round(mean, 4)))
        print("Mediana = " + str(median))
        print("Moda = " + str(mode))
        print("Variacao= " + str(round(var, 4)))
        print("Desvio Padrao= " + str(round(std_deviation, 4)))

        x_list.sort()
        x_range = (x_list[0] - 1, x_list[len(x_list) - 1] + 1)
        plt.hist(x_list, color='blue', range=x_range, histtype='bar', rwidth=0.8)
        plt.xlabel("Dados")
        plt.ylabel("No. de ocorrencias")
        plt.show()

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

        n = float(input("n (total) = "))
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
        print("Area da Distribuicao Normal (tabela)")

        z = float(input("z = "))
        area = round(ps.normal_distribution_area(z), 5)
        print("Area(0, z)=" + str(area))

    elif op == 10:
        print("Z a partir da Area da Distribuicao Normal (tabela)")

        area = float(input("area = "))
        z = round(ps.z_from_area(area), 2)

        print("Z = " + str(z))

    elif op == 11:
        print("Limites da distribuicao t de Student - (limites bilaterais)")

        alpha = float(input("alpha = "))
        v = float(input("v = "))
        area = ps.student_distribution_area(alpha/2, v)
        print("Area= " + str(round(area, 3)))

    elif op == 12:
        print("\n Distribuicao Amostral")
        x_raw = input("X [divididos por ',' (virgula)] = ")
        p_raw = input("P [divididos por ',' (virgula)] = ")
        x_list = x_raw.split(',')
        p_list = p_raw.split(',')
        for i, x in enumerate(x_list):
            x_list[i] = float(x)
            p_list[i] = float(p_list[i])

        sampling_x, sampling_x_means, sampling_p = ps.sampling_distribution(x_list, p_list)
        mean = ps.mean(sampling_x_means, sampling_p)/2
        var = ps.variation(sampling_x_means, sampling_p)
        std = ps.standard_deviation(sampling_x_means, sampling_p)

        data = {'X': sampling_x, 'X Media': sampling_x_means, 'P': sampling_p}
        table = pd.DataFrame(data)
        print("\n" + table)
        print("Media= " + round(mean, 4))
        print("Variacao= " + round(var, 4))
        print("Desvio Padrao= " + round(std, 4))

    elif op == 13:
        print("Intervalo de Confianca para Media (z)")

        n = float(input("tamanho da amostra = "))
        mean = float(input("media = "))
        std = float(input("desvio padrao = "))
        confidence = float(input("nivel de confianca % = "))
        confidence = confidence / 100
        result = ps.mean_confidence_interval_z(n, std, confidence)

        print("Intervalo de Confianca= " + str(mean) + " +- " + str(round(result, 4)))

    elif op == 14:
        print("Intervalo de Confianca para Media (t)")

        n = float(input("tamanho da amostra = "))
        mean = float(input("media = "))
        s = float(input("desvio padrao = "))
        confidence = float(input("nivel de confianca % = "))
        confidence = confidence/100
        result = ps.mean_confidence_interval_t(n, s, confidence)

        print("Intervalo de Confianca= " + mean + "+-" + str(round(result, 4)))

    else:
        print("\n Comando invalido!")

