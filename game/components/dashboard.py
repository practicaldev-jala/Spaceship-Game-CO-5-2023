import pygame
class Dashboard:
    def __init__(self):
        self.data = {
            "score": 0,
            "enemies": {},
            "deaths": 0,   
            "duration": 0
        }
        
        self.history = []
    
    def add_data_to_history(self):
        self.history.append(self.data)
        
    def set_score(self, score):
        self.data["score"] = score
        
    def set_enemies(self, enemies):
        self.data["enemies"] = enemies
    
    def set_deaths(self, deaths):
        self.data["deaths"] = deaths

    def set_duration_time(self, time):
        self.data["duration"] = time
    
    def get_score(self):
        return self.data["score"]
        
    def get_enemies(self):
        return self.data["enemies"]
    
    def get_deaths(self):
        return self.data["deaths"]

    def get_duration_time(self):
        return self.data["duration"]

    def get_max_score(self):
        max_score = 0
        for data in self.history:
            if data["score"] > max_score:
                max_score = data["score"]
        return max_score

    def reset(self):
        self.data = {
            "score": 0,
            "enemies": {},
            "deaths": 0,   
            "started_at": 0,
            "finished_at": 0,
            "duration": 0
        }