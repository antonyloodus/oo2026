class Crosshair:
    ch_dir = ["left", "right", "up", "down"]

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def move_crosshair(self, aim_direction:str):
        if aim_direction == "right":
            self.x += 1
        elif aim_direction == "left":
            self.x -= 1
        elif aim_direction == "up":
            self.y += 1
        elif aim_direction == "down":
            self.y -= 1
