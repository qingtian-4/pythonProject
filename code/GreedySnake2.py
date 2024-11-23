import pygame
import random

class SnakeGame:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        self.score = 0

    def run(self):
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)
                if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE: # 点击界面关闭按钮或者按Esc键结束游戏
                    game_over = True

            self.update_game_state()
            self.draw_game_state()

        pygame.quit()

    def handle_key(self, key):
        if key == pygame.K_UP or key == ord('w') and self.direction != 'DOWN':
            self.change_to = 'UP'
        if key == pygame.K_DOWN or key == ord('s') and self.direction != 'UP':
            self.change_to = 'DOWN'
        if key == pygame.K_LEFT or key == ord('a') and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if key == pygame.K_RIGHT or key == ord('d') and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def update_game_state(self):
        if self.change_to == 'UP':
            self.snake_pos[1] -= 10
        if self.change_to == 'DOWN':
            self.snake_pos[1] += 10
        if self.change_to == 'LEFT':
            self.snake_pos[0] -= 10
        if self.change_to == 'RIGHT':
            self.snake_pos[0] += 10

        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos == self.food_pos:
            self.score += 1
            self.food_pos = [random.randrange(1, (self.width//10)) * 10, random.randrange(1, (self.height//10)) * 10]
        else:
            self.snake_body.pop()

        # 蛇撞到边界后，从另一边出来
        # width
        if self.snake_pos[0] < 0:
            self.snake_pos[0] += width
            for pos in self.snake_body:
                pos[0] += width
        if self.snake_pos[0] > width - 10:
            self.snake_pos[0] -= width
            for pos in self.snake_body:
                pos[0] -= width
        # height
        if self.snake_pos[1] < 0:
            self.snake_pos[1] += height
            for pos in self.snake_body:
                pos[1] += height
        if self.snake_pos[1] > height - 10:
            self.snake_pos[1] -= height
            for pos in self.snake_body:
                pos[1] -= height

        # 检查蛇是否撞到自己
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                self.run()

    def draw_game_state(self):
        self.screen.fill((0, 0, 0))
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
        pygame.display.update()
        self.clock.tick(15)


# 设置屏幕大小
width, height = 640, 480
game = SnakeGame(width, height)
game.run()