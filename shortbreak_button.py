import pygame


class ShortbreakButton:
    COLORS = {"grey": (211, 211, 211, 128), "blue": (99, 153, 244), "red":(192, 76, 76), "green":(50, 183, 80), "black":(0, 0, 0), "white":(255, 255, 255)}

    def __init__(self, width, height, font_size, window):
        self.width = width
        self.height = height
        self.font_size = font_size
        self.window = window
        self.text = "Short Break"

        self.rect = None # rectangle object for collision detection
 
    def draw(self):
        """
        Draw the button rectangle on window
        """
        font = pygame.font.Font("font/roboto_mono.ttf", self.font_size)
        text = font.render(self.text, True, self.COLORS["blue"])
        shortbreak_button = text.get_rect() # get the button rectangle
        shortbreak_button.center = (self.width // 2, self.height // 4)

        self.window.blit(text, shortbreak_button)

        self.rect = shortbreak_button

    def get_button_rect(self):
        return self.rect

    def draw_hint(self):
        """
        Draw a background rect to indiciate it's selected
        """
        rect = pygame.Rect(0, 0, 20, 20)
        rect.center = (self.width // 2.7, self.height // 4)
        pygame.draw.rect(self.window, self.COLORS["grey"], rect)