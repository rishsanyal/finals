from collections import Counter
import sys, pdb, csv, pdb, math
import matplotlib.pyplot as plt
import numpy as np

D = Counter()

def main():
    partOne()


def partOne():
    i = 0
    with open("/Users/rsanyal/Documents/Books/Spring 17/STA 141C/final/orders.csv") as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if i < 500 and row[1] != "user_id":
                D[row[1]] += 1
                i += 1


    lens = np.arange(len(D))
    plt.bar(lens, D.values(),width=0.3, align='center',alpha = 0.2)
    plt.xticks(lens, D.keys())
    plt.show()

main()
