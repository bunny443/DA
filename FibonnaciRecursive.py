
COUNT = 0

def recur_fibo(n):
    global COUNT
    COUNT += 1

    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)


nterms = int(input("How many terms? "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Number of terms:", nterms)
    print("Fibonacci sequence:")

    for i in range(nterms):
        print(recur_fibo(i), end=" ")

    print("\nTotal steps required:", COUNT)
