def treasure_positions(grid):
    positions=[]
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x]==1:
                positions.append((i,x))
    return positions
grid = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 0]
]
positions=treasure_positions(grid)
print(f"Positions: {positions}")
print(f"Treasures: {len(positions)}")
for coordinates in positions:
    r, c = coordinates
    grid[r][c]=0
print(f"Updated map: {grid}")
