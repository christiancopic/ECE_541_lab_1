from matplotlib import pyplot as plt

def main():
    #Eliminate semicolons at end of rows
    with open("lab1s2m3.txt", 'r') as f:
        data = f.read()
        data = data.replace(";", "")
    f.close()

    #split data in rows/columns
    x = [[float(c) for c in r.split()] \
     for r in data.strip().split('\n')]
    
    #x[row][col]
    #columns: index, time, reference, position, uselses, useless
    #We want tPeak, peakPos, and yFV.

    pos = []
    time = []

    for r in (x):
        pos.append(r[3])
        time.append(r[1])
    
    plt.plot(time,pos)
    plt.show()
    print("Max value: " + str(max(pos)))
    print("tPeak: "+ str((x[pos.index(max(pos))][1])))
    print("yFV:" + str(x[time.index(2.754)][3]))


if __name__ == '__main__':
    main()