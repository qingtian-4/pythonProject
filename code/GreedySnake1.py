import pygame
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 设置颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 设置时钟
clock = pygame.time.Clock()

# 蛇的初始位置、长度和速度
snake_pos = [100, 50]  # 蛇头
snake_body = [[100, 50], [90, 50], [80, 50]] # 蛇身
snake_speed = 15
direction = 'RIGHT' # 现在的方向
change_to = direction # 下次变化的方向

# 食物的初始位置
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# 分数
score = 0

# 游戏结束标志
game_over = False

# 游戏主循环
while not game_over:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                game_over = True

    # 确保蛇不能直接反向移动
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # 根据方向移动蛇头
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # 蛇的身体增长机制
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # 食物的生成
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # 背景
    screen.fill(black)

    # 绘制蛇
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # 绘制食物
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # 蛇撞到边界后，从另一边出来
    # width
    if snake_pos[0] < 0:
        snake_pos[0] += width
        for pos in snake_body:
            pos[0] += width
    if snake_pos[0] > width - 10:
        snake_pos[0] -= width
        for pos in snake_body:
            pos[0] -= width
    # height
    if snake_pos[1] < 0:
        snake_pos[1] += height
        for pos in snake_body:
            pos[1] += height
    if snake_pos[1] > height - 10:
        snake_pos[1] -= height
        for pos in snake_body:
            pos[1] -= height

    # 检查蛇是否撞到自己
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # 更新屏幕
    pygame.display.update()

    # 控制蛇的速度
    clock.tick(snake_speed)

# 游戏结束
pygame.quit()