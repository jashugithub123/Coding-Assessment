n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
i = 0
j = 0
carry = 0
result = []
while i<n or j<m or carry:
  x = a[i] if i<n else 0
  y = b[j] if j<m else 0
  total = x+y+carry
  result.append(total%10)
  carry = total//10
  i+=1
  j+=1
print(*result)