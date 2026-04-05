def robust_convert_base(number_str, from_base, to_base):
    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    n = int(number_str, from_base)
    if n == 0:
        return "0"
    r = ""
    while n != 0:
        r += str(digit[n % to_base])
        n //= to_base
    return r[::-1]


print(robust_convert_base("1010", 2, 16))
# "A"
print(robust_convert_base("17", 8, 10))
# "15"
print(robust_convert_base("123", 7, 13))
# "51"