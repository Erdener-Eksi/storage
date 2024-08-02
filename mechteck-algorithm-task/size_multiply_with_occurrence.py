'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t, z):
    def count_occurrences(sub, z):
        count = 0
        start = 0
        while True:
            start = z.find(sub, start)
            if start == -1:
                break
            count += 1
            start += len(sub)
        return count

    max_value = 0
    n = len(t)

    # Generate all substrings of `t`
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = t[i:j]
            count = count_occurrences(substring, z)
            value = len(substring) * count
            max_value = max(max_value, value)

    return max_value


# test
if __name__ == '__main__':
    result = find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print(result)
