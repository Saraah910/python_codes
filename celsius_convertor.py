'''	Write three functions that calculate the remainder of two integers by using: (a)the basic 
operators of +, -, * and / (why is // not required?)  (b)the divmod function(c)the % operator'''    

a=9
b=2
print('Remainder =',a%b)
print('Remainder =',a-b*(a//b))
print('Questient and Remainder are =',divmod (a,b))
