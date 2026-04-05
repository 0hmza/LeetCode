def convert_base(number_str, source_base, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = int(number_str, source_base)
    j = 1
    if n == 0:
        return "0"
    if n < 0:
        n = n * (-1)
        j = 0
    r = ""
    while n != 0:
        r += str(digits[n % target_base])
        n //= target_base
    if j == 0:
        return "-" + r[::-1]
    elif j == 1:
        return r[::-1]


print(convert_base("-1010", 2, 10))