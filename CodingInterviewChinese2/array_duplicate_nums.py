#!/usr/bin/python
# coding=utf-8  

### 数组中重复的数字
""" 
	在一个长度为n的数组里所有的数组都在0～n-1的范围内。
	数组中的某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
"""
def duplicate_1(nums):
	""" 时间复杂度: O(n); 空间复杂度：O(1) """
	if len(nums) == 0:
		return False
	dnums= set()
	for i in xrange(len(nums)):
		m = nums[i]
		if i == m: continue
		if nums[m] == m:
			dnums.add(m)
		else:
			nums[i], nums[m] = nums[m], nums[i]
	return list(dnums)

def duplicate_2(nums):
	""" 要求不改变原数组 
	方法1: 新增一个n+1长度的数组
	"""


def TestCase():
	return [
		{"nums": [], "result": False},
		{"nums": [2, 3, 1, 0, 2, 5, 3], "result": [2,3]}
	]

def Test_1():
	test_data = TestCase()
	for item in test_data:
		if duplicate(item['nums']) == item['result']:
			print('Correct')
		else:
			print('Failed! Test data:')
			print(item)
if __name__ == '__main__':
	Test_1()
