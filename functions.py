
import math
from scipy.integrate import quad
import functions as ps


def mean(x_list, p_list=None):
    total_sum = 0
    if p_list is None:
        for x in x_list:
            total_sum += x
        result = total_sum / len(x_list)

    else:
        result = 0
        for x, p in zip(x_list, p_list):
            result += x*p

    return result


def mode(x_list):
    rep_dict = {i: 0 for i in x_list}

    for x in x_list:
        rep_dict[x] += 1

    if all(value == 1 for value in rep_dict.values()):
        return None
    else:
        return max(rep_dict, key=rep_dict.get)


def median(x_list):
    list_size = len(x_list)
    x_list.sort()
    print(list_size)
    if list_size % 2 == 0:
        result = (x_list[int(list_size/2)] + x_list[int((list_size/2)-1)])/2
    else:
        result = x_list[int((list_size-1)/2)]

    return result


def variation(x_list, p_list=None):
    list_size = len(x_list)
    m = ps.mean(x_list, p_list)
    total = 0
    if p_list is None:
        for x in x_list:
            total += (x - m) ** 2
        result = total / (list_size-1)

    else:
        for i, x in enumerate(x_list):
            total += (x ** 2) * p_list[i]
        result = (total / list_size) - (m ** 2)

    return result


def standard_deviation(x_list, p_list=None):
    return math.sqrt(variation(x_list, p_list))


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


def hypergeometric_distribution(x, n, N, N1):
    N2 = float(N - N1)
    return (combination(N1, x) * combination(N2, float(n - x))) / combination(N, n)


def standardizing(x, mean, std):
    return (x-mean)/std


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


def sampling_distribution(x_list, p_list):
    new_x_list = []
    new_x_mean_list = []
    new_p_list = []

    for p1, x1 in zip(p_list, x_list):
        for p2, x2 in zip(p_list, x_list):
            new_x_list.append(str(x1 + ", " + x2))
            new_x_mean_list.append(float((x1 + x2)/2))
            new_p_list.append(float(p1*p2))

    return new_x_list, new_x_mean_list, new_p_list
