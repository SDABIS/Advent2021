import requests 

if __name__ == "__main__":
    f = open("2text.txt", "r")

    depth = 0
    forward = 0

    for x in f:
        splitted = x.split(" ")
        command = splitted[0]
        num = int(splitted[1])
        if command == "forward":
            forward += num
        elif command == "up":
            depth -= num
        elif command == "down":
            depth += num
        
    print(depth * forward)
        