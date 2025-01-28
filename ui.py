import pygame

class Text:
    '''
    An instance of this class needs to be made inside <main.py>, then render_text() can be used to 
    create text on the screen
    '''
    def __init__(self,screen, font_name = None, font_size = 36, font_color = (255,255,255)):
        
        self.screen = screen
        self.font = pygame.font.SysFont(font_name,font_size)
        self.font_color = font_color

    def render_text(self, text, position):
        # This may need to be rewritten to handle centred text
        text_surface = self.font.render(text, True, self.font_color)

        
        
    