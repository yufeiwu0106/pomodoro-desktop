import pygame


class IdText():
    COLORS = {"blue": (99, 153, 244), "red":(192, 76, 76), "green":(50, 183, 80), "black":(0, 0, 0), "pink": (236, 85, 120)}

    def __init__(self, width, height, font_size, window):
        self.width = width
        self.height = height
        self.font_size = 23
        self.window = window
        self.text = "User id: "

        self.rect = None # rectangle object for collision detection
 
    def draw(self):
        """
        Draw the button rectangle on window
        """
        font = pygame.font.Font("font/roboto_mono.ttf", self.font_size)
        text = font.render(self.text, True, self.COLORS["pink"])
        id_text = text.get_rect() # get the button rectangle
        id_text.center = (self.width // 1.2 - 75, 20)

        self.window.blit(text, id_text)

        self.rect = id_text

    def get_button_rect(self):
        return self.rect


