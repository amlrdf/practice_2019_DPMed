from copy import deepcopy



def print_grid(grid):
    print('\n\n' + '-' * 26)
    print('    0   1   2   3   4   5   6   7   8')
    print('  ┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓')
    for y, row in enumerate(grid):
        print('{y} ┃ {r[0]} │ {r[1]} │ {r[2]} ┃ {r[3]} │ {r[4]} │ {r[5]} ┃ {r[6]} │ {r[7]} │ {r[8]} ┃ = {s}'.format(y=y, r=''.join([str(x) for x in row]).replace('0', ' '), s=sum(row)))
        print('  ┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛' if y == 8 else '  ┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫' if (y + 1) % 3 == 0 else '  ┠───┼───┼───╂───┼───┼───╂───┼───┼───┨')

    print('    ‖   ‖   ‖   ‖   ‖   ‖   ‖   ‖   ‖ ')
    col_totals = [sum([grid[y][x] for y in range(9)]) for x in range(9)]
    print('    {}   {}   {}   {}   {}   {}   {}   {}   {}'.format(*[x//10 for x in col_totals]))
    print('    {}   {}   {}   {}   {}   {}   {}   {}   {}\n'.format(*[x % 10 for x in col_totals]))

    grids_of_3x3 = [[[grid[y + 3 * (z // 3)][x + 3 * (z % 3)] for x in range(3)] for y in range(3)] for z in range(9)]
    print('3x3 sub grid totals:')
    print('┏━━━┳━━━┳━━━┓')
    for idx, sub_grid in enumerate(grids_of_3x3):
        if idx % 3 == 0 and idx > 0:
            print('┃')
            print('┣' + '━━━╋━━━╋━━━' + '┫')
        sub_grid_total = 0
        for row in sub_grid:
            sub_grid_total += sum(row)
        print('┃{:^3}'.format(sub_grid_total), end='')

    print('┃')
    print('┗━━━┻━━━┻━━━┛')


# def print_grid(grid):
#     print('\n\n' + '-'*26)
#     print('    0   1   2   3   4   5   6   7   8')
#     print('  ┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓')
#     for y, row in enumerate(grid):
#         print('{} ┃'.format(y), end='')
#         for x, col in enumerate(row):
#             print('{:^3}{}'.format(col if col != 0 else ' ', '┃' if (x + 1) % 3 == 0 else '│'), end='')
#         print(' = {}'.format(sum(row)))
#         if y <= 7:
#             print(' ', '┣' if (y + 1) % 3 == 0 else '┠', end='')
#             for x in range(len(row) * 2 - 1):
#                 if x % 2 == 0:
#                     char = '━━━' if (y + 1) % 3 == 0 else '───'
#                 else:
#                     char = '┿' if (y + 1) % 3 == 0 and (x + 1) % 3 != 0 else \
#                         '╂' if (x + 1) % 3 == 0 and (y + 1) % 3 != 0 else \
#                             '╋' if (x + 1) % 3 == 0 and (y + 1) % 3 == 0 else '┼'
#                 print(char, end='')
#             print('┫' if (y + 1) % 3 == 0 else '┨')
#     print('  ┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛')
#     print('    ‖   ‖   ‖   ‖   ‖   ‖   ‖   ‖   ‖ ')
#     col_totals = [sum([grid[y][x] for y in range(9)]) for x in range(9)]
#     print('    {}   {}   {}   {}   {}   {}   {}   {}   {}'.format(*[x//10 for x in col_totals]))
#     print('    {}   {}   {}   {}   {}   {}   {}   {}   {}\n'.format(*[x % 10 for x in col_totals]))
#     grids_of_3x3 = [[[grid[y + 3 * (z // 3)][x + 3 * (z % 3)] for x in range(3)] for y in range(3)] for z in range(9)]
#
#     print('3x3 sub grid totals:')
#     print('┏━━━┳━━━┳━━━┓')
#     for idx, sub_grid in enumerate(grids_of_3x3):
#         if idx % 3 == 0 and idx > 0:
#             print('┃')
#             print('┣' + '━━━╋━━━╋━━━' + '┫')
#         sub_grid_total = 0
#         for row in sub_grid:
#             sub_grid_total += sum(row)
#         print('┃{:^3}'.format(sub_grid_total), end='')
#
#     print('┃')
#     print('┗━━━┻━━━┻━━━┛')


def get_row(grid, row_idx):
    row = grid[row_idx]
    return row


def get_column(grid, col_idx):
    col = [grid[y][col_idx] for y in range(9)]
    return col


def get_3x3_sub_grid(grid, y, x):
    sub_grid = [[grid[y * 3 + j][x * 3 + i] for i in range(3)] for j in range(3)]
    sub_grid = sub_grid[0] + sub_grid[1] + sub_grid[2]
    return sub_grid


def build_array_from_string(string_grid):
    rows = string_grid.split('\n')
    grid = []
    for row in rows:
        grid.append([int(x) for x in row.split(',')])
    return grid


def generate_grid_of_possible_answers():
    grid = [[[i+1 for i in range(9)] for j in range(9)] for k in range(9)]
    return grid


def remove_by_row(grid_of_possible_answers, valid_grid):
    for j, row in enumerate(grid_of_possible_answers):
        row_from_grid = get_row(valid_grid, j)
        for i, possible_values in enumerate(row):
            for val in row_from_grid:
                if val in possible_values:
                    possible_values.remove(val)
    return grid_of_possible_answers


def remove_by_column(grid_of_possible_answers, valid_grid):
    for i in range(9):
        col_from_grid = get_column(valid_grid, i)
        for j in range(9):
            for val in col_from_grid:
                if val in grid_of_possible_answers[j][i]:
                    grid_of_possible_answers[j][i].remove(val)
    return grid_of_possible_answers


def remove_by_3x3_subgrid(grid_of_possible_answers, valid_grid):
    for sub_grid_y in range(3):
        for sub_grid_x in range(3):
            sub_grid_from_grid = get_3x3_sub_grid(valid_grid, sub_grid_y, sub_grid_x)
            for j in range(3):
                for i in range(3):
                    for val in sub_grid_from_grid:
                        if val in grid_of_possible_answers[sub_grid_y * 3 + j][sub_grid_x * 3 + i]:
                            grid_of_possible_answers[sub_grid_y * 3 + j][sub_grid_x * 3 + i].remove(val)
    return grid_of_possible_answers


def set_known_values(grid_of_possible_answers, valid_grid):
    for j in range(9):
        for i in range(9):
            if valid_grid[j][i] != 0:
                grid_of_possible_answers[j][i] = []
    return grid_of_possible_answers


def update_known_positions_using_grid_of_possible_answers(valid_grid, grid_of_possible_answers):
    for j in range(9):
        for i in range(9):
            if len(grid_of_possible_answers[j][i]) == 1:
                valid_grid[j][i] = grid_of_possible_answers[j][i][0]
    return valid_grid


def update_with_single_values(valid_grid, grid_of_possible_answers):
    for j in range(9):
        counts = [0]*9
        row = get_row(grid_of_possible_answers, j)
        for col in row:
            for val in col:
                counts[val-1] += 1
        for val, count in enumerate(counts):
            if count == 1:
                for idx, col in enumerate(row):
                    if val + 1 in col:
                        valid_grid[j][idx] = val + 1

    for i in range(9):
        counts = [0]*9
        column = get_column(grid_of_possible_answers, i)
        for row in column:
            for val in row:
                counts[val-1] += 1
        for val, count in enumerate(counts):
            if count == 1:
                for idx, row in enumerate(column):
                    if val + 1 in row:
                        valid_grid[idx][i] = val + 1

    for sub_grid_y in range(3):
        for sub_grid_x in range(3):
            sub_grid = get_3x3_sub_grid(grid_of_possible_answers, sub_grid_y, sub_grid_x)
            counts = [0]*9
            for a in sub_grid:
                for b in a:
                    counts[b-1] += 1
            for index, count in enumerate(counts):
                if count == 1:
                    for idx, a in enumerate(sub_grid):
                        if index + 1 in a:
                            j = idx // 3
                            i = idx % 3
                            valid_grid[sub_grid_y * 3 + j][sub_grid_x * 3 + i] = index + 1

    return valid_grid


def main(initial_grid):
    valid_grid = build_array_from_string(initial_grid)
    grid_of_possible_answers = generate_grid_of_possible_answers()
    print_grid(valid_grid)
    while True:
        grid_of_possible_answers = set_known_values(grid_of_possible_answers, valid_grid)
        grid_of_possible_answers = remove_by_row(grid_of_possible_answers, valid_grid)
        grid_of_possible_answers = remove_by_column(grid_of_possible_answers, valid_grid)
        grid_of_possible_answers = remove_by_3x3_subgrid(grid_of_possible_answers, valid_grid)
        previous_grid = deepcopy(valid_grid)
        valid_grid = update_known_positions_using_grid_of_possible_answers(valid_grid, grid_of_possible_answers)
        valid_grid = update_with_single_values(valid_grid, grid_of_possible_answers)
        row_totals = 0
        col_totals = 0
        sub_grid_totals = 0
        for j in range(9):
            row_totals += sum(get_row(valid_grid, j))
            col_totals += sum(get_column(valid_grid, j))
            sub_grid_totals += sum(get_3x3_sub_grid(valid_grid, j // 3, j % 3))
        if row_totals == 405 and col_totals == 405 and sub_grid_totals == 405 or previous_grid == valid_grid:
            break
    print_grid(valid_grid)

if __name__ in '__main__':
    # input_grid = '2,0,4,1,0,0,0,0,0' + '\n' + \
    #              '0,0,0,5,0,3,6,0,7' + '\n' + \
    #              '0,0,0,9,0,0,4,0,0' + '\n' + \
    #              '9,0,0,4,0,0,0,1,0' + '\n' + \
    #              '6,5,0,0,1,0,0,7,4' + '\n' + \
    #              '0,2,0,0,0,8,0,0,9' + '\n' + \
    #              '0,0,9,0,0,5,0,0,0' + '\n' + \
    #              '5,0,2,3,0,1,0,0,0' + '\n' + \
    #              '0,0,0,0,0,4,1,0,2'
    input_grid = '0,0,0,0,0,0,0,0,0' + '\n' + \
                 '0,0,0,0,0,3,0,8,5' + '\n' + \
                 '0,0,1,0,2,0,0,0,0' + '\n' + \
                 '0,0,0,5,0,7,0,0,0' + '\n' + \
                 '0,0,4,0,0,0,1,0,0' + '\n' + \
                 '0,9,0,0,0,0,0,0,0' + '\n' + \
                 '5,0,0,0,0,0,0,7,3' + '\n' + \
                 '0,0,2,0,1,0,0,0,0' + '\n' + \
                 '0,0,0,0,4,0,0,0,9'
    main(input_grid)

