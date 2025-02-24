# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
        # pattern = [1 , 0 , 0 , 0 , 1 ]
    result = ""
    
    count = [1/n , 0/n , 0/n , 0/n , 1/n]
    while count == 1:
        for i in range(n,n + 1):
            for j in range(n,n + 1):
                result += "*"
            print("*****", end=" ")
        result += "\n"
    while count == 0:
        for i in range(n,n + 1):
            for j in range(n,n + 1):
                result += "*   *"
            print("*   *", end=" ")
        result += "\n"
    return result

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result: ""
    count = 1
    while count <= 1:
        print(count)
        count += 1
        result += "\n"
    return ""

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return ""

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""