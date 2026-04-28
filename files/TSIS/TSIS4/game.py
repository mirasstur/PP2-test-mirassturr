import pygame
import random
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, COLORS

class GameEngine:
    def __init__(self, username, settings, pb):
        self.username = username
        self.settings = settings
        self.pb = pb
        
        self.reset()

    def reset(self):
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        
        self.score = 0
        self.level = 1
        self.food_collected = 0
        self.game_over = False
        
        self.obstacles = []
        self.foods = []
        self.powerup = None
        self.powerup_timer = 0
        
        # bonus effects
        self.shield_active = False
        self.speed_modifier = 0 # 0 = normal, 1 = fast, -1 = slow
        self.effect_end_time = 0
        
        self.spawn_food(normal_only=True)

    def spawn_food(self, normal_only=False):
        self.foods = []
        # Ordinary food always spawns
        self.foods.append(self._get_valid_spawn("normal"))
        
        # poison food
        if not normal_only and random.random() < 0.3: # 30% chance
            self.foods.append(self._get_valid_spawn("poison"))

    def spawn_powerup(self):
        types = ["speed", "slow", "shield"]
        self.powerup = self._get_valid_spawn(random.choice(types))
        self.powerup_timer = pygame.time.get_ticks() + 8000 # 8 секунд на сбор

    def _get_valid_spawn(self, type_name):
        while True:
            pos = (random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1),
                   random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1))
            if pos not in self.snake and pos not in self.obstacles:
                # avoid spawn too close to snake head
                if not (abs(pos[0] - self.snake[0][0]) < 2 and abs(pos[1] - self.snake[0][1]) < 2):
                    return {"pos": pos, "type": type_name}

    def generate_obstacles(self):
        self.obstacles = []
        num_blocks = self.level * 3
        for _ in range(num_blocks):
            while True:
                pos = (random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1),
                       random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1))
                # Save zone around snake
                dist = abs(pos[0] - self.snake[0][0]) + abs(pos[1] - self.snake[0][1])
                if pos not in self.snake and pos not in [f["pos"] for f in self.foods] and dist > 3:
                    self.obstacles.append(pos)
                    break

    def update(self):
        if self.game_over:
            return

        current_time = pygame.time.get_ticks()

        # effect duration check
        if current_time > self.effect_end_time:
            self.speed_modifier = 0

        # delete not collected bonus
        if self.powerup and current_time > self.powerup_timer:
            self.powerup = None

        # spawn new powerup with 2%
        if not self.powerup and random.random() < 0.02:
            self.spawn_powerup()

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Check for collisions
        hit_wall = (new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH // CELL_SIZE or
                    new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT // CELL_SIZE)
        hit_self = new_head in self.snake
        hit_obstacle = new_head in self.obstacles

        if hit_wall or hit_self or hit_obstacle:
            if self.shield_active:
                self.shield_active = False # Shield save once
                return 
            else:
                self.game_over = True
                return

        self.snake.insert(0, new_head)
        ate_food = False

        # Check food
        for food in self.foods[:]:
            if new_head == food["pos"]:
                ate_food = True
                self.foods.remove(food)
                if food["type"] == "normal":
                    self.score += 10
                    self.food_collected += 1
                elif food["type"] == "poison":
                    # Poison: lose 5 points and shrink snake by 2 segments
                    if len(self.snake) > 2:
                        self.snake.pop()
                        self.snake.pop()
                    else:
                        self.game_over = True
                break

        if not ate_food:
            self.snake.pop() # Delete tail if no food eaten

        # Check power-up
        if self.powerup and new_head == self.powerup["pos"]:
            ptype = self.powerup["type"]
            if ptype == "speed":
                self.speed_modifier = 1
                self.effect_end_time = current_time + 5000
            elif ptype == "slow":
                self.speed_modifier = -1
                self.effect_end_time = current_time + 5000
            elif ptype == "shield":
                self.shield_active = True
            self.powerup = None
            self.score += 5

        # level up
        if self.food_collected >= 5:
            self.level += 1
            self.food_collected = 0
            if self.level >= 3:
                self.generate_obstacles()

        if len(self.foods) == 0:
            self.spawn_food()

    def get_current_fps(self, base_fps):
        if self.speed_modifier == 1: return base_fps + 10
        if self.speed_modifier == -1: return max(5, base_fps - 5)
        return base_fps + (self.level - 1) * 2

    def draw(self, surface):
        if self.settings.get("grid", False):
            for x in range(0, WINDOW_WIDTH, CELL_SIZE):
                pygame.draw.line(surface, COLORS["grid"], (x, 0), (x, WINDOW_HEIGHT))
            for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
                pygame.draw.line(surface, COLORS["grid"], (0, y), (WINDOW_WIDTH, y))

        # draw obstacles
        for obs in self.obstacles:
            pygame.draw.rect(surface, COLORS["gray"], (obs[0]*CELL_SIZE, obs[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # draw food
        for food in self.foods:
            color = COLORS["red"] if food["type"] == "normal" else COLORS["dark_red"]
            pygame.draw.rect(surface, color, (food["pos"][0]*CELL_SIZE, food["pos"][1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # draw bonus/powerup
        if self.powerup:
            colors = {"speed": COLORS["yellow"], "slow": COLORS["cyan"], "shield": COLORS["blue"]}
            pygame.draw.circle(surface, colors[self.powerup["type"]], 
                               (self.powerup["pos"][0]*CELL_SIZE + CELL_SIZE//2, self.powerup["pos"][1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2)

        #Draw snake
        snake_color = tuple(self.settings.get("color", COLORS["green"]))
        for i, segment in enumerate(self.snake):
            color = snake_color if not self.shield_active else COLORS["blue"]
            pygame.draw.rect(surface, color, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))