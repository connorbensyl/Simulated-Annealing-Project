import numpy as np
#Connor Bensyl, CS461 Assignment 2
suites = np.empty(shape=(50, 4))
compatibility = np.empty(shape=(200, 200))
input = open("roommates.txt", 'r')
output = open("output.txt", 'a')

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
    return AB + AC + AD + BC + BD + CD


def get_comp_score(stuA, stuB):
    return int(compatibility[stuA][stuB])


def equation(swappedScore, unswappedScore):
    return np.e**((unswappedScore-swappedScore)/T)



attempted = 0
accepted = 0
iterations = 0
prob1 = 0
prob2 = 0
while True:
    iterations += 1

    variation = np.random.randint(0, 2)  # Changes to apply: Choose randomly (uniformly) between two possible variations
    if variation == 0:  # Select 2 rooms at random, and 1 student at random from each room; exchange them.
        room1 = np.random.randint(0, 50)
        room2 = np.random.randint(0, 50)
        stu1 = np.random.randint(0, 4)
        stu2 = np.random.randint(0, 4)
        comp1_before = get_fitness(room1)
        comp2_before = get_fitness(room2)
        swap(room1, stu1, room2, stu2)
        comp1_after = get_fitness(room1)
        comp2_after = get_fitness(room2)

        if comp1_before > comp1_after and comp2_before > comp2_after:
            accepted += 1

        else:

            swap(room1, stu1, room2, stu2)  # if the fitness is worse after the swap then reverse it
            attempted += 1

    elif variation == 1:  # Select 2 rooms at random; swap the first 2 students in one room with the last 2 students
        # in the other.
        room1 = np.random.randint(0, 50)
        room2 = np.random.randint(0, 50)
        comp1_before = get_fitness(room1)
        comp2_before = get_fitness(room2)
        swap(room1, 0, room2, 2)
        swap(room1, 1, room2, 3)
        comp1_after = get_fitness(room1)
        comp2_after = get_fitness(room2)
        if comp1_before > comp1_after and comp2_before > comp2_after:
            accepted += 1


        else:
            swap(room1, 0, room2, 2)
            swap(room1, 1, room2, 3)  # if the fitness is worse after the swap then reverse it
            attempted += 1

    if attempted >= 20000 or accepted >= 2000:
        T -= 0.05
        attempted = 0
        accepted = 0
        continue
    elif attempted >= 20000 and accepted == 0 or iterations >= 10000000:#stop after 1 million iterations
        break

# now produce output file
output.write("#####FINAL RESULTS#####")
best = 600
worst = 0
sum = 0
for i in range(50):
    if get_fitness(i) < best:
        best = get_fitness(i)
    if get_fitness(i) > worst:
        worst = get_fitness(i)
    sum += get_fitness(i)

best_output = "Best score: ", best
worst_output = "Worst score: ", worst
output.write(str(best_output))
output.write(str(worst_output))
avg = "Average score: ", sum / 50
output.write(str(avg))
output.write("Cooling schedule: decrease by 0.05 after every 20k attempted swaps or 2000 accepted swaps. Initial "
             "value for T 0.95")
output.write("room assignments:")
output.write(str(suites))
