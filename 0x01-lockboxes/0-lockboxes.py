#!/usr/bin/python3
'''A module for working with Lockboxes.
'''

def canUnlockAll(boxes):
	'''A key with the same number as a box opens that box
 	You can assume all keys will be positive integers
	The first box boxes[0] is unlocked
	Return True if all boxes can be opened, else return False.
 	'''
	boxesNumber = len(boxes)
	visited = [False] * boxesNumber
	visited[0] = True
	stack = [0]

	while stack:
		current_box = stack.pop()
		for key in boxes[current_box]:
			if key < boxesNumber and not visited[key]:
				visited[key] = True
				stack.append(key)
	return all(visited)
