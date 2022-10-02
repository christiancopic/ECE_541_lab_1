from matplotlib import pyplot as plt
import os

def main():
    #Eliminate semicolons at end of rows
    with open(os.getcwd() + "/Lab_data/lab1s2m3.txt", 'r') as f:
        data = f.read()
        data = data.replace(";", "")
    f.close()

    #split data into rows/columns
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

    #test
    
    maxVal = str(max(pos))
    tPeak = str(round((x[pos.index(max(pos))][1]) - 6, 3))
    yFV = str(x[time.index(2.754)][3])

    print("Max value: " + maxVal)
    print("tPeak: "+ tPeak)
    print("yFV:" + yFV)

    plt.plot(time,pos)
    plt.text(15, 2500,"Max: " + maxVal + "\ntPeak: " + tPeak + "\nyFV: " + yFV)
    plt.ylabel("Position")
    plt.xlabel("Time (s)")
    plt.title("Mass-Spring-Damper System Repsonse")
    plt.show()



if __name__ == '__main__':
    main()