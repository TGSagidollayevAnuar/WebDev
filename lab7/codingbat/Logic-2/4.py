def no_teen_sum(a, b, c):
  s = 0
  def fix_teen(n):
    if n>=13 and n<=19 and n!=15 and n!=16:
      return 0
    return n
  arr = [a, b, c]
  for i in range(0,3,1):
    s = s + fix_teen(arr[i])
  return s