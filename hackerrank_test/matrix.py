# def flippingMatrix(matrix):
#     high_numbers = []
#     for array in matrix:
#         max_number = max(array)
#         position = array.index(max_number)
#         if array[position] > array[0] or array[position] > array[1]:
#             high_numbers.append(max_number)
#     sum = high_numbers[0] + high_numbers[3] + matrix[1][0] + matrix[1][1]
#     return sum

# print(flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49],[15, 78, 101, 43], [62, 98, 114, 108]]))