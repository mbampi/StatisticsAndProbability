import math


@staticmethod
def variance_homogeneity_f(s1, s2):
    if s1 > s2:
        return s1 / s2
    else:
        return s2 / s1


@staticmethod
def variance_equality_q(n, var, var_hip):
    return ((n - 1) * var) / var_hip


@staticmethod
def proportion_z(prop, prop_hip, n):
    return (prop - prop_hip) / math.sqrt((prop_hip * (1 - prop_hip)) / n)


@staticmethod
def proportion_equality_z(p1, p2, n1, n2):
    return (p1 - p2) / math.sqrt((p1 * (1 - p1)) / n1 + (p2 * (1 - p2)) / n2)
