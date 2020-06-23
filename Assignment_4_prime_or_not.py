a=int(input("enter a value"))
def prime(a):
    for i in range(2,a):
        if a%i==0:
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")
prime(a)
enter a value97
97 is a prime number
