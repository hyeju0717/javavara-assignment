#제출

n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

line = ""
result = "-".join(line.split())
print(result)


s = input()
i,k = input().split()
if int(i)>=len(s):
    print("The number you gave is too large!")
else :
    print(s[:int(i)]+k+s[int(i)+1:])