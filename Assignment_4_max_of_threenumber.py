a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
def maximum(a,b,c):
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print("c is greater")
maximum(a,b,c)
enter a value12
enter b value45
enter c value89
c is greater
