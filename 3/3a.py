import requests 

if __name__ == "__main__":
    f = open("3text.txt", "r")

    occurrence = []
    all_elements = f.read().splitlines()
    
    for ch in all_elements[0]:
        occurrence.append([0, 0])

    elem_length = len(all_elements[0])
    print(occurrence)
    
    for elem in all_elements:
        for i in range(len(elem)):
            ch = elem[i]
            if ch == '0':
                occurrence[i][0] += 1
            elif ch == '1':
                occurrence[i][1] += 1

    gamma = ''
    epsilon = ''
    for bit_occ in occurrence:
        if(bit_occ[0] > bit_occ[1]):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    gamma_value = int(gamma, 2)
    epsilon_value = int(epsilon, 2)
    
    print(gamma)
    print(epsilon)
    print(gamma_value * epsilon_value)
    