# TRAVELING SALESMAN PROBLEM 旅行商问题
## 问题描述：求图G的最小Hamilton圈
## 问题类型：NPC问题
## 近似算法：
### 1.近邻点算法（贪心算法）
**算法思想：** 从任意顶点出发，遍历Kn的所有顶点，每次到达的顶点处，
总是选择尚未经过的邻点中最近的一个前行，直到遍历所有顶点\
#### 计算复杂度： $O(n^2)$
#### 代码：
    
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
