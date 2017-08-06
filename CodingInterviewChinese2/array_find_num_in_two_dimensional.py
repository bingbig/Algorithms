#!/usr/bin/python
# coding=utf-8  
"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
输入一个这样的二维数组和一个整数，判断这个整数是否在数组中。
"""
def find_or_fail(arr, integer):
	arr_rows = len(arr)
	if not arr_rows: return False
	arr_cols = len(arr[0])
	if not arr_rows: return False

	row, col = 0, arr_cols - 1
	while row < arr_rows and col >= 0:
		if arr[row][col] == integer:
			return True
		elif arr[row][col] > integer:
			col -= 1
		else:
			row += 1
	return False



def TestCase():
	return [
		{"array": [], "integer": 0 ,"result": False},
		{"array": [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], "integer": 7, "result": True},
		{"array": [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], "integer": 5, "result": False}
	]

def Test():
	test_data = TestCase()
	for item in test_data:
		if find_or_fail(item['array'], item['integer']) == item['result']:
			print('Correct')
		else:
			print('Failed!')
			print(item)
		
if __name__ == '__main__':
	Test()