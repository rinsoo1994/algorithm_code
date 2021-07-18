min_path = 10e9


def dfs(TX, TY, x, y, now_grid, count):
    global min_path
    if x == TX - 1 and y == TY - 1:
        min_path = min(min_path, count)

    direction_list = [(1, 0), (0, 1)]
    for direction in direction_list:
        n_x = x + direction[0]
        n_y = y + direction[1]
        if n_x < TX and n_y < TY:
            count += now_grid[n_x][n_y]
            dfs(TX, TY, n_x, n_y, now_grid, count)
            count -= now_grid[n_x][n_y]
    return


def solution(grid):
    global min_path

    X = len(grid)
    Y = len(grid[0])
    dfs(X, Y, 0, 0, grid, grid[0][0])
    return min_path


solution([ [1, 2], [3, 4] ])
