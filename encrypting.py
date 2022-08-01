#!/usr/bin/env python3
import sys
import math

def len_key():
    len_k = len(sys.argv[2])
    if len_k <= 2:
       return len_k
    a = 2
    while (len_k / a) > a:
        a = a + 1
    return (a)

def display_matrix_key(M):
    print("Key matrix:")
    for i in range(len_key()):
        for j in range(len_key()):
            if (j + 1) != len_key():
                print(str(M[i][j]), end='\t')
            else:
                print(str(M[i][j]))
    print()

def matrix_key():
    len_k = (len_key())
    M = []
    n = 0
    for i in range (len_k):
        a = []
        for j in range (len_k):
            if n < len(sys.argv[2]):
                a.append(ord(sys.argv[2][n]))
            if n >= len(sys.argv[2]):
                a.append(0)
            n = n + 1
        M.append(a)
    return (M)

def matrix_str():
    M = []
    n = 0
    for i in range (int(len(sys.argv[1])/len_key()) + 1):
        a = []
        for j in range (len_key()):
            if n < len(sys.argv[1]):
                a.append(ord(sys.argv[1][n]))
            if n >= len(sys.argv[1]):
                a.append(0)
            n = n + 1
        M.append(a)
    return (M)

def matrix_product(M1, M2):
    z = 0
    my_str = ""
    M = []
    for i in range (int(len(sys.argv[1])/len_key()) + 1):
        a = []
        for j in range (len_key()):
                a.append(0)
        M.append(a)

    for j in range ((int(len(sys.argv[1])/len_key()) + 1)):
        for k in range (len_key()):
            for l in range (len_key()):
                M[j][k] += M2[j][l] * M1[l][k]
            if z == 0:
                my_str = my_str + str(M[j][k])
                z = z + 1
            else:
                my_str = my_str + " "
                my_str = my_str + str(M[j][k])
    display_matrix_key(matrix_key())
    print("Encrypted message:")
    print(my_str)
