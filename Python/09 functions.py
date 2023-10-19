def isgreater(a,b):
    if(a>b):
        print("a is greater")
        return a
    else:
        # print("b is greater")
        return b
        return a
    
# when return statements are given firstreturn statement is considered rest all are ignored

c=isgreater(9,10)
print(c,"Only b is considered in return")