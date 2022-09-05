"""
Write a function that returns all the permutations of the given string of length 3.
"""
import string


def permutaions(string: str):
    res = set()   #making empty set that stores the given string 
    for i in range(len(string)):
        for j in range(len(string)):
            if j == i:
                continue
            for k in range(len(string)):
                #if index j=k or i=k it will skip that arrangement and return others
                if j == k or i == k:
                    continue
                res.add(string[i]+string[j]+string[k])
    return list(res)


if __name__ == '__main__':
    string = input("Enter a 3 letter word: ")
    print(f"All permutations of the {string} are: ")
    print(permutaions(string)) #calling the function