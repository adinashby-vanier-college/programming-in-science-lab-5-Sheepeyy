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
    i = 1
    result = ""

    while i <= n:
        j = 1
        line = ""

        while j <= i:
            line += str(j)
            j += 1

        result += line + "\n"
        i += 1
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    counter = 1

    while counter <= n:
        total += counter
        counter += 1

    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    i = 1
    
    while i <= n:
        space = " " * (n - i)
        stars = "*" * (2 * i - 1)
        result += str(space + stars).rstrip() + "\n"
        i += 1
    return result.rstrip()