import pygame , sys
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

def main():
    reset_game()

    running = True
    while running:
        screen.fill(FELT_GREEN)
        mouse_pos = pygame.mouse.get_pos()
        draw_button(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    reset_game()

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()