def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    len_mat = len(mat[0])
    for a in mat:
        if len(a) != len_mat:
            return ValueError('строки разной длины')
    return [[a[x] for a in mat] for x in range(len_mat)]
print('transpose')
print(transpose(mat=[[1, 2, 3]]))
print(transpose(mat=[[1], [2], [3]]))
print(transpose(mat=[[1, 2], [3, 4]]))
print(transpose(mat=[]))
print(transpose(mat=[[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    len_mat = len(mat[0])
    for a in mat:
        if len(a) != len_mat:
            return ValueError('строки разной длины')
    return [sum(a) for a in mat]
print('row_sums')
print(row_sums(mat=[[1, 2, 3], [4, 5, 6]]))
print(row_sums(mat=[[-1, 1], [10, -10]]))
print(row_sums(mat=[[0, 0], [0, 0]]))
print(row_sums(mat=[[1, 2], [3]]))
#
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    len_mat = len(mat[0])
    for a in mat:
        if len(a) != len_mat:
            return ValueError('строки разной длины')
    mat_02 = transpose(mat)
    return [sum(a) for a in mat_02]
print('col_sums')
print(col_sums(mat=[[1, 2, 3], [4, 5, 6]]))
print(col_sums(mat=[[-1, 1], [10, -10]]))
print(col_sums(mat=[[0, 0], [0, 0]]))
print(col_sums(mat=[[1, 2], [3]]))