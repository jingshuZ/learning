def threeSum(nums):
    n = len(nums)
    res = []
    if (not nums or n < 3):
        return []
    nums.sort()  # 对数组进行排序
    res = []
    for i in range(n):
        if (nums[i] > 0):
            return res  # 已经排好，返回结果
        if (i > 0 and nums[i] == nums[i - 1]):
            continue  # 继续循环的下一个迭代,用于在 for 循环（或 while 循环）中结束当前迭代,继续下一个迭代
        left = i + 1
        right = n - 1
        while (left < right):
            if (nums[i] + nums[left] + nums[right] == 0):
                res.append([nums[i], nums[left], nums[right]])
                while (left < right and nums[left] == nums[left + 1]):
                    left = left + 1
                while (left < right and nums[right] == nums[right + 1]):
                    right = right - 1
                left = left + 1
                right = right - 1
            elif (nums[i] + nums[left] + nums[right] > 0):
                right = right - 1
            else:
                left = left + 1
    return res


print(threeSum([3, 4, 5, 0, 1, -5, -6, 8]))
