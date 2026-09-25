from collections import deque
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
max_dq = deque()
min_dq = deque()
left = 0
best_length = 0
best_start = 1
for right in range(n):
  while max_dq and arr[max_dq[-1]] <= arr[right]:
    max_dq.pop()
  max_dq.append(right)
  while min_dq and arr[min_dq[-1]] >= arr[right]:
    min_dq.pop()
  min_dq.append(right)
  while arr[max_dq[0]] - arr[min_dq[0]]>k:
    if max_dq[0] == left:
      max_dq.popleft()
    if min_dq[0] == left:
      min_dq.popleft()
    left+=1
  length = right - left + 1
  if length > best_length:
    best_length = length
    best_start = left+1
print(best_length, best_start)