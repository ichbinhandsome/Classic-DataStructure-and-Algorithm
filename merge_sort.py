def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        mid = len(numbers)//2
        left = merge_sort(numbers[:mid])
        right = merge_sort(numbers[mid:])
        return merge(left,right)

print(merge_sort([1,2,7,3,4,5,-1,5]))
