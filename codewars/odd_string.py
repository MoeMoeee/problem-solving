def solve(m, s):
    total_sum = 0
    for string in s:
        string_sum = 1
        for char in string:
            ascii_value = ord(char)
            string_sum *= ascii_value ** m
        total_sum += string_sum
    print(total_sum)
    if total_sum % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    m =  2
    s = ['abc', 'bd']
    print(solve(m,s))