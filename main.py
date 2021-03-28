import numpy as np

suites = np.empty(shape=(50, 4))
compatibility = np.empty(shape=(200, 200))
input = open("roommates.txt", 'r')
output = open("output.txt", 'w')
np.set_printoptions(threshold=np.inf)
suite = 0
slot = 0
student = 0
while suite < 50 and student < 200:  # iterate through each suite, arbitrarily populating with students

    while slot < 4:  # iterate through slots in suite
        suites[suite][slot] = student
        student += 1
        slot += 1
    slot = 0
    suite += 1

x = 0
y = 0

line = input.readline().split(' ')
while x < 200 and line != '':
    while y < 200:
        compatibility[x][y] = line[y]
        y += 1
    y = 0
    x += 1
    line = input.readline().split(' ')

T = 0.95


def swap(a1, a2, b1, b2):
    temp = suites[a1][a2]
    suites[a1][a2] = suites[b1][b2]
    suites[b1][b2] = temp

def get_fitness(suite):
    A = int(suites[suite][0])
    B = int(suites[suite][1])
    C = int(suites[suite][2])
    D = int(suites[suite][3])
    AB = compatibility[A][B]
    AC = compatibility[A][C]
    AD = compatibility[A][D]
    BC = compatibility[B][C]
    BD = compatibility[B][D]
    CD = compatibility[C][D]
    return AB+AC+AD+BC+BD+CD

def get_comp_score(stuA, stuB):
    return int(compatibility[stuA][stuB])











