## create a function for the two numbers
def add_two(first_number, second_number):
    return first_number + second_number

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(add_two(a,b))