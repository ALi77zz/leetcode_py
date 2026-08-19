# @Version  : 1.0
# @Author   : Lipc
# @File     : 1两数之和.py
# @Time     : 2026/8/19 下午1:22

nums = [3,2,4]
target = 6

# 暴力解法
# for i in range(0, len(nums)):
#     for j in range(0, len(nums)):
#         if nums[i] + nums[j] == target:
#             if i != j:
#                 print(i,j)
#                 break

# 暴力改进
# for i in range(0, len(nums)):
#     '''
#         减少循环，不去做重复工作
#         当i=2的时候，如果再做j=1的工作，相当于在重复做i=1，j=2的工作
#         如果i=1，j=2时满足条件就不会再进行下面的循环了，因此无需再做与之对应的i=2，j=1
#         直接从i+1开始寻找
#     '''
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i,j)
#             break

# 哈希法（用空间来换取时间）
# '''
#     核心思想：空间换时间，遍历数组时，把已经遍历过的数字存起来，方便快速进行查找
#     关键：对于当前数num来说，我们需要找到的是target-num。在之前遍历过的数中来查找target-num
#     如果找不到的话，那就进行下一个num，并把当前num保存在哈希表（字典）中
    
#     注意，最后要返回的是两个数字的index
# '''
# # 创建一个字典来保存遍历过的数字以及对应的index
# dict = {}
# for i,num in enumerate(nums):
#     # aim用来表示另一个数字
#     aim = target - num
#     # 查找在遍历过的数字中是否存在aim
#     if aim in dict:
#         print([dict[aim], i])

#     # 如果没有找到就继续进行遍历，并把当前num存入字典中
#     dict[num] = i