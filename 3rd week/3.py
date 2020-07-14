#1
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


#2
x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

#3
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')