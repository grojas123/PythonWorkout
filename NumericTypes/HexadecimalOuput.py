def hex_output():
    decnumber = 0
    hexnum = input('Enter the hexadecimal')
    for power, digit in enumerate(reversed(hexnum)):
        decnumber += int(digit, 16) * (16 ** power)
        print(decnumber)
hex_output()


