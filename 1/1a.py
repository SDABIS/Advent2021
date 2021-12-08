import requests 

if __name__ == "__main__":
    f = open("1text.txt", "r")
    prev = 0
    count = 0
    for x in f:
        if int(x) > prev:
            count += 1
            print("{} > {}".format(int(x), prev))
        prev = int(x)
    print(count)
        