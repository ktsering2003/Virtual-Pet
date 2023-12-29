import pygame


class Item:
    def __init__(self, x, y, health, happiness, image_name):
        # Set up basic fields
        self.x = x
        self.y = y
        self.health = health
        self.happiness = happiness
    # Load and store the image based on the filepath
        self.image = pygame.image.load(image_name)
    # Shift the image rect so that the x and y are at the center rather than top left
        rect = self.image.get_rect()
        self.image_rect = pygame.Rect(
            x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)  # Use self.height instead of self.buttons_bar_height


class Game:
    def __init__(self):
        # Display variable
        self.width = 500
        self.height = 500
        self.background_colour = "white"
        self.buttons_bar_colour = "orange"
    # Pygame specific variable
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame Pet")
        self.clock_tick = 60
        self.clock = pygame.time.Clock()
    # Item variables
        self.image_names = ["apple.png", "icecream.png", "toy.png"]
    # Button variables
        self.apple_button = Item(
            self.width / 4, self.height / 2, 0, 0, self.image_names[0])  # Use self.height instead of self.buttons_bar_height
        self.ice_cream_button = Item(
            self.width / 2, self.height / 2, 0, 0, self.image_names[1])
        self.toy_button = Item(
            self.width * (3 / 4), self.height / 2, 0, 0, self.image_names[2])

    # Draw the screen, bar, buttons, items, pet
    def draw_everything(self):
        # Screen
        self.screen.fill(self.background_colour)
    # Buttons bar
        pygame.draw.rect(self.screen, self.buttons_bar_colour, pygame.Rect(
            0, 0, self.width, self.height))
    # Buttons
        self.screen.blit(self.apple_button.image, self.apple_button.image_rect)
    # Update
        pygame.display.update()
        self.screen.blit(self.ice_cream_button.image,
                         self.ice_cream_button.image_rect)
        self.screen.blit(self.toy_button.image, self.toy_button.image_rect)
        pygame.display.update()

    # Run the game loop
    def run(self):
        while True:
            # Handle incoming events
            for event in pygame.event.get():
                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
    # Draw
            self.draw_everything()
    # Tick clock
            self.clock.tick(self.clock_tick)


# Initialize Pygame and start running game
pygame.init()
game = Game()
game.run()
