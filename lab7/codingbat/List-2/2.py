def big_diff(nums):
  maxi= -9999999
  mini= 9999999
  for i in range(len(nums)):
    if nums[i] > maxi:
      maxi = nums[i]
  for i in range(len(nums)):
    if nums[i] < mini:
      mini = nums[i]
  return maxi - mini
