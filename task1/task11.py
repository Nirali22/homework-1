def fib(n):
    while(n>0):
        if n<=2:
            return 1
        else:
            return fib(n-1)+fib(n-2)
