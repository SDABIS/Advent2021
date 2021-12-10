import requests 
import numpy as np

if __name__ == "__main__":
    f = open("4text.txt", "r")

    nums = f.readline()[:-1].split(",")
    
    cartons_full = [x for x in f.read().splitlines() if x != '']
    cartons = []
    marked = []
    for i in range(0, len(cartons_full), 5):
        newcarton = [cartons_full[i + x].split() for x in range(5)]
        newmarked = np.zeros((5, 5), "int32")
        cartons.append(newcarton)
        marked.append(newmarked)

    loser_crt = False
    loser_mrk = False
    for num in nums:
        won = []
        for c in range(len(cartons)):

            crt = cartons[c]
            mrk = marked[c]

            for i in range(len(crt)):
                row = crt[i]
                for j in range(len(row)):
                    if row[j] == num:
                        mrk[i][j] = 1
                        if ((0 not in mrk[i]) or (0 not in mrk[:, j])):
                            print("WINNER: {}".format(c))
                            won.append(c)
                            if(len(cartons) == 1):
                                loser_crt = crt
                                loser_mrk = mrk
        if (loser_crt != False):
            print("AAAAAAAAAAAAAA")
            break

        print(len(cartons))
        cartons = [cartons[x] for x in range(len(cartons)) if x not in won]
        marked = [marked[x] for x in range(len(marked)) if x not in won]
        if len(cartons) < 2:
            for mrk in marked:
                print(mrk[:, 2])
                print(mrk)

    sum_of_unmarked = 0
    for i in range(len(loser_crt)):
        row = loser_crt[i]
        for j in range(len(row)):
            if loser_mrk[i][j] == 0:
                sum_of_unmarked += int(row[j])


    print(sum_of_unmarked * int(num))

