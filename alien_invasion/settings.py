# -*- coding:utf-8 -*-
class Settings():
    """存储《👽入侵》的所有设置类"""

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
    
        self.ship_speed_factor = 10
        self.ship_limit = 3

        self.bullet_speed_factor = 10
        self.bullet_width = 30
        self.bullet_height = 15 
        self.bullet_color = 60, 60, 60
        self.bullet_allowd = 3

        self.alien_speed_factor  = 5
        self.fleet_drop_speed = 20
        # 1 ➡️    -1 ⬅️  
        self.fleet_direction = 1

