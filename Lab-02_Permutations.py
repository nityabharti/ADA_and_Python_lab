import string


def permutaions(string: str):
    res = set()
    for i in range(len(string)):
        for j in range(len(string)):
            if j == i:
                continue
            for k in range(len(string)):
                if j == k or i == k:
                    continue
                res.add(string[i]+string[j]+string[k])
    return list(res)


if __name__ == '__main__':
    string = input("Enter a 3 letter word: ")
    print(f"All permutations of the {string} are: ")
    print(permutaions(string))