import pygame
import sys
from ui import Button, draw_text, FONT, SMALL_FONT
from persistence import load_settings, save_settings, load_leaderboard, save_leaderboard
from racer import GameEngine, WIDTH, HEIGHT

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 3: Advanced Racer")
CLOCK = pygame.time.Clock()

def text_input_screen():
    username = ""
    active = True
    while active:
        SCREEN.fill((50, 50, 50))
        draw_text(SCREEN, "Enter Username:", FONT, (255, 255, 255), WIDTH//2, HEIGHT//2 - 50)
        draw_text(SCREEN, username + "_", FONT, (255, 255, 0), WIDTH//2, HEIGHT//2 + 10)
        draw_text(SCREEN, "Press ENTER to continue", SMALL_FONT, (200, 200, 200), WIDTH//2, HEIGHT//2 + 80)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip():
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 15 and event.unicode.isprintable():
                        username += event.unicode
                        
        pygame.display.flip()
        CLOCK.tick(60)

def main():
    settings = load_settings()
    leaderboard = load_leaderboard()
    
    state = "MENU"
    engine = None
    username = ""

    # buttons for main menu
    btn_play = Button(WIDTH//2 - 100, 250, 200, 50, "Play")
    btn_lb = Button(WIDTH//2 - 100, 320, 200, 50, "Leaderboard")
    btn_set = Button(WIDTH//2 - 100, 390, 200, 50, "Settings")
    btn_quit = Button(WIDTH//2 - 100, 460, 200, 50, "Quit")

    # buttons after game
    btn_retry = Button(WIDTH//2 - 100, 400, 200, 50, "Retry")
    btn_menu = Button(WIDTH//2 - 100, 470, 200, 50, "Main Menu")
    
    # buttons for settings
    btn_color = Button(WIDTH//2 - 100, 250, 200, 50, "Color: " + settings["car_color"])
    btn_diff = Button(WIDTH//2 - 100, 320, 200, 50, "Diff: " + settings["difficulty"])
    btn_back = Button(WIDTH//2 - 100, 500, 200, 50, "Back")

    while True:
        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                save_settings(settings)
                pygame.quit()
                sys.exit()

        SCREEN.fill((30, 30, 40))

        if state == "MENU":
            draw_text(SCREEN, "TSIS 3: RACER", FONT, (255, 255, 255), WIDTH//2, 150)
            for btn in [btn_play, btn_lb, btn_set, btn_quit]:
                btn.check_hover(mouse_pos)
                btn.draw(SCREEN)
                for event in events:
                    if btn.handle_event(event):
                        if btn == btn_play:
                            if not username:
                                username = text_input_screen()
                            engine = GameEngine(settings, username)
                            state = "PLAY"
                        elif btn == btn_lb: state = "LEADERBOARD"
                        elif btn == btn_set: state = "SETTINGS"
                        elif btn == btn_quit: 
                            save_settings(settings)
                            pygame.quit(); sys.exit()

        elif state == "PLAY":
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: engine.player.move(-1)
                    if event.key == pygame.K_RIGHT: engine.player.move(1)
            
            engine.update()
            engine.draw(SCREEN)
            
            if engine.is_game_over:
                # save scores
                leaderboard.append({"name": username, "score": engine.score, "distance": int(engine.distance)})
                save_leaderboard(leaderboard)
                leaderboard = load_leaderboard() # restore sorted leaderboard
                state = "GAMEOVER"

        elif state == "GAMEOVER":
            draw_text(SCREEN, "GAME OVER", FONT, (255, 50, 50), WIDTH//2, 200)
            draw_text(SCREEN, f"Score: {engine.score}", SMALL_FONT, (255, 255, 255), WIDTH//2, 260)
            draw_text(SCREEN, f"Distance: {int(engine.distance)}m", SMALL_FONT, (255, 255, 255), WIDTH//2, 290)
            
            for btn in [btn_retry, btn_menu]:
                btn.check_hover(mouse_pos)
                btn.draw(SCREEN)
                for event in events:
                    if btn.handle_event(event):
                        if btn == btn_retry:
                            engine = GameEngine(settings, username)
                            state = "PLAY"
                        elif btn == btn_menu:
                            state = "MENU"

        elif state == "SETTINGS":
            draw_text(SCREEN, "SETTINGS", FONT, (255, 255, 255), WIDTH//2, 150)
            btn_color.text = "Color: " + settings["car_color"].capitalize()
            btn_diff.text = "Diff: " + settings["difficulty"]
            
            for btn in [btn_color, btn_diff, btn_back]:
                btn.check_hover(mouse_pos)
                btn.draw(SCREEN)
                for event in events:
                    if btn.handle_event(event):
                        if btn == btn_color:
                            colors = ["blue", "red", "green", "yellow"]
                            idx = (colors.index(settings["car_color"]) + 1) % len(colors)
                            settings["car_color"] = colors[idx]
                        elif btn == btn_diff:
                            diffs = ["Easy", "Medium", "Hard"]
                            idx = (diffs.index(settings["difficulty"]) + 1) % len(diffs)
                            settings["difficulty"] = diffs[idx]
                        elif btn == btn_back:
                            save_settings(settings)
                            state = "MENU"

        elif state == "LEADERBOARD":
            draw_text(SCREEN, "TOP 10 SCORES", FONT, (255, 255, 255), WIDTH//2, 100)
            y_offset = 170
            for i, entry in enumerate(leaderboard[:10]):
                txt = f"{i+1}. {entry['name']} - {entry['score']} pts ({entry['distance']}m)"
                draw_text(SCREEN, txt, SMALL_FONT, (200, 200, 200), WIDTH//2, y_offset)
                y_offset += 35
                
            btn_back.check_hover(mouse_pos)
            btn_back.draw(SCREEN)
            for event in events:
                if btn_back.handle_event(event):
                    state = "MENU"

        pygame.display.flip()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()