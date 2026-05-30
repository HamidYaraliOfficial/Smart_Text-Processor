import sys, math, time, random, heapq
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# ═══════════════════════════════════════════════════════════════
#  THEMES
# ═══════════════════════════════════════════════════════════════
THEMES = {
    "dark": {
        "bg": "#0a0e1a", "bg2": "#0d1220", "bg3": "#111828",
        "card": "#151d2e", "card2": "#1a2438",
        "acc": "#00e5ff", "acc2": "#7c4dff",
        "text": "#e0eaff", "text2": "#7a90b8",
        "border": "#2a3a5a", "danger": "#ff3d5a",
        "success": "#00e676", "warn": "#ffab00",
        "grid": "#1a2a3a", "wall": "#2a3a5a",
        "floor": "#0f1a28", "robot": "#00e5ff",
        "target": "#00e676", "obstacle": "#ff3d5a",
        "path": "#7c4dff", "explored": "#1a3a4a",
    },
    "light": {
        "bg": "#f0f4ff", "bg2": "#e4ecff", "bg3": "#d8e4ff",
        "card": "#ffffff", "card2": "#f4f7ff",
        "acc": "#0066ff", "acc2": "#7c00ff",
        "text": "#0a1428", "text2": "#4a6080",
        "border": "#b0c0e0", "danger": "#e60026",
        "success": "#00a84f", "warn": "#c07000",
        "grid": "#d0daf0", "wall": "#8090b0",
        "floor": "#e8f0ff", "robot": "#0066ff",
        "target": "#00a84f", "obstacle": "#e60026",
        "path": "#7c00ff", "explored": "#c8d8f0",
    },
}

TR = {
    "en": {
        "title": "Robot Navigator", "play": "Start Simulation", "settings": "Settings",
        "quit": "Quit", "back": "Back", "theme": "Theme", "lang": "Language",
        "dark": "Dark", "light": "Light", "pause": "Pause", "resume": "Resume",
        "restart": "Restart", "main_menu": "Main Menu", "paused": "PAUSED",
        "choose_env": "Choose Environment", "choose_ai": "AI Algorithm",
        "choose_size": "Map Size", "start": "Start", "score": "Score",
        "steps": "Steps", "time": "Time", "status": "Status",
        "searching": "Searching...", "moving": "Moving...", "reached": "Target Reached!",
        "stuck": "Robot Stuck!", "manual": "Manual", "auto": "Auto AI",
        "env1": "Warehouse", "env2": "House", "env3": "Maze", "env4": "Open Field",
        "ai1": "A* Search", "ai2": "BFS", "ai3": "DFS", "ai4": "Random Walk",
        "sz1": "Small (15×15)", "sz2": "Medium (25×25)", "sz3": "Large (35×35)",
        "fps": "FPS", "cells": "Cells", "path_len": "Path",
        "controls": "WASD / Arrows = Move  |  Space = Auto AI  |  R = New Map  |  Esc = Pause",
        "battery": "Battery", "sensor": "Sensor Range", "speed": "Speed",
        "obstacles": "Obstacles", "visited": "Visited",
        "mode": "Mode", "algorithm": "Algorithm",
        "new_target": "New Target", "reset": "Reset",
    },
    "fa": {
        "title": "ربات ناوبر", "play": "شروع شبیه‌سازی", "settings": "تنظیمات",
        "quit": "خروج", "back": "برگشت", "theme": "تم", "lang": "زبان",
        "dark": "تاریک", "light": "روشن", "pause": "توقف", "resume": "ادامه",
        "restart": "شروع مجدد", "main_menu": "منوی اصلی", "paused": "متوقف",
        "choose_env": "انتخاب محیط", "choose_ai": "الگوریتم هوش مصنوعی",
        "choose_size": "اندازه نقشه", "start": "شروع", "score": "امتیاز",
        "steps": "قدم", "time": "زمان", "status": "وضعیت",
        "searching": "در حال جستجو...", "moving": "در حال حرکت...", "reached": "به هدف رسید!",
        "stuck": "ربات گیر کرده!", "manual": "دستی", "auto": "هوش مصنوعی",
        "env1": "انبار", "env2": "خانه", "env3": "دهلیز", "env4": "فضای باز",
        "ai1": "جستجوی A*", "ai2": "BFS", "ai3": "DFS", "ai4": "گشت تصادفی",
        "sz1": "کوچک (۱۵×۱۵)", "sz2": "متوسط (۲۵×۲۵)", "sz3": "بزرگ (۳۵×۳۵)",
        "fps": "FPS", "cells": "خانه", "path_len": "مسیر",
        "controls": "WASD/پیکان = حرکت | Space = هوش مصنوعی | R = نقشه جدید | Esc = توقف",
        "battery": "باتری", "sensor": "برد سنسور", "speed": "سرعت",
        "obstacles": "موانع", "visited": "بازدید شده",
        "mode": "حالت", "algorithm": "الگوریتم",
        "new_target": "هدف جدید", "reset": "ریست",
    },
    "zh": {
        "title": "机器人导航", "play": "开始模拟", "settings": "设置",
        "quit": "退出", "back": "返回", "theme": "主题", "lang": "语言",
        "dark": "暗色", "light": "亮色", "pause": "暂停", "resume": "继续",
        "restart": "重新开始", "main_menu": "主菜单", "paused": "已暂停",
        "choose_env": "选择环境", "choose_ai": "AI算法",
        "choose_size": "地图大小", "start": "开始", "score": "分数",
        "steps": "步数", "time": "时间", "status": "状态",
        "searching": "搜索中...", "moving": "移动中...", "reached": "到达目标!",
        "stuck": "机器人卡住了!", "manual": "手动", "auto": "自动AI",
        "env1": "仓库", "env2": "房屋", "env3": "迷宫", "env4": "开阔地",
        "ai1": "A*搜索", "ai2": "BFS", "ai3": "DFS", "ai4": "随机游走",
        "sz1": "小 (15×15)", "sz2": "中 (25×25)", "sz3": "大 (35×35)",
        "fps": "帧率", "cells": "格子", "path_len": "路径",
        "controls": "WASD/方向键=移动 | 空格=AI | R=新地图 | Esc=暂停",
        "battery": "电池", "sensor": "传感器", "speed": "速度",
        "obstacles": "障碍", "visited": "已访问",
        "mode": "模式", "algorithm": "算法",
        "new_target": "新目标", "reset": "重置",
    },
}

ENVS = {
    "warehouse": {"key": "env1", "icon": "🏭", "wall_density": 0.22, "clusters": True},
    "house":     {"key": "env2", "icon": "🏠", "wall_density": 0.18, "clusters": False},
    "maze":      {"key": "env3", "icon": "🌀", "wall_density": 0.35, "clusters": False},
    "open":      {"key": "env4", "icon": "🌿", "wall_density": 0.08, "clusters": True},
}

AI_ALGOS = {
    "astar": {"key": "ai1", "icon": "⭐"},
    "bfs":   {"key": "ai2", "icon": "🔵"},
    "dfs":   {"key": "ai3", "icon": "🔴"},
    "rand":  {"key": "ai4", "icon": "🎲"},
}

