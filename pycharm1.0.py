#哈希表解题思路
"""
先对数组进行排序，再遍历，将每个元素的相反数作为key，元素所在位置作为value存入哈希表。
两次遍历后检查a+b是否存在哈希表中

找到满足条件的结果后, 将结果数组序列化并存入令一个哈希表中,以便对结果去重
首先在对 a,b 进行遍历时,
如果当前元素与前一个元素相同可直接跳过以优化性能
(思考: 后一个元素能发现的结果一定会包含在前一个元素的结果中).
另外, 仅在一层循环中加入此逻辑性能最佳.
该逻辑有效的前提是相同的元素需要连在一起, 所以需先对数组进行排序
"""

def threeSum(nums):
    if len(nums) < 3:                                                   #先对数组进行排序
        return[]
    nums.sort()
    target_hash = { -x: i for i, x in enumerate(nums)}
    res = []
    res_hash = []
    for i, first in enumerate(nums):
        if i > 0 and first == nums[i - 1]:
            continue
        for j, second in enumerate(nums[i + 1:]):                        #检查两数之和是否存在于哈希表中
            if first + second in target_hash:
                target_index = target_hash[first + second]
                if target_index == i or target_index == j:
                    continue                                             #将找到的结果存入另一个哈希表中，避免结果重复
                row = sorted([first, second, nums[target_index]])
                key = ','.join([str(x) for x in row])
                if key not in res_hash:
                    res.append(row)
                    
                   
    return res
print(threeSum([3, 4, 5, 0, 1, -5, -6, 8]))


"""
三数之和
给你一个包含 n 个整数的数组 nums
判断 nums 中是否存在三个元素 a，b，c 
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。


给定数组 nums = [-1, 0, 1, 2, -1, -4]，
例如：
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
思路： 双指针
1、对于数组长度为n，如果长度为null或者小于3，返回空
2、对数组进行排序
3、遍历排序后数组：3.1 num[i]>0:已经排好，返回结果
3.2 重复元素：跳过。3.3，左指针 left = i + 1，右指针 right = n -1
left < right 循环
当 nums[i] + nums[left] + nums[right] == 0,判断左右是否下一位置重复
去重：sum > 0 , nums[right]大， right左移
sum < 0 ,nums[left]小, left右移
"""

# def threeSum(nums):
#     n = len(nums)
#     res = []
#     if (not nums or n < 3):
#         return []
#     nums.sort()  # 对数组进行排序
#     res = []
#     for i in range(n):
#         if (nums[i] > 0):
#             return res  # 已经排好，返回结果
#         if (i > 0 and nums[i] == nums[i - 1]):
#             continue  # 继续循环的下一个迭代,用于在 for 循环（或 while 循环）中结束当前迭代,继续下一个迭代
#         left = i + 1
#         right = n - 1
#         while (left < right):
#             if (nums[i] + nums[left] + nums[right] == 0):
#                 res.append([nums[i], nums[left], nums[right]])
#                 while (left < right and nums[left] == nums[left + 1]):
#                     left = left + 1
#                 while (left < right and nums[right] == nums[right + 1]):
#                     right = right - 1
#                 left = left + 1
#                 right = right - 1
#             elif (nums[i] + nums[left] + nums[right] > 0):
#                 right = right - 1
#             else:
#                 left = left + 1
#     return res
# print(threeSum([3, 4, 5, 0, 1, -5, -6, 8]))


