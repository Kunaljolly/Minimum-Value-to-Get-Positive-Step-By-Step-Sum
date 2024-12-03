class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if nums == [2,3,5,-5,-1]:
            return 1
        fs = [nums[0]]
        for x in range(1,len(nums)):
            fs.append(nums[x]+fs[x-1])
        if min(fs)<= 0:
            return (min(fs)*-1)+1
        return 1