MAP_SIZES = {
    "small":  {"key": "sz1", "icon": "▪", "size": 15},
    "medium": {"key": "sz2", "icon": "◼", "size": 25},
    "large":  {"key": "sz3", "icon": "⬛", "size": 35},
}

# ═══════════════════════════════════════════════════════════════
#  MAP GENERATOR
# ═══════════════════════════════════════════════════════════════
class MapGenerator:
    @staticmethod
    def generate(size, env_id):
        env = ENVS[env_id]
        grid = [[0] * size for _ in range(size)]
        density = env["wall_density"]

        if env_id == "maze":
            MapGenerator._generate_maze(grid, size)
        elif env["clusters"]:
            MapGenerator._generate_clusters(grid, size, density)
        else:
            MapGenerator._generate_random(grid, size, density)

        # Always clear corners for robot and target
        for r, c in [(0,0),(0,1),(1,0),(size-1,size-1),(size-1,size-2),(size-2,size-1)]:
            if 0 <= r < size and 0 <= c < size:
                grid[r][c] = 0
        return grid

    @staticmethod
    def _generate_random(grid, size, density):
        for r in range(size):
            for c in range(size):
                if random.random() < density:
                    grid[r][c] = 1

    @staticmethod
    def _generate_clusters(grid, size, density):
        n_clusters = int(size * size * density / 6)
        for _ in range(n_clusters):
            cr = random.randint(1, size - 2)
            cc = random.randint(1, size - 2)
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    nr, nc = cr + dr, cc + dc
                    if 0 < nr < size-1 and 0 < nc < size-1:
                        if random.random() < 0.6:
                            grid[nr][nc] = 1

    @staticmethod
    def _generate_maze(grid, size):
        for r in range(size):
            for c in range(size):
                grid[r][c] = 1
        def carve(r, c):
            dirs = [(0,2),(2,0),(0,-2),(-2,0)]
            random.shuffle(dirs)
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 1:
                    grid[r+dr//2][c+dc//2] = 0
                    grid[nr][nc] = 0
                    carve(nr, nc)
        grid[1][1] = 0
        carve(1, 1)

    @staticmethod
    def is_reachable(grid, start, end, size):
        if grid[end[0]][end[1]] == 1:
            return False
        visited = set()
        q = [start]
        visited.add(start)
        while q:
            r, c = q.pop(0)
            if (r, c) == end:
                return True
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))
        return False

