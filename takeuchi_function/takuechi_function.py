count = 0

def T(x,y,z):
    if x<= y:
        return y
    else:
        global count 
        count+= 1
        return T(T(x-1,y,z),T(y-1,z,x),T(z-1,x,y))

def U(n):
    T(n,0,n+1)

def solve(n):
    global count
    count= 0
    U(n)
    digits = str(count)
    total = 0
    for digit in digits:
        total += int(digit)
    return total

print(solve(5))
print(solve(10))
print(solve(20))
print(solve(30))
print(solve(50))
print(solve(99))
print(solve(140))
print(solve(150))