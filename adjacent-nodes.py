def is_adjacent(matrix, node1, node2):
     return True if matrix[node1][node2] else False

print(is_adjacent([
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
], 0, 1))
	
