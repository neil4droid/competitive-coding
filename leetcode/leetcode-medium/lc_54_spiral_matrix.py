from typing import List

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		spiral_list = list()
		visited_matrix = [[False for value in matrix[i]] for i in range(len(matrix))]
		current_pos = [0, 0]
		direction = 0

		while current_pos is not None and not visited_matrix[current_pos[0]][current_pos[1]]:
			spiral_list.append(matrix[current_pos[0]][current_pos[1]])
			visited_matrix[current_pos[0]][current_pos[1]] = True
			direction = self.__update_direction(visited_matrix, current_pos, direction)
			current_pos = self.__get_next_position(current_pos, direction, matrix)

		return spiral_list

	def __update_direction(self, visited_matrix, current_pos, direction) -> int:
		try:
			if(	(direction == 0 and visited_matrix[current_pos[0]][current_pos[1]+1])
				or (direction == 1 and visited_matrix[current_pos[0]+1][current_pos[1]])
				or (direction == 2 and visited_matrix[current_pos[0]][current_pos[1]-1])
				or (direction == 3 and visited_matrix[current_pos[0]-1][current_pos[1]]) ):
					direction = (direction + 1) % 4
		except IndexError:
			direction = (direction + 1) % 4
		return direction

	def __get_next_position(self, current_pos, direction, matrix) -> List[int]:
		if direction == 0:
			current_pos = [current_pos[0], current_pos[1]+1]
		if direction == 1:
			current_pos = [current_pos[0]+1, current_pos[1]]
		if direction == 2:
			current_pos = [current_pos[0], current_pos[1]-1]
		if direction == 3:
			current_pos = [current_pos[0]-1, current_pos[1]]
		if current_pos[0] >= len(matrix) or current_pos[1] >= len(matrix[0]):
			return None
		return current_pos

sol = Solution()
input_matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]
print(sol.spiralOrder(input_matrix))
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sol.spiralOrder(input_matrix))
input_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(sol.spiralOrder(input_matrix))
input_matrix = [[1]]
print(sol.spiralOrder(input_matrix))