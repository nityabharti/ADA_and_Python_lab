"""
Write a function which return all the unique palindromes from a given string.
"""
def expand(s, left, right):
    len_s = len(s)
    while left >= 0 and right < len_s and s[left] == s[right]:
        left -= 1
        right += 1
    return left+1, right-1


def get_unique_palindromes(s):
    len_s = len(s)
    result = []
    for i in range(len_s):
        l1, r1 = expand(s, i, i)
        l2, r2 = expand(s, i, i+1)

        if l1 != r1:
            result.append(s[l1:r1+1])
        if l2 < r2:
            result.append(s[l2:r2+1])
    return result


if __name__ == '__main__':
    string = input("Enter a Word: ")
    print(f"All unique palindromes are :{get_unique_palindromes(string)}")