def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num

original_num = 69
reversed_num = reverse_number(original_num)
print(f"Original number: {original_num}")
print(f"Reversed number: {reversed_num}")