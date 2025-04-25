import random
import pygame
import sys

pygame.init()
pygame.mixer.init()

#music
dice_roll_sound = pygame.mixer.Sound('dice_roll.mp3')
pygame.mixer.music.load("elevator_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Game")

BLACK = (0, 0, 0)
FELT_GREEN = (34, 139, 34)
font = pygame.font.SysFont(None, 60)

button_text = font.render("Play Again", True, FELT_GREEN)
button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
button_color = BLACK
button_hover_color = BLACK

dice_images = [
    pygame.transform.scale(pygame.image.load(f'dice{i}.png'), (80, 80))
    for i in range(1, 7)
]

# Dice rolls
player_dice = []
dealer_dice = []

def reset_game():
    screen.fill(BLACK)
    pygame.display.update()

def draw_button(mouse_pos):
    color = button_hover_color if button_rect.collidepoint(mouse_pos) else button_color
    pygame.draw.rect(screen, color, button_rect.inflate(20, 20), border_radius=12)
    screen.blit(button_text, button_rect)

def roll_dice():
    dice_roll_sound.play()
    
    global player_dice, dealer_dice
    player_dice = [random.randint(1, 6) for _ in range(6)]
    dealer_dice = [random.randint(1, 6) for _ in range(6)]

    player_total = sum(player_dice)
    dealer_total = sum(dealer_dice)

    print(f"You rolled {player_dice}")
    print(f"The dealer rolled {dealer_dice}")
    print(f"Your total combined number is {player_total}")
    print(f"The dealer's total combined number is {dealer_total}")

    if player_total > dealer_total:
        print("Congratulations! You've won!!!")
    elif player_total < dealer_total:
        print("You've lost!")
    else:
        print("It's a tie!")

def draw_dice():
    dealer_label = font.render("DEALER", True, FELT_GREEN)
    player_label = font.render("PLAYER", True, FELT_GREEN)

    screen.blit(dealer_label, (WIDTH // 2 - dealer_label.get_width() // 2, 50))
    screen.blit(player_label, (WIDTH // 2 - player_label.get_width() // 2, 370))

    total_row_width = 6 * 80 + 5 * 40  # 680px
    start_x = (WIDTH - total_row_width) // 2

    #dealer dice
    for i in range(6):
        x = start_x + i * (80 + 40)
        screen.blit(dice_images[dealer_dice[i] - 1], (x, 120))
    #player dice
    for i in range(6):
        x = start_x + i * (80 + 40)
        screen.blit(dice_images[player_dice[i] - 1], (x, 440))

def main():
    running = True
    while running:
        reset_game()
        roll_dice()
        screen.fill(BLACK)
        draw_dice()
        pygame.display.update()

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
