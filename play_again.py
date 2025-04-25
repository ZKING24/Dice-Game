import random
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Play Again Example")

BLACK = (0, 0, 0)
FELT_GREEN = (34, 139, 34)
font = pygame.font.SysFont(None, 60)

button_text = font.render("Play Again", True, FELT_GREEN)
button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
button_color = BLACK
button_hover_color = BLACK

def reset_game():
    screen.fill(FELT_GREEN)
    pygame.display.update()

def draw_button(mouse_pos):
    color = button_hover_color if button_rect.collidepoint(mouse_pos) else button_color
    pygame.draw.rect(screen, color, button_rect.inflate(20, 20), border_radius=12)
    screen.blit(button_text, button_rect)

def roll_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    num4 = random.randint(1, 6)
    num5 = random.randint(1, 6)
    num6 = random.randint(1, 6)

    Dnum1 = random.randint(1, 6)
    Dnum2 = random.randint(1, 6)
    Dnum3 = random.randint(1, 6)
    Dnum4 = random.randint(1, 6)
    Dnum5 = random.randint(1, 6)
    Dnum6 = random.randint(1, 6)

    combined_num = num1 + num2 + num3 + num4 + num5 + num6
    dealer_combined = Dnum1 + Dnum2 + Dnum3 + Dnum4 + Dnum5 + Dnum6

    print(f"You rolled [{num1} {num2} {num3} {num4} {num5} {num6}]")
    print(f"\nThe dealer rolled [{Dnum1} {Dnum2} {Dnum3} {Dnum4} {Dnum5} {Dnum6}]")
    print(f"\nYour total combined number is {combined_num}")
    print(f"The dealer's total combined number is {dealer_combined}")

    if combined_num > dealer_combined:
        print("Congratulations! You've won!!!")
    elif combined_num < dealer_combined:
        print("You've lost!")
    else:
        print("It's a tie!")

def main():
    running = True
    while running:
        reset_game()
        roll_dice()
        game_running = True
        while game_running:
            mouse_pos = pygame.mouse.get_pos()
            draw_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):

                        print("\nGame Resetting...\n")
                        game_running = False
                        pygame.time.wait(1000)

            pygame.display.update()


        print("\nGame Over! Click Play Again to restart.")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()