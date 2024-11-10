import pygame

class IdInputBox():
    COLORS = {"blue": (99, 153, 244), "red": (192, 76, 76), "green": (50, 183, 80), "black": (0, 0, 0), "pink": (224, 180, 210)}

    def __init__(self, width, height, window):
        self.width = width
        self.height = height
        self.font_size = 22
        self.window = window
        self.text = ""
        self.user_id = "" # final user id

        self.active = False

    def draw(self):
        font = pygame.font.Font("font/roboto_mono.ttf", self.font_size)
        text_rect = font.render(self.text, True, self.COLORS["black"])
        
        id_input_box = text_rect.get_rect()
        id_input_box.center = (self.width // 1.2 + 50, 20)

        self.window.blit(text_rect, id_input_box)

        self.rect = id_input_box

    def get_input_rect(self):
        return self.rect
