import math
from scipy.integrate import quad


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
