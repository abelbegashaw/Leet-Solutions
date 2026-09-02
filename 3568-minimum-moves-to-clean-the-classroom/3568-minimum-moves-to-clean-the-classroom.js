/**
 * @param {string[]} classroom
 * @param {number} energy
 * @return {number}
 */
var minMoves = function(classroom, energy) {
  // pre - process
    let m = classroom.length, n = classroom[0].length
    const key = (i, j) => `${i},${j}`
    const inbound = (x, y) => 0 <= x && x < m && 0 <= y && y < n
    var identifier = 0
    var litters = new Map()
    var sx = -1, sy = -1;
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if (classroom[i][j] === 'L') {
                litters.set(key(i, j), identifier);
                identifier++;
            } else if (classroom[i][j] === 'S') {
                sx = i
                sy = j
            }
        }
    }

    // BFS
    let directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    let best = Array.from({length : m}, (_, i) => Array.from({length : n}, (_, j) => Array.from({length : 1 << litters.size}, (_, k) => -1)))
    let curr = [[sx, sy, energy, 0]]
    let jump = 0
    let next_level = []
    while(curr.length != 0) {
        
        for(let i = 0; i < curr.length; i++) {
            let [x, y, power, mask] = curr[i] // 1, 1, 3, 2
            let new_mask = 0, new_power = 0
            
            if (mask === (1 << litters.size) - 1) {
                return jump
            }
            
            for(const [dx, dy] of directions) {
                let new_x = x + dx, new_y = y + dy
                if (inbound(new_x, new_y) && power && classroom[new_x][new_y] != 'X') {
                    new_mask = classroom[new_x][new_y] == 'L' ? mask | (1 << litters.get(key(new_x, new_y))) : mask
                    new_power = classroom[new_x][new_y] == 'R' ? energy : power - 1
                    if (best[new_x][new_y][new_mask] < new_power) {
                        best[new_x][new_y][new_mask] = new_power
                        next_level.push([new_x, new_y, new_power, new_mask])
                    }
                }
            }
        }
        curr = next_level
        next_level = []
        jump++;
    }
    return -1;  
};