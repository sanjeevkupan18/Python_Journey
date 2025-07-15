from itertools import permutations
from collections import deque

def parse_input_and_extract_sheets(grid, N, M):
    sheets = []
    for i in range(0, N, M):
        row = []
        for j in range(0, N, M):
            sheet = [grid[x][j:j + M] for x in range(i, i + M)]
            row.append(sheet)
        sheets.append(row)
    return sheets

def is_valid_connection(sheet1, sheet2, side):
    if side == "right":  # Check the right edge of sheet1 with the left edge of sheet2
        for i in range(len(sheet1)):
            if sheet1[i][-1] == "T" and sheet2[i][0] != "T":
                return False
    elif side == "bottom":  # Check the bottom edge of sheet1 with the top edge of sheet2
        if sheet1[-1] != sheet2[0]:
            return False
    return True

def reconstruct_full_grid(sheets, N, M):
    full_grid = []
    for sheet_row in sheets:
        for i in range(M):
            row = []
            for sheet in sheet_row:
                row.extend(sheet[i])
            full_grid.append(row)
    return full_grid

def bfs_shortest_distance(grid, start, end, N):
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and grid[nx][ny] in {"T", "D"}:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return float("inf")

def find_shortest_path(N, M, grid):
    # Extract sheets from the input grid
    sheets = parse_input_and_extract_sheets(grid, N, M)
    num_sheets = N // M

    # Find the positions of S and D
    start_pos, end_pos = None, None
    for i in range(num_sheets):
        for j in range(num_sheets):
            sheet = sheets[i][j]
            for x in range(M):
                for y in range(M):
                    if sheet[x][y] == "S":
                        start_pos = (i, j, x, y)
                    elif sheet[x][y] == "D":
                        end_pos = (i, j, x, y)

    # Rearrange sheets
    sheet_positions = [(i, j) for i in range(num_sheets) for j in range(num_sheets)]
    sheet_positions.remove((start_pos[0], start_pos[1]))
    sheet_positions.remove((end_pos[0], end_pos[1]))

    min_distance = float("inf")
    for perm in permutations(sheet_positions):
        # Arrange sheets in the order of the permutation
        arranged_sheets = [[None for _ in range(num_sheets)] for _ in range(num_sheets)]
        arranged_sheets[0][0] = sheets[start_pos[0]][start_pos[1]]
        arranged_sheets[-1][-1] = sheets[end_pos[0]][end_pos[1]]

        index = 0
        for i in range(num_sheets):
            for j in range(num_sheets):
                if arranged_sheets[i][j] is None:
                    arranged_sheets[i][j] = sheets[perm[index][0]][perm[index][1]]
                    index += 1

        # Validate connections between adjacent sheets
        valid = True
        for i in range(num_sheets):
            for j in range(num_sheets - 1):
                if not is_valid_connection(arranged_sheets[i][j], arranged_sheets[i][j + 1], "right"):
                    valid = False
                    break
            if not valid:
                break
        for i in range(num_sheets - 1):
            for j in range(num_sheets):
                if not is_valid_connection(arranged_sheets[i][j], arranged_sheets[i + 1][j], "bottom"):
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            continue

        # Reconstruct the full grid
        full_grid = reconstruct_full_grid(arranged_sheets, N, M)

        # Compute shortest path using BFS
        shortest_distance = bfs_shortest_distance(full_grid, start_pos[2:], end_pos[2:], N)
        min_distance = min(min_distance, shortest_distance)

    return min_distance

# Input handling
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# Find and print the shortest distance
print(find_shortest_path(N, M, grid))