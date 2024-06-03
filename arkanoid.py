import pygame
import random

# Inizializza Pygame
pygame.init()

# Costanti
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_SIZE = 10
BRICK_WIDTH, BRICK_HEIGHT = 10, 10  # Ridotto per rappresentare i "pixel"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Crea la finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Clock
clock = pygame.time.Clock()

# Paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = -5

# Variabili di gioco
lives = 3
score = 0
current_level = 0
bricks = []

# Variabili per gli oggetti speciali
items = []

# Font per il punteggio e messaggi
font = pygame.font.SysFont('Arial', 24)
game_over_font = pygame.font.SysFont('Arial', 48)

# Funzioni per gestire i livelli
def create_level(level):
    global bricks
    bricks.clear()
    if level == 0:
        text = [
            " SSSSS  III  M   M  OOO  N   N  EEEEE  TTTTT  EEEEE  OOO  DDDD  OOO  RRRR  III",
            "S       I   MM MM O   O NN  N  E        T    E     O   O D   D O   O R   R  I",
            " SSS    I   M M M O   O N N N  EEEE     T    EEEE  O   O D   D O   O RRRR   I",
            "    S   I   M   M O   O N  NN  E        T    E     O   O D   D O   O R   R  I",
            "SSSSS  III  M   M  OOO  N   N  EEEEE    T    EEEEE  OOO  DDDD  OOO  R   R III",
        ]
        offset_x = (WIDTH - (len(text[0]) * (BRICK_WIDTH + 1))) // 2
        for row_index, row in enumerate(text):
            for col_index, char in enumerate(row):
                if char != " ":
                    brick_x = col_index * (BRICK_WIDTH + 1) + offset_x
                    brick_y = row_index * (BRICK_HEIGHT + 1) + 50
                    brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
                    bricks.append((brick, random.choice(COLORS)))

create_level(current_level)

# Funzione per disegnare oggetti
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))
    if game_over:
        game_over_text = game_over_font.render("Game Over! Press Enter to Restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()

# Funzione per gestire la collisione
def ball_collision():
    global ball_speed_x, ball_speed_y, lives, current_level, score, game_over
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(paddle):
        ball_speed_y *= -1
    for brick, color in bricks:
        if ball.colliderect(brick):
            bricks.remove((brick, color))
            ball_speed_y *= -1
            drop_item(brick)
            score += 10
            break

# Funzione per far cadere oggetti speciali dai mattoni
def drop_item(brick):
    if random.random() < 0.3:
        item_type = random.choice(["life", "grow", "shrink"])
        item = (pygame.Rect(brick.left, brick.top, BRICK_WIDTH, BRICK_HEIGHT), item_type)
        items.append(item)

# Funzione per gestire il reset del gioco
def reset_game():
    global lives, ball_speed_x, ball_speed_y, current_level, score, game_over
    lives = 3
    score = 0
    ball_speed_x = 5 * random.choice((1, -1))
    ball_speed_y = -5
    current_level = 0
    create_level(current_level)
    ball.topleft = (WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)
    paddle.topleft = (WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30)
    game_over = False

# Funzione per gestire gli oggetti speciali
def handle_items():
    global lives, PADDLE_WIDTH
    for item, item_type in items:
        item[0].move_ip(0, 5)
        if paddle.colliderect(item[0]):
            if item_type == "life":
                lives += 1
            elif item_type == "grow":
                PADDLE_WIDTH += 20
                paddle.width = PADDLE_WIDTH
            elif item_type == "shrink":
                lives -= 1
            items.remove(item)
        elif item[0].top > HEIGHT:
            items.remove(item)

# Variabili di stato
game_over = False

# Loop principale del gioco
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_over:
                reset_game()
    
    if not game_over:
        # Movimento del paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-10, 0)
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.move_ip(10, 0)
        
        # Movimento della pallina
        ball.move_ip(ball_speed_x, ball_speed_y)
        ball_collision()
        
        # Gestione degli oggetti speciali
        handle_items()
        
        # Controllo se la pallina esce dallo schermo
        if ball.top > HEIGHT:
            game_over = True
        
        # Controllo se tutti i mattoni sono stati distrutti
        if not bricks:
            current_level += 1
            if current_level < len(LEVELS):
                create_level(current_level)
            else:
                print("You Win! Restarting the game...")
                reset_game()
    
    # Disegna tutto
    draw()

pygame.quit()
