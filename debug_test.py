def total(nums):
    s = 0
    for n in nums:
        s += n          # 여기에 중단점
    return s

data = [3, 1, 4, 1, 5, 9, 2, 6]
print("합계:", total(data))
