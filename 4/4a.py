import requests 
import numpy as np

if __name__ == "__main__":
    f = open("4text.txt", "r")

    nums = f.readline()[:-1].split(",")
    
    cartons_full = [x for x in f.read().splitlines() if x != '']
    print(len(cartons_full))
    cartons = []
    marked = []
    for i in range(0, len(cartons_full), 5):
        newcarton = [cartons_full[i + x].split() for x in range(5)]
        print(newcarton)
        newmarked = np.zeros((5, 5), "int32")
        print(newmarked)
        cartons.append(newcarton)
        marked.append(newmarked)

    winner_crt = False
    winner_mrk = False
    for num in nums:
        for c in range(len(cartons)):
            crt = cartons[c]
            mrk = marked[c]

            for i in range(len(crt)):
                row = crt[i]
                for j in range(len(row)):
                    if row[j] == num:
                        mrk[i][j] = 1
                        print("HIT: Number {} is on Carton {} on the position ({},{})".format(num, c, i, j))
                        print(mrk)

                        if ((0 not in mrk[i]) or (0 not in mrk[:][j])):
                            print("WINNER")
                            winner_crt = crt
                            winner_mrk = mrk

        if (winner_crt != False):
            print("AAAAAAAAAAAAAA")
            break
    

    sum_of_unmarked = 0
    for i in range(len(winner_crt)):
        row = winner_crt[i]
        for j in range(len(row)):
            if winner_mrk[i][j] == 0:
                sum_of_unmarked += int(row[j])


    print(sum_of_unmarked * int(num))

