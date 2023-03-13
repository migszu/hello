import time

n = 100000

def for_sum(n):
  sum = 0
  for i in range(1, n+1):
    sum = sum + i
  return sum

def while_sum(n):
  sum = 0
  i = 1
  while i <= n:
    sum = sum + i
    i = i + 1
  return sum

start = time.time()
result = for_sum(n)
end = time.time()
print(f"Sum of numbers from 1 to {n} using for loop is {result}")
print(f"Execution time of for_sum function is {end - start} seconds\n")

start = time.time()
result = while_sum(n)
end = time.time()
print(f"Sum of numbers from 1 to {n} using while loop is {result}")
print(f"Execution time of while_sum function is {end - start} seconds\n")