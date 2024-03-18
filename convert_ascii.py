code = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73,
        73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for i in code:
    code = chr(i)
    print(code, end="")

text = "crypto{ASCII_pr1nt4bl3}"
ascii_list = []

for ch in text:
    text = ord(ch)
    ascii_list.append(text)
print(ascii_list)
