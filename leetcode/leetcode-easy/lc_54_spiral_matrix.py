from typing import List

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		spiral_list = list()
		visited_matrix = [[False for value in matrix[i]] for i in range(len(matrix))]
		current_pos = [0, 0]

		while current_pos is not None:
			spiral_list.append(matrix[current_pos[0]][current_pos[1]])
			visited_matrix[current_pos[0]][current_pos[1]] = True
			current_pos = self.__get_next_position(visited_matrix, current_pos)

		return spiral_list

	def __get_next_position(self, visited_matrix, current_pos) -> List[int]:
		try:
			if not visited_matrix[current_pos[0]][current_pos[1]+1]:
				return [current_pos[0], current_pos[1]+1]
		except IndexError: pass
		try:
			if not visited_matrix[current_pos[0]+1][current_pos[1]]:
				return [current_pos[0]+1, current_pos[1]]
		except IndexError: pass
		try:
			if not visited_matrix[current_pos[0]][current_pos[1]-1]:
				return [current_pos[0], current_pos[1]-1]
		except IndexError: pass
		try:
			if not visited_matrix[current_pos[0]-1][current_pos[1]]:
				return [current_pos[0]-1, current_pos[1]]
		except IndexError: pass
		return None

sol = Solution()
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