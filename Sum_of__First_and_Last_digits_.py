n = int(input())
sum_ = n%10
while n > 10:
  n  = n//10
sum_ = sum_+n;
print(sum_)