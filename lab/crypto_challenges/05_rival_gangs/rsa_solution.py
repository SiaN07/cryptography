from rsa import solution

def rsa_crpto(chars):
    char_list = []
    char_list2 = []
    for i in chars:
        char_list.append(i)
    length = len(chars)

    int_list1 = [int(i) for i in char_list]
    print(int_list1)

    for i in range(0, length-1, 2):
        char_list2.append(char_list[i] + char_list[i+1])

    int_list = [int(i) for i in char_list2]
    print(int_list)

    for i in int_list:
        int_list = chr(i)
        print(int_list, end="")

sol = solution()
print(sol)
rsa_crpto(sol)
