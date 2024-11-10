import pygame


class Timer:
    COLOR = (169, 169, 169) # darkgrey rgb
    
    def __init__(self, width, height, font_size, window, counter):
        self.width = width
        self.height = height
        self.font_size = font_size
        self.window = window
        self.counter = counter

    def draw(self):
        font = pygame.font.Font("font/RobotoMono-Medium.ttf", 120)

        min, sec = divmod(self.counter, 60)
        text = font.render(f"{min:02d}:{sec:02d}", True, self.COLOR)

        clock_rect = text.get_rect()
        clock_rect.center = (self.width // 2, self.height // 2)

        self.window.blit(text, clock_rect)

        

        
        