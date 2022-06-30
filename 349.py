grid = {}
blacks = 0
jump = [[(0,-1), (1,0), (0,1), (-1,0)], [(0,1), (-1,0), (0,-1), (1,0)]]

def nextstep(now, dir):
    onblack = grid.get(now, 0)
    new = (now[0]+jump[onblack][dir][0], now[1]+jump[onblack][dir][1])
    grid[now] = 0 if onblack else 1
    if onblack:
        dir += 1
        if dir > 3: dir = 0
    else:
        dir -= 1
        if dir < 0: dir = 3
    return new, dir, -1 if onblack else 1

ant, dir = (0, 0), 0
steps = 0
while True:
    ant, dir, b = nextstep(ant, dir)
    blacks += b
    steps  += 1
    if steps > 10647 and (10**18 - steps) % 104 == 0:
        blacks += 12 * (10**18 - steps) // 104
        print(blacks)
        break

