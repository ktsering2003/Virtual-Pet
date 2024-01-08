import pygame
import sys
import os


class Item:
    def __init__(self, x, y, health, happiness, image_name):
        self.x = x
        self.y = y
        self.health = health
        self.happiness = happiness
        self.image = pygame.image.load(image_name)
        rect = self.image.get_rect()
        self.image_rect = pygame.Rect(
            x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)


class Game:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.background_colour = (255, 255, 255)
        self.buttons_bar_colour = (255, 165, 0)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Pet")
        self.clock_tick = 60
        self.clock = pygame.time.Clock()
        self.image_names = ["apple.png", "icecream.png", "toy.png"]
        self.apple_button = Item(
            self.width / 4, self.height / 2, 0, 0, self.image_names[0])
        self.ice_cream_button = Item(
            self.width / 2, self.height / 2, 0, 0, self.image_names[1])
        self.toy_button = Item(
            self.width * (3 / 4), self.height / 2, 0, 0, self.image_names[2])
        self.background_image = pygame.Surface((self.width, self.height))

        # Game variables
        self.game_time = 0

    def draw_everything(self):
        self.screen.fill(self.background_colour)
        pygame.draw.rect(self.screen, self.buttons_bar_colour, pygame.Rect(
            0, 0, self.width, self.height))
        self.screen.blit(self.apple_button.image, self.apple_button.image_rect)
        self.screen.blit(
            self.ice_cream_button.image, self.ice_cream_button.image_rect)
        self.screen.blit(self.toy_button.image, self.toy_button.image_rect)

        # Display pet stats
        font = pygame.font.Font(None, 36)
        text = font.render(
            f"Health: {self.apple_button.health} Happiness: {self.apple_button.happiness}", True, (0, 0, 0))
        self.screen.blit(text, (20, 20))

        # Display game time
        time_text = font.render(
            f"Time: {self.game_time} seconds", True, (0, 0, 0))
        self.screen.blit(time_text, (self.width - 200, 20))

        pygame.display.update()

    def handle_button_click(self, button):
        # Simulate feeding the pet
        button.health += 10
        button.happiness += 5

    def update_game_time(self):
        self.game_time += 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a button is clicked
                    if self.apple_button.image_rect.collidepoint(event.pos):
                        self.handle_button_click(self.apple_button)
                    elif self.ice_cream_button.image_rect.collidepoint(event.pos):
                        self.handle_button_click(self.ice_cream_button)
                    elif self.toy_button.image_rect.collidepoint(event.pos):
                        self.handle_button_click(self.toy_button)

            self.update_game_time()
            self.draw_everything()
            self.clock.tick(self.clock_tick)


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
