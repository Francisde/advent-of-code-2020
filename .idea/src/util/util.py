def print_2d(grid):
    for row in grid:
        print(row)
    print()

def print_3d(grid):
    for slice in grid:
        print("next slice")
        for row in slice:
            print(row)
        print()

def deepcopy_3d(grid):
    result = []
    for slice in grid:
        new_slice = []
        for row in slice:
            new_slice.append(row.copy())
        result.append(new_slice)
    return result

def deepcopy_4d(grid):
    result = []
    for slice in grid:
        new_slice = []
        for row in slice:
            new_row = []
            for rrow in row:
                new_row.append(rrow.copy())
            new_slice.append(new_row)
        result.append(new_slice)
    return result