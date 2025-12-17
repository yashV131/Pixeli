import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

# Screen & grid parameters
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Art Maker")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
COLOR = RED

rect_x1 = 50 
rect_y1 = 50
rect_width = 400
rect_height = 400
line_thickness = 5 

CELL_SIZE = 10
GRID_COLS = rect_width // CELL_SIZE
GRID_ROWS = rect_height // CELL_SIZE

# Use a 2D list for grid state
grid = [[WHITE for _ in range(GRID_ROWS)] for _ in range(GRID_COLS)]

def draw_grid(surface, x0, y0, grid):
    for x in range(GRID_COLS):
        for y in range(GRID_ROWS):
            rect = pygame.Rect(x0 + x * CELL_SIZE, y0 + y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
            color = grid[x][y]
            pygame.draw.rect(surface, color, rect)

def draw():
    text_surface = font.render('Get ready to draw!', True, WHITE)
    screen.blit(text_surface, (rect_x1, rect_y1-40))
    draw_grid(screen, rect_x1, rect_y1, grid)

def event_handler():
    global COLOR
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                # Check if click inside grid
                if (rect_x1 <= mx < rect_x1 + rect_width) and (rect_y1 <= my < rect_y1 + rect_height):
                    grid_x = (mx - rect_x1) // CELL_SIZE
                    grid_y = (my - rect_y1) // CELL_SIZE
                    grid[grid_x][grid_y] = COLOR  # Turn red (change to not grid[x][y] to allow toggle)
                    print(f'Cell clicked: ({grid_x}, {grid_y})')
            elif event.button == 3:
                mx, my = pygame.mouse.get_pos()
                # Check if click inside grid
                if (rect_x1 <= mx < rect_x1 + rect_width) and (rect_y1 <= my < rect_y1 + rect_height):
                    grid_x = (mx - rect_x1) // CELL_SIZE
                    grid_y = (my - rect_y1) // CELL_SIZE
                    grid[grid_x][grid_y] = WHITE  # Turn red (change to not grid[x][y] to allow toggle)
                    print(f'Cell clicked: ({grid_x}, {grid_y})')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_grid_as_image(grid)
                print("CTRL S CLICKED")
            if event.key == pygame.K_b:
                print("IN BLUE")
               
                COLOR = BLUE
        
                
                
    return True


def save_grid_as_image(grid, filename= "pixelart.jpg"):
    global COLOR
    width = GRID_COLS*CELL_SIZE
    height = GRID_ROWS*CELL_SIZE
    
    surf = transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    surf.fill((0, 0, 0, 0))  
   
    for x in range(GRID_COLS):
        for y in range(GRID_ROWS):
            if grid[x][y]:
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
                pygame.draw.rect(surf, (*COLOR,255), rect)
    pygame.image.save(surf,filename)
    print(f"Saved image to {filename}")
 
    
    
    
running = True
while running:
    screen.fill((0,0,0))
    draw()
    pygame.draw.rect(screen, BLUE, (rect_x1, rect_y1, rect_width, rect_height), line_thickness)
    running = event_handler()
    pygame.display.flip()

pygame.quit()