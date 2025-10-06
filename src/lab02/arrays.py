def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError('список пуст')
    else:
        return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    a = []
    for row in mat:
        if isinstance(row, list) or isinstance(row, tuple):
            a.extend(row)
        else:
            raise TypeError('строка не строка строк матрицы')
    return a

print('min_max')
print(min_max(nums=[3, -1, 5, 5, 0]))
print(min_max(nums=[42]))
print(min_max(nums=[-5, -2, -9]))
print(min_max(nums=[1.5, 2, 2.0, -3.1]))
print(min_max(nums=[]))

print('unique_sorted')
print(unique_sorted(nums=[3, 1, 2, 1, 3]))
print(unique_sorted(nums=[]))
print(unique_sorted(nums=[-1, -1, 0, 2, 2]))
print(unique_sorted(nums=[1.0, 1, 2.5, 2.5, 0]))

print('flatten')
print(flatten(mat=[[1, 2], [3, 4]]))
print(flatten(mat=[[1, 2], (3, 4, 5)]))
print(flatten(mat=[[1], [], [2, 3]]))
print(flatten(mat=[[1, 2], "ab"]))
