def sum67(nums):
  total = 0
  i=0
  while i < len(nums):
    if nums[i] == 6:
      while nums[i] != 7:
        i+=1
      i+=1
    if i<len(nums) and nums[i]!=6:
      total+=nums[i]
      i+=1
  return total