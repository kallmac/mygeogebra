import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Кнопка для создания и удаления круга')

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Параметры круга
circle_radius = 50
circle_x = -100  # Начальная позиция круга за экраном
circle_y = -100

# Параметры кнопок
button_width = 200
button_height = 60
button_x = 300
button_y = 250
create_button_color = GREEN
delete_button_color = RED
button_text_color = (255, 255, 255)

# Шрифт для текста на кнопках
font = pygame.font.SysFont(None, 36)


# Функция для отрисовки кнопки
def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))  # Рисуем кнопку
    # Рисуем текст на кнопке
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface,
                (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))


# Главный цикл игры
running = True
while running:
    screen.fill(WHITE)  # Очистка экрана

    # Получаем все события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка на клик мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левый клик
                mouse_x, mouse_y = event.pos

                # Проверка, попал ли клик в область кнопки "Создать круг"
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    # При нажатии на кнопку создаем круг в центре экрана
                    if circle_x == -100 and circle_y == -100:  # Если круг еще не был создан
                        circle_x = 400  # Позиция круга по оси X
                        circle_y = 300  # Позиция круга по оси Y

                # Проверка, попал ли клик в область кнопки "Удалить круг"
                elif button_x <= mouse_x <= button_x + button_width and button_y + button_height + 20 <= mouse_y <= button_y + button_height + 20 + button_height:
                    # При нажатии на кнопку удаляем круг (устанавливаем его координаты за экран)
                    if circle_x != -100 and circle_y != -100:  # Если круг был создан
                        circle_x = -100  # Убираем круг за экран
                        circle_y = -100

    # Рисуем кнопку "Создать круг"
    draw_button("Создать круг", button_x, button_y, button_width, button_height, create_button_color, button_text_color)

    # Рисуем кнопку "Удалить круг"
    draw_button("Удалить круг", button_x, button_y + button_height + 20, button_width, button_height,
                delete_button_color, button_text_color)

    # Рисуем круг, если он активен
    if circle_x != -100 and circle_y != -100:
        pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)

    pygame.display.flip()  # Обновляем экран

pygame.quit()
sys.exit()
