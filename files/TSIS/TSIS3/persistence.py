import json
import os

def load_data(filepath, default_data):
    if not os.path.exists(filepath):
        return default_data
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except(json.JSONDecodeError, IOError):
        return default_data
    
def save_data(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
def load_settings():
    default_settings = {"sound" : True, "car_color": "blue", "difficulty": "Medium"}
    return load_data("setting.json", default_settings)

def save_settings(settings):
    save_data("settings.josn", settings)
    
def load_leaderboard():
    return load_data("leaderboard.json", [])

def save_leaderboard(leaderboard):
    leaderboard = sorted(leaderboard, key=lambda x: x.get("score", 0), reverse=True)[:10]
    save_data("leaderboard.json", leaderboard)
    
