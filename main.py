import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Взаимодействие фигур')
FPS= 60 # кадры в секунду

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметры круга
circle_radius = 40
circle_x = 200
circle_y = 200

# Переменные для отслеживания перетаскивания
dragging = False
offset_x = 0
offset_y = 0

# Главный цикл игры
running = True
while running:
    screen.fill(WHITE)  # Очистка экрана

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Проверяем, что мышь находится внутри круга
                if (event.pos[0] - circle_x) ** 2 + (event.pos[1] - circle_y) ** 2 <= circle_radius ** 2:
                    dragging = True
                    # Вычисляем смещение мыши относительно центра круга
                    offset_x = circle_x - event.pos[0]
                    offset_y = circle_y - event.pos[1]
            if event.button == 4:  # Увеличиваем радиус круга при нажатии
                circle_radius += 5
            if event.button == 5:
                circle_radius -= 5
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False  # Останавливаем перетаскивание
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Обновляем позицию круга
                circle_x = event.pos[0] + offset_x
                circle_y = event.pos[1] + offset_y
            # elif event.button == 3:  # Правая кнопка мыши
            #     # Уменьшаем радиус круга при нажатии
            #     if circle_radius > 5:
            #         circle_radius -= 5

    # Рисуем круг
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)

    pygame.display.flip()  # Обновляем экран

pygame.quit()
sys.exit()
