#!/usr/bin/env python3
import sys
import math
import encrypting

def matrix_determinant():
    m = encrypting.matrix_key()
    if encrypting.len_key() == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    if encrypting.len_key() == 3:
        coef1 = 1*(m[0][0]*((m[1][1]*m[2][2])-(m[1][2]*m[2][1])))
        coef2 = -1*(m[0][1]*((m[1][0]*m[2][2])-(m[1][2]*m[2][0])))
        coef3 = 1*(m[0][2]*((m[1][0]*m[2][1])-(m[1][1]*m[2][0])))
        determinant = coef1 + coef2 + coef3
        return determinant

def transpose_matrix(m):
    MT = [[m[0][0], m[1][0], m[2][0]], [m[0][1], m[1][1], m[2][1]], [m[0][2], m[1][2], m[2][2]]]
    return MT

def adjoint_matrix(MT):
    a = 1*((MT[1][1]*MT[2][2]) - (MT[1][2]*MT[2][1]))
    b = -1*((MT[1][0]*MT[2][2]) - (MT[1][2]*MT[2][0]))
    c = 1*((MT[1][0]*MT[2][1]) - (MT[1][1]*MT[2][0]))
    d = -1*((MT[0][1]*MT[2][2]) - (MT[0][2]*MT[2][1]))
    e = 1*((MT[0][0]*MT[2][2]) - (MT[0][2]*MT[2][0]))
    f = -1*((MT[0][0]*MT[2][1]) - (MT[0][1]*MT[2][0]))
    g = 1*((MT[0][1]*MT[1][2]) - (MT[0][2]*MT[1][1]))
    h = -1*((MT[0][0]*MT[1][2]) - (MT[0][2]*MT[1][0]))
    i = 1*((MT[0][0]*MT[1][1]) - (MT[0][1]*MT[1][0]))
    MA = [[a, b, c], [d, e, f], [g, h, i]]
    return MA

def matrix_inverse():
    m = encrypting.matrix_key()
    determinant = matrix_determinant()
    if determinant == 0:
        return m
    if encrypting.len_key() == 2:
        M2 = [[m[1][1] / determinant, -1 * m[0][1] / determinant], [-1 * m[1][0] / determinant, m[0][0] / determinant]]
        return M2
    if encrypting.len_key() == 3:
        MT = transpose_matrix(m)
        MA = adjoint_matrix(MT)
        M3 = []
        for i in range (encrypting.len_key()):
            a = []
            for j in range (encrypting.len_key()):
                a.append((1/determinant) * MA[i][j])
            M3.append(a)
        return M3

def matrix_decrypt_str():
    M = []
    n = 0
    nbr_list = [int(s) for s in sys.argv[1].split() if s.isdigit()]
    len_str = len(nbr_list)
    for i in range (int(len_str/encrypting.len_key())):
        a = []
        for j in range (encrypting.len_key()):
            if n < len_str:
                a.append(nbr_list[n])
            if n >= len_str:
                a.append(0)
            n = n + 1
        M.append(a)
    return (M)

def matrix_quotient(M1, M2):
    z = 0
    my_str = ""
    nbr_list = [int(s) for s in sys.argv[1].split() if s.isdigit()]
    len_str = len(nbr_list)
    M = []
    for i in range (int(len_str/encrypting.len_key())):
        a = []
        for j in range (encrypting.len_key()):
            a.append(0)
        M.append(a)
    for j in range (int(len_str/encrypting.len_key())):
        for k in range (encrypting.len_key()):
            for l in range (encrypting.len_key()):
                M[j][k] += M2[j][l] * M1[l][k]
            if (round(M[j][k]) > 31) & (round(M[j][k]) < 127):
                my_str = my_str + chr(round(M[j][k]))
    encrypting.display_matrix_key(matrix_inverse())
    print("Decrypted message:")
    print(my_str)
    return
