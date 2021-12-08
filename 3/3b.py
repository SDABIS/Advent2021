import requests 

def iterate_list(all_list, choice):
    lst = all_list.copy()
    elem_length = len(all_elements[0])
    all_zeros = [0] * elem_length
    print(all_zeros)
    for i in range(elem_length):
        plus_zeros = 0
        for elem in lst:
            ch = elem[i]
            if ch == '0':
                plus_zeros += 1
            elif ch == '1':
                plus_zeros -= 1
    
        if plus_zeros > 0:
            keep = str(0 ^ choice)
        else:
            keep = str(1 ^ choice)

        print(keep)
        lst[:] = [x for x in lst if (x[i] == str(keep))]
        if len(lst) == 1: break

    return lst[0]

if __name__ == "__main__":
    f = open("3text.txt", "r")

    all_elements = f.read().splitlines()

    oxy_str = iterate_list(all_elements, 0)
    co2_str = iterate_list(all_elements, 1)

    print(oxy_str)
    print(co2_str)
    oxy = int(oxy_str, 2)
    co2 = int(co2_str, 2)
    
    print(oxy * co2)