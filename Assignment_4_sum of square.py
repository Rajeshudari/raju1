n=int(input("enter n value"))
def sum_of_squares(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i**2
    print(sum)  
sum_of_squares(n)
enter n value5
55
