def max_parwise_product(numbers):
    numbers.sort()
    max_product = numbers[-1] * numbers[-2]
    
    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_parwise_product(input_numbers))
    