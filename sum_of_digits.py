def sum_of_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_of_digits(num // 10)
    
print(sum_of_digits(788))
# the last number is beging added until the number becomes zero
