# 输入：邻接矩阵matrix 输出：路径(list,num)
# 算法端
def nearest_neighbor(dist, start=0):
    n = len(dist)
    if len(dist) == 0:
        return [], 0
    path = [start] # 保存轨迹
    visited = {start} # 保存走过的顶点 set 查找复杂度为O（1）
    index = start # 保存当前顶点
    weight = 0



    while len(visited) != len(dist):
        next = min((v for v in range(n) if not v in visited),key=lambda v:dist[index][v])
        path.append(next)
        visited.add(next)
        weight += dist[index][next]
        index = next
    weight += dist[index][start]

    return path, weight








if __name__ == '__main__':
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    print(nearest_neighbor(dist, start=0))