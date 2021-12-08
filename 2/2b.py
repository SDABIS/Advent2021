import requests 

if __name__ == "__main__":
    f = open("2text.txt", "r")

    depth = 0
    forward = 0
    aim = 0

    for x in f:
        splitted = x.split(" ")
        command = splitted[0]
        num = int(splitted[1])
        if command == "forward":
            forward += num
            depth += aim * num
        elif command == "up":
            aim -= num
        elif command == "down":
            aim += num
        
    print(depth * forward)
        