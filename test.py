import numpy as np

a = [[1, 2, 3], 
     [1, 2, 3], 
     [1, 2, 3]]

b = [[1, 2, 3], 
     [1, 2, 3], 
     [1, 2, 3]]

c = [[], [], []]



for ligne in range(len(a)):
    for colonne in range(len(b)):
        res_postition_matrice = 0
        for calcul in range(len(b)):
            res_postition_matrice += a[ligne][calcul] * b[calcul][colonne]
        c[ligne].append(res_postition_matrice)

# print(c)




def suite(n):
    un = 1
    for i in range(n+1):
        un = 0.5 * un + i - 1
        print(f"Un à l'index {i} donne : {un}")
    return un


def tristan_suite(n):
    un = 1
    s = un
    for i in range(n):
        un = 0.5*un +i -1
        s += un
        print(f"index : {i}, result : {s}")
    return s

def somme(n):
    u = 1          # u_0 = 1
    s = u
    print(u)
    for k in range(1, n+1):
        u = 0.5 * u + k - 1   # u_{k+1}
        s += u
        print(f"index : {k}, result : {s}")
    return s


#g(x) = 2x**3 − 1 + 2 ln x

def g(x):
    return 2*x**3 - 1 + 2*np.log(x)

from math import log

def g(x):
    return 2*x**3 - 1 + 2*log(x)

def dichotomie():
    a, b = 0.5, 1.0
    while b - a >= 1e-4:
        m = (a + b) / 2
        if g(m) < 0:
            a = m
        else:
            b = m
    return (a + b) / 2

print(dichotomie())  # ≈ 0.7729



"""
print(tristan_suite(5))
print(suite(5))
print(somme(5))"""

print(g(5))