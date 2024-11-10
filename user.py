import pygame

class User:

    """
    Draw rectangle in the middle to show how many work times have been made
    """
    COLORS = {"grey": (211, 211, 211, 128), "blue": (99, 153, 244), "red":(192, 76, 76), "green":(50, 183, 80), "black":(0, 0, 0), "white":(255, 255, 255)}

    def __init__(self,  width, height, window, user_name, db):
        self.width = width
        self.height = height
        self.font_size = 20
        self.window = window
        
        self.user_name = user_name
        self.work_times = -1
        self.text = "Your work times: "

        self.db = db # assign the db object to user

    def draw(self):
        font = pygame.font.Font("font/roboto_mono.ttf", self.font_size)
        text = font.render(self.text + str(self.work_times), True, self.COLORS["green"])
        id_text = text.get_rect() # get the button rectangle
        id_text.center = (self.width//2, 20)

        self.window.blit(text, id_text)

    def init_row(self):
        """
        If user already exist in database, then get the work times
        Otherwise, insert a new user record
        """

        work_times = self.db.get_work_times(self.user_name)

        if work_times: # if not None(it's an existing user)
            self.work_times = work_times
        else: # work_times == None, create a new row for new user
            self.db.insert_user(self.user_name)
            self.work_times = 0

    def refresh_work_times(self):
        """
        1. update database row
        2. update text that's shown on the UI
        """
        self.db.increase_work_times(self.user_name)
        self.work_times += 1