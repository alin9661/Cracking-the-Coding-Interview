from collections import defaultdict

def test(nums):
    dictionary = defaultdict()
    for num in nums:
        dictionary[num] = nums

    for key, value in dictionary.items():
        dictionary.pop(key)

array = list(range(5))
test(nums=array)