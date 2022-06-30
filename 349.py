grid = {}
blacks = 0
jump =  [(0,1), (-1,0), (0,-1), (1,0)]

def nextstep(now, dir):
    onblack = grid.get(now, -1)
    new = (now[0]+jump[dir][0]*onblack, now[1]+jump[dir][1]*onblack)
    grid[now] = -onblack
    dir = (dir+onblack) % 4
    return new, dir, -onblack

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