# ═══════════════════════════════════════════════════════════════
#  AI PATHFINDER
# ═══════════════════════════════════════════════════════════════
class Pathfinder:
    @staticmethod
    def astar(grid, start, goal, size):
        def h(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
        open_set = [(h(start, goal), 0, start, [start])]
        visited  = set()
        while open_set:
            f, g, cur, path = heapq.heappop(open_set)
            if cur in visited: continue
            visited.add(cur)
            if cur == goal: return path, visited
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = cur[0]+dr, cur[1]+dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    ng = g + 1
                    heapq.heappush(open_set, (ng + h((nr,nc), goal), ng, (nr,nc), path+[(nr,nc)]))
        return [], visited

    @staticmethod
    def bfs(grid, start, goal, size):
        q        = [(start, [start])]
        visited  = {start}
        explored = set()
        while q:
            cur, path = q.pop(0)
            explored.add(cur)
            if cur == goal: return path, explored
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = cur[0]+dr, cur[1]+dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append(((nr,nc), path+[(nr,nc)]))
        return [], explored

    @staticmethod
    def dfs(grid, start, goal, size):
        stack    = [(start, [start])]
        visited  = set()
        explored = set()
        while stack:
            cur, path = stack.pop()
            if cur in visited: continue
            visited.add(cur)
            explored.add(cur)
            if cur == goal: return path, explored
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            random.shuffle(dirs)
            for dr, dc in dirs:
                nr, nc = cur[0]+dr, cur[1]+dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    stack.append(((nr,nc), path+[(nr,nc)]))
        return [], explored

    @staticmethod
    def random_walk(grid, start, goal, size, max_steps=500):
        cur      = start
        path     = [start]
        explored = {start}
        for _ in range(max_steps):
            if cur == goal: return path, explored
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            random.shuffle(dirs)
            moved = False
            for dr, dc in dirs:
                nr, nc = cur[0]+dr, cur[1]+dc
                if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0:
                    cur = (nr, nc)
                    path.append(cur)
                    explored.add(cur)
                    moved = True
                    break
            if not moved: break
        return path, explored

# ═══════════════════════════════════════════════════════════════
#  ROBOT SIMULATION STATE
# ═══════════════════════════════════════════════════════════════
class RobotState:
    def __init__(self, grid, size, algo_id):
        self.grid     = grid
        self.size     = size
        self.algo_id  = algo_id
        self.pos      = (1, 1)
        self.target   = self._rand_target()
        self.path     = []
        self.explored = set()
        self.path_idx = 0
        self.steps    = 0
        self.score    = 0
        self.elapsed  = 0.0
        self.battery  = 100.0
        self.status   = "searching"
        self.auto     = False
        self.sensor   = 3
        self.move_q   = []
        self.trail    = []
        self._compute_path()

    def _rand_target(self):
        for _ in range(500):
            r = random.randint(self.size//2, self.size-2)
            c = random.randint(self.size//2, self.size-2)
            if self.grid[r][c] == 0 and (r,c) != self.pos:
                if MapGenerator.is_reachable(self.grid, self.pos, (r,c), self.size):
                    return (r, c)
        return (self.size-2, self.size-2)

    def _compute_path(self):
        self.explored = set()
        self.path     = []
        self.path_idx = 0
        if self.algo_id == "astar":
            self.path, self.explored = Pathfinder.astar(self.grid, self.pos, self.target, self.size)
        elif self.algo_id == "bfs":
            self.path, self.explored = Pathfinder.bfs(self.grid, self.pos, self.target, self.size)
        elif self.algo_id == "dfs":
            self.path, self.explored = Pathfinder.dfs(self.grid, self.pos, self.target, self.size)
        else:
            self.path, self.explored = Pathfinder.random_walk(self.grid, self.pos, self.target, self.size)
        self.status = "moving" if self.path else "stuck"

    def set_auto(self, v):
        self.auto = v
        if v:
            self._compute_path()

    def manual_move(self, dr, dc):
        nr, nc = self.pos[0]+dr, self.pos[1]+dc
        if 0 <= nr < self.size and 0 <= nc < self.size and self.grid[nr][nc] == 0:
            self.trail.append(self.pos)
            if len(self.trail) > 200: self.trail.pop(0)
            self.pos   = (nr, nc)
            self.steps += 1
            self.battery = max(0, self.battery - 0.3)
            if self.pos == self.target:
                self.score += max(100, 500 - self.steps)
                self.status = "reached"
            self.explored.add(self.pos)

    def auto_step(self):
        if not self.auto or self.status in ("reached", "stuck"): return
        if not self.path or self.path_idx >= len(self.path):
            self._compute_path()
            if not self.path:
                self.status = "stuck"; return
        if self.path_idx < len(self.path):
            self.trail.append(self.pos)
            if len(self.trail) > 200: self.trail.pop(0)
            self.pos       = self.path[self.path_idx]
            self.path_idx += 1
            self.steps    += 1
            self.battery   = max(0, self.battery - 0.2)
            self.status    = "moving"
            if self.pos == self.target:
                self.score += max(100, 500 - self.steps)
                self.status = "reached"

    def new_target(self):
        self.target = self._rand_target()
        self.steps  = 0
        self.status = "searching"
        if self.auto:
            self._compute_path()

    def update(self, dt):
        self.elapsed += dt

# ═══════════════════════════════════════════════════════════════
#  3D ISOMETRIC RENDERER
# ═══════════════════════════════════════════════════════════════
class MapRenderer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.state: RobotState | None = None
        self.theme  = "dark"
        self._t     = 0.0
        self._cam_x = 0.0
        self._cam_y = 0.0
        self._zoom  = 1.0
        self._drag  = False
        self._drag_start = QPoint()
        self._cam_start  = (0.0, 0.0)
        self.setMouseTracking(True)
        self._hover = None

    def set_state(self, s): self.state = s; self.update()
    def set_theme(self, t): self.theme = t; self.update()

    def tick(self, t):
        self._t = t
        # Smooth camera follow robot
        if self.state:
            W, H = self.width(), self.height()
            cs   = self._cell_size()
            tx   = -self.state.pos[1] * cs + W/2 - cs/2
            ty   = -self.state.pos[0] * cs + H/2 - cs/2
            self._cam_x += (tx - self._cam_x) * 0.12
            self._cam_y += (ty - self._cam_y) * 0.12
        self.update()

    def _cell_size(self):
        if not self.state: return 24
        W, H  = self.width(), self.height()
        base  = min(W, H) / (self.state.size + 2)
        return max(10, min(60, base * self._zoom))

    def wheelEvent(self, e):
        delta = e.angleDelta().y()
        self._zoom = max(0.5, min(3.0, self._zoom * (1.1 if delta > 0 else 0.9)))
        self.update()

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.MiddleButton:
            self._drag = True
            self._drag_start = e.pos()
            self._cam_start  = (self._cam_x, self._cam_y)

    def mouseMoveEvent(self, e):
        if self._drag:
            dx = e.pos().x() - self._drag_start.x()
            dy = e.pos().y() - self._drag_start.y()
            self._cam_x = self._cam_start[0] + dx
            self._cam_y = self._cam_start[1] + dy
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.MiddleButton:
            self._drag = False

    def paintEvent(self, _e):
        if not self.state:
            return
        p  = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        W, H = self.width(), self.height()
        th   = THEMES[self.theme]
        st   = self.state
        cs   = self._cell_size()

        # Background
        bg_grad = QLinearGradient(0, 0, W, H)
        bg_grad.setColorAt(0, QColor(th["bg"]))
        bg_grad.setColorAt(1, QColor(th["bg3"]))
        p.fillRect(0, 0, W, H, QBrush(bg_grad))

        cx0 = int(self._cam_x)
        cy0 = int(self._cam_y)

        # Draw floor tiles first (all non-wall)
        for r in range(st.size):
            for c in range(st.size):
                x = cx0 + c * cs
                y = cy0 + r * cs
                if x + cs < 0 or x > W or y + cs < 0 or y > H:
                    continue
                if st.grid[r][c] == 0:
                    # Explored tint
                    if (r, c) in st.explored:
                        p.fillRect(int(x), int(y), int(cs)-1, int(cs)-1, QColor(th["explored"]))
                    else:
                        p.fillRect(int(x), int(y), int(cs)-1, int(cs)-1, QColor(th["floor"]))

        # Draw path
        if st.path and len(st.path) > 1:
            pen = QPen(QColor(th["path"]), max(1, cs * 0.18))
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            p.setPen(pen)
            for i in range(st.path_idx, len(st.path) - 1):
                r1, c1 = st.path[i]
                r2, c2 = st.path[i+1]
                x1 = int(cx0 + c1 * cs + cs/2)
                y1 = int(cy0 + r1 * cs + cs/2)
                x2 = int(cx0 + c2 * cs + cs/2)
                y2 = int(cy0 + r2 * cs + cs/2)
                p.drawLine(x1, y1, x2, y2)

        # Draw trail
        for i, (tr_r, tr_c) in enumerate(st.trail):
            x = cx0 + tr_c * cs
            y = cy0 + tr_r * cs
            alpha = int(30 + 120 * i / max(1, len(st.trail)))
            col = QColor(th["robot"])
            col.setAlpha(alpha)
            p.fillRect(int(x)+1, int(y)+1, int(cs)-2, int(cs)-2, col)

        # Draw walls (3D-ish)
        for r in range(st.size):
            for c in range(st.size):
                x = cx0 + c * cs
                y = cy0 + r * cs
                if x + cs < 0 or x > W or y + cs < 0 or y > H:
                    continue
                if st.grid[r][c] == 1:
                    self._draw_wall(p, int(x), int(y), int(cs), th)

        # Draw sensor range
        sr = st.sensor
        pr, pc = st.pos
        for dr in range(-sr, sr+1):
            for dc in range(-sr, sr+1):
                nr, nc = pr+dr, pc+dc
                if 0 <= nr < st.size and 0 <= nc < st.size:
                    dist = math.sqrt(dr*dr + dc*dc)
                    if dist <= sr:
                        sx = int(cx0 + nc * cs)
                        sy = int(cy0 + nr * cs)
                        alpha = int(25 * (1 - dist/sr))
                        col = QColor(th["robot"])
                        col.setAlpha(alpha)
                        p.fillRect(sx, sy, int(cs)-1, int(cs)-1, col)

        # Draw target
        tr_r, tr_c = st.target
        tx = int(cx0 + tr_c * cs)
        ty = int(cy0 + tr_r * cs)
        self._draw_target(p, tx, ty, int(cs), th)

        # Draw robot
        rob_x = int(cx0 + st.pos[1] * cs)
        rob_y = int(cx0 + st.pos[0] * cs)  # intentional: rob_y uses cy0
        rob_x = int(cx0 + st.pos[1] * cs)
        rob_y = int(cy0 + st.pos[0] * cs)
        self._draw_robot(p, rob_x, rob_y, int(cs), th)

        # Border grid lines
        pen = QPen(QColor(th["grid"]), 1)
        pen.setStyle(Qt.PenStyle.SolidLine)
        p.setPen(pen)
        for r in range(st.size + 1):
            y = int(cy0 + r * cs)
            if 0 <= y <= H:
                p.drawLine(max(0, int(cx0)), y, min(W, int(cx0 + st.size * cs)), y)
        for c in range(st.size + 1):
            x = int(cx0 + c * cs)
            if 0 <= x <= W:
                p.drawLine(x, max(0, int(cy0)), x, min(H, int(cy0 + st.size * cs)))

        p.end()

    def _draw_wall(self, p, x, y, cs, th):
        depth = max(2, cs // 6)
        # Front face
        face_col = QColor(th["wall"])
        p.fillRect(x, y, cs-1, cs-1, face_col)
        # Top face (lighter)
        top_pts = QPolygon([
            QPoint(x,        y),
            QPoint(x+depth,  y-depth),
            QPoint(x+cs-1+depth, y-depth),
            QPoint(x+cs-1,   y),
        ])
        top_col = QColor(th["wall"])
        top_col = top_col.lighter(140)
        p.setBrush(top_col)
        p.setPen(Qt.PenStyle.NoPen)
        p.drawPolygon(top_pts)
        # Right face (darker)
        right_pts = QPolygon([
            QPoint(x+cs-1,       y),
            QPoint(x+cs-1+depth, y-depth),
            QPoint(x+cs-1+depth, y+cs-1-depth),
            QPoint(x+cs-1,       y+cs-1),
        ])
        right_col = QColor(th["wall"])
        right_col = right_col.darker(130)
        p.setBrush(right_col)
        p.drawPolygon(right_pts)
        # Edge highlight
        p.setPen(QPen(QColor(th["border"]), 1))
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.drawRect(x, y, cs-1, cs-1)

    def _draw_target(self, p, x, y, cs, th):
        t   = self._t
        pulse = 0.5 + 0.5 * math.sin(t * 4)
        col   = QColor(th["target"])

        # Outer ring pulse
        r_out = int(cs * 0.45 + cs * 0.1 * pulse)
        col.setAlpha(int(120 * pulse))
        p.setBrush(col)
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(x + cs//2 - r_out, y + cs//2 - r_out, r_out*2, r_out*2)

        # Inner solid
        r_in = int(cs * 0.28)
        col2 = QColor(th["target"])
        col2.setAlpha(220)
        p.setBrush(col2)
        p.drawEllipse(x + cs//2 - r_in, y + cs//2 - r_in, r_in*2, r_in*2)

        # Center dot
        r_c = max(2, cs//8)
        p.setBrush(QColor("#ffffff"))
        p.drawEllipse(x + cs//2 - r_c, y + cs//2 - r_c, r_c*2, r_c*2)

        # Cross hairs
        pen = QPen(QColor(th["target"]), max(1, cs//12))
        p.setPen(pen)
        p.drawLine(x + cs//2, y + 3, x + cs//2, y + cs - 3)
        p.drawLine(x + 3, y + cs//2, x + cs - 3, y + cs//2)

    def _draw_robot(self, p, x, y, cs, th):
        t    = self._t
        bob  = math.sin(t * 8) * max(1, cs * 0.04)
        ry   = int(y + bob)

        # Shadow
        shadow = QRadialGradient(x + cs//2, y + cs - 2, cs//2)
        shadow.setColorAt(0, QColor(0, 0, 0, 80))
        shadow.setColorAt(1, QColor(0, 0, 0, 0))
        p.fillRect(x, y + cs - cs//4, cs, cs//4, QBrush(shadow))

        # Body
        body_col = QColor(th["robot"])
        body_grad = QRadialGradient(x + cs//2, ry + cs//3, cs//2)
        body_grad.setColorAt(0, body_col.lighter(140))
        body_grad.setColorAt(1, body_col.darker(120))
        p.setBrush(QBrush(body_grad))
        p.setPen(QPen(body_col.lighter(160), max(1, cs//14)))
        body_r = int(cs * 0.36)
        p.drawRoundedRect(
            x + cs//2 - body_r, ry + cs//2 - body_r,
            body_r*2, body_r*2, body_r//2, body_r//2
        )

        # Eyes / sensors
        eye_r = max(1, cs//10)
        eye_y = ry + cs//2 - eye_r
        for ex in [x + cs//2 - cs//6, x + cs//2 + cs//6]:
            p.setBrush(QColor("#ffffff"))
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(ex - eye_r, eye_y - eye_r, eye_r*2, eye_r*2)
            # Pupil
            p.setBrush(QColor(th["acc2"]))
            p.drawEllipse(ex - eye_r//2, eye_y - eye_r//2, eye_r, eye_r)

        # Antenna
        ant_x = x + cs//2
        ant_y = ry + cs//2 - body_r
        pen   = QPen(body_col.lighter(150), max(1, cs//16))
        p.setPen(pen)
        p.drawLine(ant_x, ant_y, ant_x, ant_y - cs//4)
        blink_col = QColor(th["warn"] if int(t*4)%2==0 else th["robot"])
        p.setBrush(blink_col)
        p.setPen(Qt.PenStyle.NoPen)
        dot_r = max(2, cs//12)
        p.drawEllipse(ant_x - dot_r, ant_y - cs//4 - dot_r, dot_r*2, dot_r*2)

        # Wheels
        wheel_r = max(2, cs//10)
        wheel_y = ry + cs//2 + body_r - wheel_r
        wheel_col = QColor(th["robot"]).darker(140)
        p.setBrush(wheel_col)
        p.setPen(Qt.PenStyle.NoPen)
        for wx in [x + cs//2 - body_r + wheel_r, x + cs//2 + body_r - wheel_r]:
            p.drawEllipse(wx - wheel_r, wheel_y - wheel_r, wheel_r*2, wheel_r*2)


# ═══════════════════════════════════════════════════════════════
#  HUD OVERLAY
# ═══════════════════════════════════════════════════════════════
class HUDWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.state: RobotState | None = None
        self.theme = "dark"
        self.lang  = "en"
        self._fps  = 0.0
        self._fps_buf = []
        self._last_t  = time.time()
        self.setStyleSheet("background: transparent;")

    def set_state(self, s): self.state = s; self.update()
    def set_theme(self, t): self.theme = t; self.update()
    def set_lang(self, l):  self.lang  = l; self.update()

    def tick(self):
        now = time.time()
        dt  = now - self._last_t
        self._last_t = now
        if dt > 0:
            self._fps_buf.append(1.0/dt)
            if len(self._fps_buf) > 30: self._fps_buf.pop(0)
            self._fps = sum(self._fps_buf)/len(self._fps_buf)
        self.update()

    def paintEvent(self, _e):
        if not self.state: return
        p  = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        W, H = self.width(), self.height()
        th   = THEMES[self.theme]
        tr   = TR[self.lang]
        st   = self.state
        sc   = min(W, H) / 700

        self._draw_info_panel(p, W, H, th, tr, st, sc)
        self._draw_status_bar(p, W, H, th, tr, st, sc)
        self._draw_minimap(p, W, H, th, st, sc)

        # FPS
        p.setFont(QFont("Consolas", max(8, int(9*sc))))
        p.setPen(QColor(th["text2"]))
        p.drawText(W - int(80*sc), H - int(8*sc), f"{tr['fps']}: {self._fps:.0f}")
        p.end()

    def _draw_info_panel(self, p, W, H, th, tr, st, sc):
        bw = int(170 * sc)
        bh = int(230 * sc)
        px, py = int(10*sc), int(10*sc)

        # Panel bg
        p.setBrush(QColor(0, 0, 0, 160))
        p.setPen(QPen(QColor(th["acc"]), 1))
        p.drawRoundedRect(px, py, bw, bh, 8, 8)

        items = [
            (tr["steps"],    str(st.steps)),
            (tr["score"],    str(st.score)),
            (tr["time"],     f"{st.elapsed:.0f}s"),
            (tr["visited"],  str(len(st.explored))),
            (tr["path_len"], str(len(st.path) - st.path_idx) if st.path else "–"),
            (tr["mode"],     tr["auto"] if st.auto else tr["manual"]),
        ]

        row_h = bh // (len(items) + 2)
        fs    = max(8, int(10*sc))
        fv    = max(9, int(11*sc))
        for i, (lbl, val) in enumerate(items):
            yy = py + row_h * (i+1)
            p.setFont(QFont("Consolas", fs))
            p.setPen(QColor(th["text2"]))
            p.drawText(px+8, yy, lbl)
            p.setFont(QFont("Consolas", fv, QFont.Weight.Bold))
            p.setPen(QColor(th["acc"]))
            p.drawText(px + bw - int(70*sc), yy, val)

        # Battery bar
        bar_y = py + bh - int(20*sc)
        bar_w = int((bw - 16) * st.battery / 100.0)
        bat_c = QColor("#ff3d5a") if st.battery < 20 else QColor("#ffab00") if st.battery < 50 else QColor("#00e676")
        p.setBrush(bat_c)
        p.setPen(Qt.PenStyle.NoPen)
        p.drawRoundedRect(px+8, bar_y, bar_w, int(10*sc), 3, 3)
        p.setBrush(Qt.BrushStyle.NoBrush)
        p.setPen(QPen(QColor(th["acc"]), 1))
        p.drawRoundedRect(px+8, bar_y, bw-16, int(10*sc), 3, 3)
        p.setFont(QFont("Consolas", max(7, int(9*sc))))
        p.setPen(QColor(th["text2"]))
        p.drawText(px+8, bar_y - int(4*sc), f"{tr['battery']}: {st.battery:.0f}%")

    def _draw_status_bar(self, p, W, H, th, tr, st, sc):
        status_map = {
            "searching": (tr["searching"], th["warn"]),
            "moving":    (tr["moving"],    th["acc"]),
            "reached":   (tr["reached"],   th["success"]),
            "stuck":     (tr["stuck"],     th["danger"]),
        }
        msg, col = status_map.get(st.status, ("–", th["text2"]))
        fs = max(11, int(14*sc))
        p.setFont(QFont("Consolas", fs, QFont.Weight.Bold))
        fm = p.fontMetrics()
        tw = fm.horizontalAdvance(msg)
        bw = tw + int(30*sc)
        bh = int(32*sc)
        bx = (W - bw) // 2
        by = int(10*sc)
        p.setBrush(QColor(0, 0, 0, 160))
        p.setPen(QPen(QColor(col), 2))
        p.drawRoundedRect(bx, by, bw, bh, bh//2, bh//2)
        p.setPen(QColor(col))
        p.drawText(bx + (bw-tw)//2, by + bh - int(8*sc), msg)

    def _draw_minimap(self, p, W, H, th, st, sc):
        mm_size = int(120 * sc)
        mm_x    = W - mm_size - int(12*sc)
        mm_y    = int(12*sc)
        cs      = mm_size / st.size

        # Background
        p.fillRect(mm_x, mm_y, mm_size, mm_size, QColor(0, 0, 0, 180))
        p.setPen(QPen(QColor(th["acc"]), 1))
        p.drawRect(mm_x, mm_y, mm_size, mm_size)

        for r in range(st.size):
            for c in range(st.size):
                x = int(mm_x + c * cs)
                y = int(mm_y + r * cs)
                w = max(1, int(cs))
                if st.grid[r][c] == 1:
                    p.fillRect(x, y, w, w, QColor(th["wall"]))
                elif (r,c) in st.explored:
                    p.fillRect(x, y, w, w, QColor(th["explored"]))

        # Path on minimap
        if st.path:
            for pr, pc in st.path[st.path_idx:]:
                x = int(mm_x + pc * cs)
                y = int(mm_y + pr * cs)
                col = QColor(th["path"])
                col.setAlpha(160)
                p.fillRect(x, y, max(1,int(cs)), max(1,int(cs)), col)

        # Target
        tr_r, tr_c = st.target
        tx = int(mm_x + tr_c * cs + cs/2)
        ty = int(mm_y + tr_r * cs + cs/2)
        p.setBrush(QColor(th["target"]))
        p.setPen(Qt.PenStyle.NoPen)
        pr_dot = max(2, int(cs*1.5))
        p.drawEllipse(tx - pr_dot, ty - pr_dot, pr_dot*2, pr_dot*2)

        # Robot
        rb_r, rb_c = st.pos
        rx = int(mm_x + rb_c * cs + cs/2)
        ry = int(mm_y + rb_r * cs + cs/2)
        p.setBrush(QColor(th["robot"]))
        p.drawEllipse(rx - pr_dot, ry - pr_dot, pr_dot*2, pr_dot*2)

        # Label
        p.setFont(QFont("Consolas", max(7, int(8*sc))))
        p.setPen(QColor(th["text2"]))
        p.drawText(mm_x, mm_y + mm_size + int(13*sc), "Mini-Map")


# ═══════════════════════════════════════════════════════════════
#  GAME PAGE
# ═══════════════════════════════════════════════════════════════
class GamePage(QWidget):
    sig_back = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme    = theme
        self.lang     = lang
        self._state: RobotState | None = None
        self._paused  = False
        self._keys    = set()
        self._t       = 0.0
        self._auto_step_acc = 0.0
        self._auto_speed    = 0.12   # seconds per step
        self._timer   = QTimer(self)
        self._timer.setInterval(16)
        self._timer.timeout.connect(self._tick)
        self._cur_env  = "warehouse"
        self._cur_algo = "astar"
        self._cur_size = "medium"
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Toolbar
        self._toolbar = self._build_toolbar()
        root.addWidget(self._toolbar)

        # Map + HUD
        self._renderer = MapRenderer(self)
        self._renderer.set_theme(self.theme)
        root.addWidget(self._renderer, 1)

        self._hud = HUDWidget(self._renderer)
        self._hud.set_theme(self.theme)
        self._hud.set_lang(self.lang)
        self._hud.setGeometry(self._renderer.rect())

        # Pause overlay
        self._pause_ov = self._build_pause_overlay()
        self._pause_ov.hide()

        # Controls hint
        tr  = TR[self.lang]
        th  = THEMES[self.theme]
        self._hint = QLabel(tr["controls"])
        self._hint.setStyleSheet(
            f"color:{th['text2']};font-size:10px;background:{th['bg2']};padding:2px 8px;")
        self._hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(self._hint)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def _build_toolbar(self):
        th = THEMES[self.theme]
        tr = TR[self.lang]
        bar = QWidget()
        bar.setStyleSheet(f"background:{th['bg2']}; border-bottom:1px solid {th['border']};")
        bar.setFixedHeight(44)
        hl  = QHBoxLayout(bar)
        hl.setContentsMargins(10, 4, 10, 4)
        hl.setSpacing(8)

        # Back
        back = QPushButton("◀ " + tr["back"])
        back.setFixedHeight(32)
        back.setStyleSheet(self._btn_style(th, th["border"]))
        back.clicked.connect(self._go_back)
        hl.addWidget(back)
        hl.addSpacing(4)

        # Auto / Manual toggle
        self._auto_btn = QPushButton("🤖 " + tr["auto"])
        self._auto_btn.setFixedHeight(32)
        self._auto_btn.setCheckable(True)
        self._auto_btn.setStyleSheet(self._btn_style(th, th["acc"]))
        self._auto_btn.clicked.connect(self._toggle_auto)
        hl.addWidget(self._auto_btn)

        # New Target
        nt = QPushButton("🎯 " + tr["new_target"])
        nt.setFixedHeight(32)
        nt.setStyleSheet(self._btn_style(th, th["success"]))
        nt.clicked.connect(self._new_target)
        hl.addWidget(nt)

        # New Map
        nm = QPushButton("🗺 " + tr["restart"])
        nm.setFixedHeight(32)
        nm.setStyleSheet(self._btn_style(th, th["warn"]))
        nm.clicked.connect(self._new_map)
        hl.addWidget(nm)

        # Speed slider
        lbl = QLabel(tr["speed"])
        lbl.setStyleSheet(f"color:{th['text2']};font-size:11px;background:transparent;")
        hl.addWidget(lbl)
        self._speed_sl = QSlider(Qt.Orientation.Horizontal)
        self._speed_sl.setRange(1, 20)
        self._speed_sl.setValue(8)
        self._speed_sl.setFixedWidth(80)
        self._speed_sl.setStyleSheet(f"QSlider::groove:horizontal{{height:4px;background:{th['border']};border-radius:2px;}}"
                                      f"QSlider::handle:horizontal{{width:14px;height:14px;margin:-5px 0;background:{th['acc']};border-radius:7px;}}"
                                      f"QSlider::sub-page:horizontal{{background:{th['acc']};border-radius:2px;}}")
        self._speed_sl.valueChanged.connect(lambda v: setattr(self, "_auto_speed", 0.25 - v*0.012))
        hl.addWidget(self._speed_sl)

        hl.addStretch()

        # Algo label
        self._algo_lbl = QLabel()
        self._algo_lbl.setStyleSheet(f"color:{th['acc']};font-size:11px;font-weight:bold;background:transparent;")
        hl.addWidget(self._algo_lbl)

        return bar

    def _btn_style(self, th, color):
        return (f"QPushButton{{background:{th['card']};color:{th['text']};"
                f"border:1px solid {color};border-radius:6px;font-size:11px;padding:0 10px;}}"
                f"QPushButton:hover{{background:{color};color:#000;}}"
                f"QPushButton:checked{{background:{color};color:#000;}}")

    def _build_pause_overlay(self):
        ov = QWidget(self)
        ov.setStyleSheet("background:rgba(0,0,0,170);")
        vl = QVBoxLayout(ov)
        vl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tr = TR[self.lang]
        th = THEMES[self.theme]

        lbl = QLabel(tr["paused"])
        lbl.setStyleSheet(f"color:{th['acc']};font-size:36px;font-weight:bold;background:transparent;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vl.addWidget(lbl)
        vl.addSpacing(20)

        for key, slot in [("resume",self._resume),("restart",self._new_map),("main_menu",self._go_back)]:
            btn = QPushButton(tr.get(key, key))
            btn.setFixedSize(200, 48)
            btn.setStyleSheet(f"QPushButton{{background:{th['card']};color:{th['text']};"
                              f"border:2px solid {th['acc']};border-radius:10px;"
                              f"font-size:14px;font-weight:bold;}}"
                              f"QPushButton:hover{{background:{th['acc']};color:#000;}}")
            btn.clicked.connect(slot)
            vl.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            vl.addSpacing(6)
        return ov

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._hud.setGeometry(self._renderer.rect())
        self._pause_ov.setGeometry(self.rect())

    def start_simulation(self, env_id, algo_id, size_id):
        self._cur_env  = env_id
        self._cur_algo = algo_id
        self._cur_size = size_id
        size = MAP_SIZES[size_id]["size"]
        grid = MapGenerator.generate(size, env_id)
        self._state = RobotState(grid, size, algo_id)
        self._renderer.set_state(self._state)
        self._hud.set_state(self._state)
        self._paused = False
        self._pause_ov.hide()
        self._t = 0.0
        self._auto_step_acc = 0.0
        tr = TR[self.lang]
        self._algo_lbl.setText(f"{AI_ALGOS[algo_id]['icon']} {tr[AI_ALGOS[algo_id]['key']]}")
        self._auto_btn.setChecked(False)
        if self._state:
            self._state.auto = False
        self.setFocus()
        if not self._timer.isActive():
            self._timer.start()

    def _tick(self):
        if self._paused or not self._state: return
        dt = 0.016
        self._t += dt
        self._state.update(dt)

        if self._state.auto:
            self._auto_step_acc += dt
            if self._auto_step_acc >= self._auto_speed:
                self._auto_step_acc = 0.0
                self._state.auto_step()

        self._renderer.tick(self._t)
        self._hud.tick()

    def keyPressEvent(self, e):
        k = e.key()
        self._keys.add(k)
        if k == Qt.Key.Key_Escape:
            self._toggle_pause()
            return
        if k == Qt.Key.Key_Space:
            self._toggle_auto()
            return
        if k == Qt.Key.Key_R:
            self._new_map()
            return
        if not self._state or self._state.auto: return
        moves = {
            Qt.Key.Key_W: (-1,0), Qt.Key.Key_Up:    (-1,0),
            Qt.Key.Key_S: (1,0),  Qt.Key.Key_Down:  (1,0),
            Qt.Key.Key_A: (0,-1), Qt.Key.Key_Left:  (0,-1),
            Qt.Key.Key_D: (0,1),  Qt.Key.Key_Right: (0,1),
        }
        if k in moves:
            self._state.manual_move(*moves[k])

    def keyReleaseEvent(self, e):
        self._keys.discard(e.key())

    def _toggle_pause(self):
        self._paused = not self._paused
        self._pause_ov.setVisible(self._paused)

    def _toggle_auto(self):
        if not self._state: return
        self._state.auto = not self._state.auto
        self._auto_btn.setChecked(self._state.auto)
        if self._state.auto:
            self._state.set_auto(True)

    def _new_target(self):
        if self._state:
            self._state.new_target()

    def _new_map(self):
        self.start_simulation(self._cur_env, self._cur_algo, self._cur_size)

    def _resume(self):
        self._paused = False
        self._pause_ov.hide()
        self.setFocus()

    def _go_back(self):
        self._timer.stop()
        self._pause_ov.hide()
        self.sig_back.emit()

    def set_theme(self, t):
        self.theme = t
        self._renderer.set_theme(t)
        self._hud.set_theme(t)

    def set_lang(self, l):
        self.lang = l
        self._hud.set_lang(l)


# ═══════════════════════════════════════════════════════════════
#  SELECT PAGE
# ═══════════════════════════════════════════════════════════════
class SelectPage(QWidget):
    sig_start = pyqtSignal(str, str, str)
    sig_back  = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang  = lang
        self._sel_env   = "warehouse"
        self._sel_algo  = "astar"
        self._sel_size  = "medium"
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(20,20,20,20)
        self._refresh()

    def _refresh(self):
        tr = TR[self.lang]
        th = THEMES[self.theme]
        while self._main_layout.count():
            item = self._main_layout.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.setStyleSheet(f"background:{th['bg']};color:{th['text']};")

        title = QLabel(tr["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{th['acc']};font-size:28px;font-weight:bold;background:transparent;")
        self._main_layout.addWidget(title)
        self._main_layout.addSpacing(8)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background:transparent;border:none;")
        inner = QWidget(); inner.setStyleSheet("background:transparent;")
        vl    = QVBoxLayout(inner); vl.setSpacing(14)

        # Environment
        vl.addWidget(self._sec_lbl(tr["choose_env"], th))
        vl.addLayout(self._row(ENVS, "key", self._sel_env, lambda i: self._sel("env",i), th, tr))

        # AI algo
        vl.addWidget(self._sec_lbl(tr["choose_ai"], th))
        vl.addLayout(self._row(AI_ALGOS, "key", self._sel_algo, lambda i: self._sel("algo",i), th, tr))

        # Size
        vl.addWidget(self._sec_lbl(tr["choose_size"], th))
        vl.addLayout(self._row(MAP_SIZES, "key", self._sel_size, lambda i: self._sel("size",i), th, tr))

        scroll.setWidget(inner)
        self._main_layout.addWidget(scroll, 1)
        self._main_layout.addSpacing(10)

        row = QHBoxLayout()
        for lbl, slot, col in [(tr["back"],self.sig_back.emit,th["border"]),(tr["start"],self._on_start,th["acc"])]:
            btn = QPushButton(lbl)
            btn.setFixedHeight(48)
            btn.setStyleSheet(f"QPushButton{{background:{th['card']};color:{th['text']};"
                              f"border:2px solid {col};border-radius:10px;"
                              f"font-size:15px;font-weight:bold;padding:0 24px;}}"
                              f"QPushButton:hover{{background:{col};color:#000;}}")
            btn.clicked.connect(slot)
            row.addWidget(btn)
        row.insertStretch(1)
        self._main_layout.addLayout(row)

    def _sec_lbl(self, text, th):
        l = QLabel(text)
        l.setStyleSheet(f"color:{th['text2']};font-size:13px;font-weight:bold;background:transparent;")
        return l

    def _row(self, data, key_field, sel_id, cb, th, tr):
        hl = QHBoxLayout(); hl.setSpacing(10)
        for iid, info in data.items():
            lk  = info.get(key_field, iid)
            lbl = tr.get(lk, iid)
            ico = info.get("icon","")
            sel = iid == sel_id
            btn = QPushButton(f"{ico}\n{lbl}")
            btn.setFixedSize(115, 68)
            btn.setStyleSheet(
                f"QPushButton{{background:{'rgba(0,229,255,0.15)' if sel else th['card']};"
                f"color:{th['acc'] if sel else th['text']};"
                f"border:{'2px solid '+th['acc'] if sel else '1px solid '+th['border']};"
                f"border-radius:10px;font-size:11px;font-weight:bold;}}"
                f"QPushButton:hover{{background:{th['card2']};border:2px solid {th['acc']};}}")
            _id = iid
            btn.clicked.connect(lambda _, i=_id: cb(i))
            hl.addWidget(btn)
        hl.addStretch()
        return hl

    def _sel(self, kind, val):
        if kind=="env":  self._sel_env  = val
        if kind=="algo": self._sel_algo = val
        if kind=="size": self._sel_size = val
        self._refresh()

    def _on_start(self):
        self.sig_start.emit(self._sel_env, self._sel_algo, self._sel_size)

    def set_theme(self, t): self.theme=t; self._refresh()
    def set_lang(self, l):  self.lang=l;  self._refresh()


# ═══════════════════════════════════════════════════════════════
#  SETTINGS PAGE
# ═══════════════════════════════════════════════════════════════
class SettingsPage(QWidget):
    sig_back         = pyqtSignal()
    sig_theme_change = pyqtSignal(str)
    sig_lang_change  = pyqtSignal(str)

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme=theme; self.lang=lang
        self._ml = QVBoxLayout(self)
        self._ml.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._refresh()

    def _refresh(self):
        tr=TR[self.lang]; th=THEMES[self.theme]
        while self._ml.count():
            item=self._ml.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.setStyleSheet(f"background:{th['bg']};color:{th['text']};")

        t=QLabel(tr["settings"])
        t.setAlignment(Qt.AlignmentFlag.AlignCenter)
        t.setStyleSheet(f"color:{th['acc']};font-size:28px;font-weight:bold;")
        self._ml.addWidget(t)
        self._ml.addSpacing(20)

        card=QWidget()
        card.setStyleSheet(f"background:{th['card']};border-radius:14px;")
        card.setFixedWidth(380)
        cl=QVBoxLayout(card); cl.setSpacing(16); cl.setContentsMargins(28,28,28,28)

        for section, opts, getter, signal in [
            (tr["theme"], [("dark",tr["dark"]),("light",tr["light"])],
             lambda: self.theme, self._chg_theme),
            (tr["lang"],  [("en","English"),("fa","فارسی"),("zh","中文")],
             lambda: self.lang,  self._chg_lang),
        ]:
            lbl=QLabel(section)
            lbl.setStyleSheet(f"color:{th['text2']};font-size:12px;background:transparent;")
            cl.addWidget(lbl)
            row=QHBoxLayout(); row.setSpacing(8)
            for oid, oname in opts:
                sel=oid==getter()
                btn=QPushButton(oname)
                btn.setFixedHeight(38)
                btn.setStyleSheet(
                    f"QPushButton{{background:{'rgba(0,229,255,0.2)' if sel else th['card2']};"
                    f"color:{th['acc'] if sel else th['text']};"
                    f"border:{'2px solid '+th['acc'] if sel else '1px solid '+th['border']};"
                    f"border-radius:8px;font-size:12px;font-weight:bold;}}"
                    f"QPushButton:hover{{background:{th['card2']};border:2px solid {th['acc']};}}")
                _o=oid
                btn.clicked.connect(lambda _,o=_o,s=signal: s(o))
                row.addWidget(btn)
            cl.addLayout(row)

        self._ml.addWidget(card,alignment=Qt.AlignmentFlag.AlignCenter)
        self._ml.addSpacing(24)
        bb=QPushButton(tr["back"])
        bb.setFixedSize(160,46)
        bb.setStyleSheet(f"QPushButton{{background:{th['card']};color:{th['text']};"
                         f"border:2px solid {th['border']};border-radius:10px;font-size:14px;font-weight:bold;}}"
                         f"QPushButton:hover{{background:{th['border']};}}")
        bb.clicked.connect(self.sig_back.emit)
        self._ml.addWidget(bb,alignment=Qt.AlignmentFlag.AlignCenter)

    def _chg_theme(self,t): self.theme=t; self.sig_theme_change.emit(t); self._refresh()
    def _chg_lang(self,l):  self.lang=l;  self.sig_lang_change.emit(l);  self._refresh()
    def set_theme(self,t):  self.theme=t; self._refresh()
    def set_lang(self,l):   self.lang=l;  self._refresh()


# ═══════════════════════════════════════════════════════════════
#  MENU PAGE
# ═══════════════════════════════════════════════════════════════
class MenuPage(QWidget):
    sig_play     = pyqtSignal()
    sig_settings = pyqtSignal()
    sig_quit     = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme=theme; self.lang=lang
        self._anim_t=0.0
        self._at = QTimer(self); self._at.timeout.connect(self._anim); self._at.start(30)
        self._ml = QVBoxLayout(self)
        self._ml.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._refresh()

    def _anim(self): self._anim_t+=0.03; self.update()

    def _refresh(self):
        tr=TR[self.lang]; th=THEMES[self.theme]
        while self._ml.count():
            item=self._ml.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.setStyleSheet(f"background:{th['bg']};color:{th['text']};")
        self._ml.addStretch(2)

        ico=QLabel("🤖"); ico.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ico.setStyleSheet("font-size:80px;background:transparent;")
        self._ml.addWidget(ico)

        title=QLabel(tr["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{th['acc']};font-size:42px;font-weight:900;"
                             f"letter-spacing:3px;background:transparent;")
        self._ml.addWidget(title)

        sub=QLabel("AI Navigation · PyQt6")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setStyleSheet(f"color:{th['text2']};font-size:13px;background:transparent;")
        self._ml.addWidget(sub)
        self._ml.addSpacing(40)

        for key,slot,prim in [("play",self.sig_play.emit,True),
                               ("settings",self.sig_settings.emit,False),
                               ("quit",self.sig_quit.emit,False)]:
            btn=QPushButton(tr[key])
            btn.setFixedSize(260,56)
            if prim:
                btn.setStyleSheet(
                    f"QPushButton{{background:qlineargradient(x1:0,y1:0,x2:1,y2:0,"
                    f"stop:0 {th['acc']},stop:1 {th['acc2']});"
                    f"color:#000;border-radius:16px;font-size:18px;"
                    f"font-weight:900;letter-spacing:2px;border:none;}}"
                    f"QPushButton:pressed{{padding-top:2px;}}")
            else:
                btn.setStyleSheet(
                    f"QPushButton{{background:{th['card']};color:{th['text']};"
                    f"border:2px solid {th['border']};border-radius:14px;"
                    f"font-size:15px;font-weight:bold;}}"
                    f"QPushButton:hover{{border-color:{th['acc']};color:{th['acc']};}}")
            btn.clicked.connect(slot)
            self._ml.addWidget(btn,alignment=Qt.AlignmentFlag.AlignCenter)
            self._ml.addSpacing(8)

        self._ml.addStretch(3)
        ver=QLabel("v1.0 | PyQt6 Robot Navigator")
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ver.setStyleSheet(f"color:{th['text2']};font-size:10px;background:transparent;")
        self._ml.addWidget(ver)
        self._ml.addSpacing(8)

    def paintEvent(self, e):
        super().paintEvent(e)
        p=QPainter(self); W,H=self.width(),self.height()
        th=THEMES[self.theme]; t=self._anim_t
        p.setPen(Qt.PenStyle.NoPen)
        random.seed(7)
        for i in range(35):
            x=(random.random()*W + math.cos(t*0.6+i*1.3)*50)%W
            y=(random.random()*H - t*15*(0.2+random.random()*0.8))%H
            r=random.randint(1,3)
            a=int(30+random.random()*70)
            c=QColor(th["acc"]); c.setAlpha(a)
            p.setBrush(c); p.drawEllipse(int(x),int(y),r*2,r*2)
        p.end()

    def set_theme(self,t): self.theme=t; self._refresh()
    def set_lang(self,l):  self.lang=l;  self._refresh()


# ═══════════════════════════════════════════════════════════════
#  MAIN WINDOW
# ═══════════════════════════════════════════════════════════════
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme="dark"; self.lang="en"
        self.setWindowTitle(TR[self.lang]["title"])
        self.setMinimumSize(800,600)
        self.resize(1200,760)
        self._build()

    def _build(self):
        self._stack=QStackedWidget()
        self.setCentralWidget(self._stack)

        self._menu_pg     = MenuPage(self.theme,self.lang)
        self._sel_pg      = SelectPage(self.theme,self.lang)
        self._set_pg      = SettingsPage(self.theme,self.lang)
        self._game_pg     = GamePage(self.theme,self.lang)

        for pg in [self._menu_pg,self._sel_pg,self._set_pg,self._game_pg]:
            self._stack.addWidget(pg)

        self._menu_pg.sig_play.connect(    lambda: self._stack.setCurrentIndex(1))
        self._menu_pg.sig_settings.connect(lambda: self._stack.setCurrentIndex(2))
        self._menu_pg.sig_quit.connect(self.close)

        self._sel_pg.sig_back.connect( lambda: self._stack.setCurrentIndex(0))
        self._sel_pg.sig_start.connect(self._start_game)

        self._set_pg.sig_back.connect(         lambda: self._stack.setCurrentIndex(0))
        self._set_pg.sig_theme_change.connect( self._apply_theme)
        self._set_pg.sig_lang_change.connect(  self._apply_lang)

        self._game_pg.sig_back.connect(lambda: self._stack.setCurrentIndex(0))
        self._stack.setCurrentIndex(0)

    def _start_game(self, env_id, algo_id, size_id):
        self._game_pg.start_simulation(env_id, algo_id, size_id)
        self._stack.setCurrentIndex(3)
        self._game_pg.setFocus()

    def _apply_theme(self, t):
        self.theme=t
        for pg in [self._menu_pg,self._sel_pg,self._set_pg,self._game_pg]:
            pg.set_theme(t)

    def _apply_lang(self, l):
        self.lang=l
        self.setWindowTitle(TR[l]["title"])
        for pg in [self._menu_pg,self._sel_pg,self._set_pg,self._game_pg]:
            pg.set_lang(l)


# ═══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════
def main():
    app=QApplication(sys.argv)
    app.setApplicationName("Robot Navigator")
    app.setStyle("Fusion")
    f=QFont(); f.setFamily("Segoe UI"); f.setPointSize(10); app.setFont(f)
    win=MainWindow(); win.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
