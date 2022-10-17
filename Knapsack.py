
def knapsack(W_bag,s_a):
    a=sorted(s_a,key=lambda i:i[1],reverse=True)
    result=0
    for item in a:
        if item[0]<=W_bag:
            W_bag=W_bag-item[0]
            result=result+item[1]
    return (result)    


W_bag=int(input("Enter the bag size:"))
wt_item=input("Enter the weight of the items:").split()
wt_item=[int(item) for item in wt_item]
val_item=input("Enter the value of the item:").split()
val_item=[int(item) for item in val_item]
s_a=[[wt_item[i],val_item[i]] for i in range(3)]
print (s_a)
print(knapsack(W_bag,s_a))