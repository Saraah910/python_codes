def string(a):
    l1 =['upper']
    l2 =['lower']
    for i in a:
        if i.isupper():
            l1+=1
        elif i.islower():
            l2+=1

        print("Original string:",a)
        print("Upper case char:",l1)
        print("Lower case char:",l2)
        
string("How you like THAT")

