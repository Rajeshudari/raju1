num=input("enter the number")
try:    
        temp=int(num)
        rev=0
        num1=int(num)
        while(num1>0):
            r=num1%10
            rev=rev*10+r
            num1=num1//10
        if temp==rev:
            print("The number is a palindrome")
        else:
            print("The number is not a palindrome")
except ValueError:
    print("The input is not proper")
enter the numbersam
The input is not proper
