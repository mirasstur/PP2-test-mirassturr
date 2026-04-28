import pygame
import random

# Константы
WIDTH, HEIGHT = 600, 800
LANES = [100, 300, 500]  # X-координаты центров полос

COLORS = {
    "red": (255, 0, 0), "blue": (0, 0, 255), "green": (0, 255, 0),
    "yellow": (255, 255, 0), "black": (0, 0, 0), "cyan": (0, 255, 255),
    "grey": (100, 100, 100), "white": (255, 255, 255), "purple": (128, 0, 128)
}

class Player:
    def __init__(self, color_name):
        self.rect = pygame.Rect(0, 0, 50, 100)
        self.rect.center = (LANES[1], HEIGHT - 120)
        self.color = COLORS.get(color_name, COLORS["blue"])
        self.speed = 5
        self.has_shield = False
        self.nitro_active = False
        self.nitro_timer = 0
        self.target_x = self.rect.centerx

    def move(self, dx):
        self.target_x += dx * 200
        self.target_x = max(LANES[0], min(self.target_x, LANES[2])) # Limit to lanes

    def update(self):
        # Smooth lane change
        if self.rect.centerx < self.target_x:
            self.rect.x += 10
        elif self.rect.centerx > self.target_x:
            self.rect.x -= 10
            
        if self.nitro_active and pygame.time.get_ticks() > self.nitro_timer: # Deactivate nitro after timer
            self.nitro_active = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.has_shield:
            pygame.draw.circle(surface, COLORS["cyan"], self.rect.center, 60, 3)
        if self.nitro_active:
            pygame.draw.rect(surface, COLORS["yellow"], (self.rect.x, self.rect.bottom, 50, 20))

class Entity:
    def __init__(self, type_name):
        self.type = type_name
        self.rect = pygame.Rect(0, -100, 50, 50)
        self.rect.centerx = random.choice(LANES)
        
        if type_name == "enemy":
            self.rect.height = 100
            self.color = COLORS["red"]
        elif type_name == "obstacle": # obstacle - препятствиe
            self.rect.height = 30
            self.color = COLORS["black"]
        elif type_name == "coin":
            self.rect.width = 30
            self.rect.height = 30
            self.color = COLORS["yellow"]
            self.value = random.choices([1, 5, 10], weights=[70, 20, 10])[0]
        elif type_name in ["nitro", "shield", "repair"]:
            self.rect.width = 40
            self.rect.height = 40
            self.color = COLORS["green"] if type_name == "repair" else (COLORS["cyan"] if type_name == "shield" else COLORS["purple"])
            
    def update(self, speed):
        self.rect.y += speed
        
    def draw(self, surface):
        if self.type == "coin":
            pygame.draw.circle(surface, self.color, self.rect.center, 15)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

class GameEngine:
    def __init__(self, settings, username):
        self.settings = settings
        self.username = username
        self.player = Player(self.settings["car_color"])
        
        self.difficulty_mult = {"Easy": 1.0, "Medium": 1.5, "Hard": 2.0}[self.settings["difficulty"]]
        self.base_speed = 5 * self.difficulty_mult
        
        self.entities = []
        self.score = 0
        self.coins = 0
        self.distance = 0
        self.is_game_over = False
        
        self.spawn_timer = 0

    def get_speed(self):
        speed = self.base_speed + (self.distance / 1000) # Increase speed as distance increases
        if self.player.nitro_active:
            speed *= 1.5
        return speed

    def safe_spawn(self, type_name):
        entity = Entity(type_name)
        # check for collisions
        for e in self.entities:
            if entity.rect.colliderect(e.rect):
                return # Cancel spawn
        self.entities.append(entity)

    def update(self):
        if self.is_game_over: return

        speed = self.get_speed()
        self.player.update()
        self.distance += speed / 10
        self.score = int(self.distance) + (self.coins * 10)

        # Spawn mechanics
        self.spawn_timer -= 1
        if self.spawn_timer <= 0:
            rand = random.random()
            if rand < 0.5: self.safe_spawn("enemy")
            elif rand < 0.7: self.safe_spawn("obstacle")
            elif rand < 0.9: self.safe_spawn("coin")
            else: self.safe_spawn(random.choice(["nitro", "shield", "repair"]))
            
            # more spawns as distance increases
            self.spawn_timer = max(30, 100 - (self.distance / 50)) 

        # Update and collision check
        for e in self.entities[:]:
            e.update(speed)
            if e.rect.top > HEIGHT:
                self.entities.remove(e)
                continue
                
            if self.player.rect.colliderect(e.rect):
                if e.type == "coin":
                    self.coins += e.value
                    self.entities.remove(e)
                elif e.type == "nitro":
                    self.player.nitro_active = True
                    self.player.nitro_timer = pygame.time.get_ticks() + 4000 # 4 seconds for nitro
                    self.entities.remove(e)
                elif e.type == "shield":
                    self.player.has_shield = True
                    self.entities.remove(e)
                elif e.type == "repair":
                    # Clear all obstacles on the screen
                    self.entities = [ent for ent in self.entities if ent.type not in ["enemy", "obstacle"]]
                    self.entities.remove(e)
                elif e.type in ["enemy", "obstacle"]:
                    if self.player.has_shield:
                        self.player.has_shield = False
                        self.entities.remove(e)
                    else:
                        self.is_game_over = True

    def draw(self, surface):
        surface.fill(COLORS["grey"])
        # draw lanes
        for x in [200, 400]:
            pygame.draw.line(surface, COLORS["white"], (x, 0), (x, HEIGHT), 5)
            
        for e in self.entities:
            e.draw(surface)
            
        self.player.draw(surface)
        
        # HUD
        font = pygame.font.SysFont("Arial", 24)
        hud_text = f"Score: {self.score} | Coins: {self.coins} | Dist: {int(self.distance)}m"
        surf = font.render(hud_text, True, COLORS["white"])
        surface.blit(surf, (10, 10))