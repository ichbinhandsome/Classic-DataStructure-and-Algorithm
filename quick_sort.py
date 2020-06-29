
#frist method
def quicksort(nums,left,right):
    if left >= right:
        return 
    standard = nums[left]
    i = left
    j = right
    while i < j:
        while i < j:
            if nums[j] < standard:
                nums[i] = nums[j]
                break
            else:
                j -= 1
        while i < j:
            if nums[i] > standard:
                nums[j] = nums[i]
                break
            else:
                i += 1
    nums[i] = standard
    quicksort(nums,left,i-1)
    quicksort(nums,i+1,right)
#second method
def quicksort_2(nums,left,right):
    if left >= right:
        return 
    standard = nums[left]
    i = left
    j = right
    while i < j:
        while i < j and nums[j] > standard: j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] < standard: i += 1
        nums[j] = nums[i]
    nums[i] = standard
    quicksort(nums,left,i-1)
    quicksort(nums,i+1,right)

nums = [-10,2,3,1,1,0,6]
print(nums)
quicksort(nums, 0, len(nums)-1)
print(nums)

nums = [-10,2,3,1,1,0,6]
print(nums)
quicksort_2(nums, 0, len(nums)-1)
print(nums)
