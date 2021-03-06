import pygame # 파이 게임 모듈 임포트
import random
pygame.init() # 파이 게임 초기화

# 화면 크기 설정
size = [600, 700]
SCREEN_WIDTH = size[0] # 화면 가로크기
SCREEN_HEIGHT = size[1] # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

# 폭탄 클래스 생성하기
class Bomb(pygame.sprite.Sprite):
    # 생성자
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('asset/image/bomb.png')
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 0


    def put_img(self):
        self.sx, self.sy = self.image.get_size()  # 현재 이미지에 대한 크기를 각각 sx, sy에 저장

    def show(self):
       screen.blit(self.image, (self.x, self.y))

    def fall (self):
        self.y += self.speed

    def isFallen(self):
        if self.y > 800:
            return True
        else:
            return False

    def reCreate(self):
        self.x = random.randint(0, 600 - self.sx)
        self.y = - 100
        self.speed = random.randint(3, 9)