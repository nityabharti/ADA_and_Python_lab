# Write a function to find Duplicate values in the List

def findduplicate(mylist):
    dublicate=set([])
    # creating a set to store the dublicate value 
    for i in range(len(mylist)):
        # first pointer to traverse through list
        for j in range(len(mylist)):
            # first pointer to traverse through list
            if mylist[i]==mylist[j] and i!=j:
                #  Both value are equal and their index are not same 
                dublicate.add(mylist[i])
                # adding dublicate value to the set 

    return list(dublicate)



if __name__ == "__main__":
    mylist=[2,3,4,3,5,6,7,6,8,9]
    # list containing dublicate values
    print(f"Dublicate values in the list : {findduplicate(mylist)} ")