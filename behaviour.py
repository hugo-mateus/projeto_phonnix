class behaviour:
    def __init__(self, mode = "none", mood = "feliz", is_ball_owner = True):
        self.mode = mode
        self.mood = mood
        self.is_ball_owner = is_ball_owner
        if self.is_ball_owner:
            print(f"Behaviour inicializado, estou com a bola e estou {self.mood}")
        else:
            print(f"Behaviour inicializado, não estou com a bola e estou {self.mood}")
    
