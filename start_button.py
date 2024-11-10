import pygame


class StartButton():
    COLORS = {"blue": (99, 153, 244), "red":(192, 76, 76), "green":(50, 183, 80), "black":(0, 0, 0), "white":(255, 255, 255)}

    def __init__(self, width, height, font_size, window):
        self.width = width
        self.height = height
        self.font_size = font_size
        self.window = window
        self.text = "Start"
        self.paused = False # Add ‘pause’ function to represent status

        self.rect = None # rectangle object for collision detection
 
    def draw(self):
        """
        Draw the button rectangle on window
        """
        font = pygame.font.Font("font/roboto_mono.ttf", self.font_size)
        text = font.render(self.text, True, self.COLORS["red"])
        button = text.get_rect() # get the button rectangle
        button.center = (self.width // 2, self.height * 3 // 4)

        self.window.blit(text, button)

        self.rect = button

    def get_button_rect(self):
        return self.rect
    
    def set_paused(self):
        self.text = "Pause"
        self.paused = True
    
    def set_started(self):
        self.text = "Start"
        self.paused = False

    def toggle_text(self):
        if self.text == "Start":
            self.text = "Pause"
        elif self.text == "Pause":
            self.text = "Start"


