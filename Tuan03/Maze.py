# Bài 2: MÊ CUNG - Tìm đường đi từ 0 đến A

from collections import deque
import sys

# ===== ĐỊNH NGHĨA MÊ CUNG =====
class MazeProblem:
    def __init__(self):
        # Mê cung 5 hàng x 4 cột
        # 0 = đường, 1 = tường
        # 0 = điểm bắt đầu (góc trên-trái)
        # A = điểm kết thúc (góc dưới-phải)
        
        self.maze = [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 'A']
        ]
        
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        self.start = (0, 0)      # Vị trí 0
        self.goal = (4, 3)       # Vị trí A
        
        # 4 hướng: Trên, Dưới, Trái, Phải
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.direction_names = ["Up", "Down", "Left", "Right"]
    
    def is_valid(self, row, col, visited):
        """Kiểm tra vị trí có hợp lệ không"""
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.maze[row][col] != 1 and 
                (row, col) not in visited)
    
    def get_neighbors(self, pos):
        """Lấy các vị trí lân cận hợp lệ"""
        row, col = pos
        neighbors = []
        
        for i, (dr, dc) in enumerate(self.directions):
            new_row, new_col = row + dr, col + dc
            if self.is_valid(new_row, new_col, set()):
                neighbors.append(((new_row, new_col), self.direction_names[i]))
        
        return neighbors
    
    def print_maze(self, path=None):
        """In mê cung ra màn hình"""
        print("\n MÊ CUNG (5x4):")
        print("    0 = đường, 1 = tường")
        print("    0 = điểm bắt đầu, A = điểm kết thúc\n")
        
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.maze[i][j]
                
                # Tô đỏ đường đi nếu có
                if path and (i, j) in path:
                    if (i, j) == self.start:
                        print("start", end=" ")  # Điểm bắt đầu
                    elif (i, j) == self.goal:
                        print("end", end=" ")  # Điểm kết thúc
                    else:
                        print("way", end=" ")  # Đường đi
                else:
                    if (i, j) == self.start:
                        print("start", end=" ")
                    elif (i, j) == self.goal:
                        print("end", end=" ")
                    elif cell == 0:
                        print("path", end=" ")
                    else:
                        print("wall", end=" ")
            print()

# ===== THUẬT TOÁN BFS =====
def bfs_maze(problem):
    """Tìm đường đi ngắn nhất trong mê cung"""
    queue = deque([(problem.start, [problem.start])])
    visited = {problem.start}
    
    while queue:
        (row, col), path = queue.popleft()
        
        # Kiểm tra đã đến đích chưa
        if (row, col) == problem.goal:
            return path
        
        # Khám phá các vị trí lân cận
        for new_row in range(row - 1, row + 2):
            for new_col in range(col - 1, col + 2):
                # Chỉ xét 4 hướng (không xét đường chéo)
                if abs(new_row - row) + abs(new_col - col) == 1:
                    if problem.is_valid(new_row, new_col, visited):
                        visited.add((new_row, new_col))
                        queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None

# ===== THUẬT TOÁN DFS =====
def dfs_maze(problem):
    """Tìm đường đi bằng DFS"""
    stack = [(problem.start, [problem.start])]
    visited = {problem.start}
    
    while stack:
        (row, col), path = stack.pop()
        
        if (row, col) == problem.goal:
            return path
        
        for new_row in range(row - 1, row + 2):
            for new_col in range(col - 1, col + 2):
                if abs(new_row - row) + abs(new_col - col) == 1:
                    if problem.is_valid(new_row, new_col, visited):
                        visited.add((new_row, new_col))
                        stack.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None

# ===== MAIN =====
if __name__ == "__main__":
    problem = MazeProblem()
    
    print("=" * 60)
    print("BÀI 2: MÊ CUNG - TÌM ĐƯỜNG ĐI TỪ 0 ĐẾN A")
    print("=" * 60)
    
    # In mê cung
    problem.print_maze()
    
    # BFS
    print("\n Tìm kiếm BFS (Breadth-First Search)...")
    bfs_path = bfs_maze(problem)
    
    if bfs_path:
        print(f" Tìm thấy đường đi!")
        print(f" Vị trí: {' → '.join([str(pos) for pos in bfs_path])}")
        print(f" Độ dài: {len(bfs_path) - 1} bước")
        problem.print_maze(set(bfs_path))
    else:
        print(" Không tìm thấy đường đi")
    
    # DFS
    print("\n Tìm kiếm DFS (Depth-First Search)...")
    dfs_path = dfs_maze(problem)
    
    if dfs_path:
        print(f" Tìm thấy đường đi!")
        print(f" Vị trí: {' → '.join([str(pos) for pos in dfs_path])}")
        print(f" Độ dài: {len(dfs_path) - 1} bước")
    else:
        print(" Không tìm thấy đường đi")
    
    print("\n" + "=" * 60)
    print("Kết luận: BFS tìm ra đường đi ngắn nhất")
    print("=" * 60)
