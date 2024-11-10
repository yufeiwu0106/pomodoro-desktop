import pygame


class ExitButton():
    COLORS = {"blue": (99, 153, 244), "red":(192, 76, 76), "green":(50, 183, 80), "black":(0, 0, 0), "white":(255, 255, 255)}

    def __init__(self, width, height, font_size, window):
        self.width = width
        self.height = height
        self.font_size = font_size
        self.window = window
        self.text = "Exit"

        self.rect = None # rectangle object for collision detection
 
    def draw(self):
        """
        Draw the button rectangle on window
        """
        font = pygame.font.Font("font/roboto_mono.ttf", self.font_size)
        text = font.render(self.text, True, self.COLORS["blue"])
        button = text.get_rect() # get the button rectangle
        button.center = (self.width // 2, self.height * 2.5 // 2.84)

        self.window.blit(text, button)

        self.rect = button

    def get_button_rect(self):
        return self.rect

