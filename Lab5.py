# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n <= 0:
        return None

    result = ""
    row = 0
    
    while row < n:
        if row == 0 or row == n - 1:
            result += "*" * n
        else: 
            result += "*" + " " * (n - 2) + "*" if n > 1 else "*"
        if row < n - 1:
            result += "\n"

        row += 1
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