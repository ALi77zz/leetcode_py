'''
Author: Lipc
Date: 2026-08-20 20:49:56
LastEditTime: 2026-08-20 23:19:25
Description: 
FilePath: \python\hot100\283移动零.py
'''

# 第一种思路

# 遍历数组中的每一个数字，如果是零，就找下一个不为零的进行交换。
for i in range(0, len(nums)):
    if nums[i] == 0:
        j = i + 1
        while j < len(nums):
            if nums[j] == 0:
                j += 1
        # 直到下一个不为零的数字
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

# 超时了    可能反复扫描同一段数组，最坏是 O(n²)

# 第二种思路
# 双指针
# slow 用来找零，  fast 用来找非零
slow = 0
fast = 0
# fast找到非零就与slow交换
for fast in range(0, len(nums)):
    if nums[fast] != 0:
        temp = nums[fast]
        nums[fast] = nums[slow]
        nums[slow] = temp
        # slow 移动到下一位
        slow += 1

# 第三种思路
# 原地覆盖 + 补零
'''
    用slow来指0，fast指非0
    fast找到非零就覆盖slow，slow移动到下一位
    fast找完之后，slow后面的都补零
'''
slow = 0
for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow] = nums[fast]
        slow += 1
for i in range(slow, len(nums)):
    nums[i] = 0
