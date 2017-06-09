from collections import Counter
import sys, pdb, csv, pdb, math
import matplotlib.pyplot as plt
import numpy as np

D = Counter()

def main():
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

    # xs= zip(D.keys())
    # ys = D.values()

    # display
    # plt.figure(figsize=(10,8))
    # plt.title('Scatter Plot', fontsize=20)
    # plt.xlabel('x', fontsize=15)
    # plt.ylabel('y', fontsize=15)
    # plt.scatter(xs, ys, marker = 'o')
    # for label, x, y in zip(labels, xs, ys):
    #     plt.annotate(label, xy = (x, y))


main()
