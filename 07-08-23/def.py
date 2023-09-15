# def twoSum(a,t):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j]==target:
#                 return ([i,j])
# nums = [11,15,324,4235435,2,34324535,53456346,7]
# target = 9
# print(twoSum(nums, target))

# def twosum(a,t):
#     start=0
#     end=len(a)-1
#     while start<end:
#         currentsum=a[start]+a[end]
#         if currentsum ==t:
#             return([start,end])
#         elif currentsum<target:
#             start+=1
#         else:
#             end=end-1
#     return -1
# nums=[1,2,3,4,5]
# target=9
# print(twosum(nums,target))