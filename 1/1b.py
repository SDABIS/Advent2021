import requests 

if __name__ == "__main__":
    f = open("1text.txt", "r")

    lines = []
    for x in f:
        lines.append(int(x))

    count = 0
    prev = 9999999
    for i in range(len(lines) - 2):
        window = sum(lines[i:i+3])
        if(window > prev):
            count += 1
            print("{} > {}".format(window, prev))
        prev = window
    print(count)

        