import pygame
import sys
import json
import os
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, COLORS
import db
from game import GameEngine

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("TSIS 4: Advanced Snake")
font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 48)

SETTINGS_FILE = "settings.json"

def load_settings():
    default_settings = {"color": [0, 255, 0], "grid": False, "sound": True}
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return default_settings

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

def draw_text(text, font, color, surface, x, y, center=True):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = (150, 150, 150) if self.rect.collidepoint(mouse_pos) else (100, 100, 100)
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, COLORS["white"], self.rect, 2)
        draw_text(self.text, font, COLORS["white"], surface, self.rect.centerx, self.rect.centery)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

def get_username():
    username = ""
    active = True
    while active:
        screen.fill(COLORS["black"])
        draw_text("Enter Username:", big_font, COLORS["white"], screen, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50)
        draw_text(username + "_", font, COLORS["yellow"], screen, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 20)
        draw_text("Press ENTER to continue", font, COLORS["gray"], screen, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip():
                    return username.strip()
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 15 and event.unicode.isprintable() and event.unicode.isascii():
                        username += event.unicode
        pygame.display.flip()

def main():
    db.init_db()
    settings = load_settings()
    clock = pygame.time.Clock()
    state = "MENU"
    username = None
    engine = None

    btn_play = Button(WINDOW_WIDTH//2 - 100, 200, 200, 50, "Play")
    btn_lb = Button(WINDOW_WIDTH//2 - 100, 280, 200, 50, "Leaderboard")
    btn_set = Button(WINDOW_WIDTH//2 - 100, 360, 200, 50, "Settings")
    btn_quit = Button(WINDOW_WIDTH//2 - 100, 440, 200, 50, "Quit")
    btn_back = Button(WINDOW_WIDTH//2 - 100, 500, 200, 50, "Back")
    btn_retry = Button(WINDOW_WIDTH//2 - 100, 350, 200, 50, "Retry")
    
    btn_toggle_grid = Button(WINDOW_WIDTH//2 - 100, 200, 200, 50, "Toggle Grid")
    btn_color = Button(WINDOW_WIDTH//2 - 100, 280, 200, 50, "Change Color")

    while True:
        screen.fill(COLORS["black"])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        if state == "MENU":
            draw_text("SNAKE DB EDITION", big_font, COLORS["green"], screen, WINDOW_WIDTH//2, 100)
            for btn in [btn_play, btn_lb, btn_set, btn_quit]:
                btn.draw(screen)
                for event in events:
                    if btn.is_clicked(event):
                        if btn == btn_play:
                            if not username:
                                username = get_username()
                            pb = db.get_personal_best(username)
                            engine = GameEngine(username, settings, pb)
                            state = "PLAY"
                        elif btn == btn_lb:
                            state = "LEADERBOARD"
                        elif btn == btn_set:
                            state = "SETTINGS"
                        elif btn == btn_quit:
                            pygame.quit(); sys.exit()

        elif state == "SETTINGS":
            draw_text("SETTINGS", big_font, COLORS["white"], screen, WINDOW_WIDTH//2, 100)
            draw_text(f"Grid: {'ON' if settings['grid'] else 'OFF'}", font, COLORS["white"], screen, WINDOW_WIDTH//2, 180)
            pygame.draw.rect(screen, tuple(settings["color"]), (WINDOW_WIDTH//2 + 120, 285, 40, 40))
            
            btn_toggle_grid.draw(screen)
            btn_color.draw(screen)
            btn_back.draw(screen)
            
            for event in events:
                if btn_toggle_grid.is_clicked(event):
                    settings["grid"] = not settings["grid"]
                    save_settings(settings)
                elif btn_color.is_clicked(event):
                    colors = [COLORS["green"], COLORS["blue"], COLORS["yellow"], COLORS["white"]]
                    curr_idx = colors.index(tuple(settings["color"])) if tuple(settings["color"]) in colors else 0
                    settings["color"] = list(colors[(curr_idx + 1) % len(colors)])
                    save_settings(settings)
                elif btn_back.is_clicked(event):
                    state = "MENU"

        elif state == "LEADERBOARD":
            draw_text("TOP 10 SCORES", big_font, COLORS["white"], screen, WINDOW_WIDTH//2, 50)
            top10 = db.get_top_10()
            y_offset = 120
            for i, row in enumerate(top10):
                # row: username, score, level, date
                txt = f"{i+1}. {row[0]} - Score: {row[1]} | Lvl: {row[2]}"
                draw_text(txt, font, COLORS["white"], screen, WINDOW_WIDTH//2, y_offset)
                y_offset += 35
                
            btn_back.rect.y = 520
            btn_back.draw(screen)
            for event in events:
                if btn_back.is_clicked(event):
                    btn_back.rect.y = 500
                    state = "MENU"

        elif state == "PLAY":
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and engine.direction != (0, 1):
                        engine.next_direction = (0, -1)
                    elif event.key == pygame.K_DOWN and engine.direction != (0, -1):
                        engine.next_direction = (0, 1)
                    elif event.key == pygame.K_LEFT and engine.direction != (1, 0):
                        engine.next_direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and engine.direction != (-1, 0):
                        engine.next_direction = (1, 0)

            engine.update()
            engine.draw(screen)
            
            # HUD
            hud = f"Score: {engine.score} | Lvl: {engine.level} | PB: {engine.pb}"
            draw_text(hud, font, COLORS["white"], screen, 10, 10, center=False)

            if engine.game_over:
                db.save_result(username, engine.score, engine.level)
                state = "GAMEOVER"
                
            clock.tick(engine.get_current_fps(FPS))
            pygame.display.flip()
            continue # Пропускаем стандартный clock.tick(FPS) в конце цикла

        elif state == "GAMEOVER":
            draw_text("GAME OVER", big_font, COLORS["red"], screen, WINDOW_WIDTH//2, 150)
            draw_text(f"Final Score: {engine.score}", font, COLORS["white"], screen, WINDOW_WIDTH//2, 230)
            draw_text(f"Level Reached: {engine.level}", font, COLORS["white"], screen, WINDOW_WIDTH//2, 270)
            
            btn_retry.draw(screen)
            btn_back.rect.y = 420
            btn_back.draw(screen)
            
            for event in events:
                if btn_retry.is_clicked(event):
                    pb = db.get_personal_best(username)
                    engine = GameEngine(username, settings, pb)
                    state = "PLAY"
                elif btn_back.is_clicked(event):
                    btn_back.rect.y = 500
                    state = "MENU"

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()