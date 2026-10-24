
import os
import random
import sys

import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 300
FPS = 60
GROUND_Y = 240
ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

BG_COLOR = (247, 233, 200)
FG_COLOR = (83, 83, 83)
ACCENT_COLOR = (214, 120, 60)
CLOUD_COLOR = (255, 255, 255)

GRAVITY = 0.9
JUMP_VELOCITY = -15
FAST_FALL_GRAVITY = 2.7
INITIAL_SPEED = 6
MAX_SPEED = 20
SPEED_STEP = 0.5
SCORE_RATE = 0.25
SPEED_INTERVAL = 100
MENU_KEYS = (pygame.K_SPACE, pygame.K_UP, pygame.K_RETURN)


def make_dino_run(leg):
    surf = pygame.Surface((44, 47), pygame.SRCALPHA)
    pygame.draw.rect(surf, FG_COLOR, (0, 14, 32, 20))
    pygame.draw.rect(surf, FG_COLOR, (22, 0, 22, 18))
    pygame.draw.polygon(surf, FG_COLOR, [(0, 16), (-0, 22), (0, 22)])
    pygame.draw.rect(surf, FG_COLOR, (0, 10, 8, 8))
    pygame.draw.circle(surf, BG_COLOR, (34, 6), 2)
    if leg == 0:
        pygame.draw.rect(surf, FG_COLOR, (10, 34, 8, 13))
        pygame.draw.rect(surf, FG_COLOR, (24, 34, 8, 9))
    else:
        pygame.draw.rect(surf, FG_COLOR, (10, 34, 8, 9))
        pygame.draw.rect(surf, FG_COLOR, (24, 34, 8, 13))
    return surf


def make_dino_duck(leg):
    surf = pygame.Surface((59, 30), pygame.SRCALPHA)
    pygame.draw.rect(surf, FG_COLOR, (0, 10, 44, 14))
    pygame.draw.rect(surf, FG_COLOR, (38, 4, 21, 12))
    pygame.draw.circle(surf, BG_COLOR, (52, 8), 2)
    if leg == 0:
        pygame.draw.rect(surf, FG_COLOR, (12, 22, 8, 8))
        pygame.draw.rect(surf, FG_COLOR, (28, 22, 8, 6))
    else:
        pygame.draw.rect(surf, FG_COLOR, (12, 22, 8, 6))
        pygame.draw.rect(surf, FG_COLOR, (28, 22, 8, 8))
    return surf


def make_cactus(width, height):
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surf, ACCENT_COLOR, (width // 3, 0, width // 3, height))
    pygame.draw.rect(surf, ACCENT_COLOR, (0, height // 2, width // 3, height // 8))
    pygame.draw.rect(surf, ACCENT_COLOR, (0, height // 3, width // 3, height // 6))
    pygame.draw.rect(surf, ACCENT_COLOR, (2 * width // 3, height // 2, width // 3, height // 8))
    pygame.draw.rect(surf, ACCENT_COLOR, (2 * width // 3, height // 4, width // 3, height // 6))
    return surf


def make_bird(flap):
    surf = pygame.Surface((46, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, FG_COLOR, (8, 14, 30, 16))
    pygame.draw.polygon(surf, FG_COLOR, [(34, 18), (46, 14), (40, 22)])
    pygame.draw.circle(surf, FG_COLOR, (36, 14), 5)
    if flap == 0:
        pygame.draw.polygon(surf, FG_COLOR, [(16, 16), (24, 0), (30, 16)])
    else:
        pygame.draw.polygon(surf, FG_COLOR, [(16, 24), (24, 40), (30, 24)])
    return surf


def make_cloud():
    surf = pygame.Surface((64, 24), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, CLOUD_COLOR, (0, 8, 40, 16))
    pygame.draw.ellipse(surf, CLOUD_COLOR, (18, 0, 36, 20))
    pygame.draw.ellipse(surf, CLOUD_COLOR, (40, 10, 24, 14))
    return surf


def load_sprite(filename, size, fallback):
    path = os.path.join(ASSET_DIR, filename)
    if os.path.isfile(path):
        try:
            image = pygame.image.load(path).convert_alpha()
            return pygame.transform.smoothscale(image, size)
        except pygame.error:
            pass
    return fallback()


RUNNING = [
    load_sprite("dino_run_1.png", (44, 47), lambda: make_dino_run(0)),
    load_sprite("dino_run_2.png", (44, 47), lambda: make_dino_run(1)),
]
DUCKING = [
    load_sprite("dino_duck_1.png", (59, 30), lambda: make_dino_duck(0)),
    load_sprite("dino_duck_2.png", (59, 30), lambda: make_dino_duck(1)),
]
JUMPING = [load_sprite("dino_jump.png", (44, 47), lambda: make_dino_run(0))]
SMALL_CACTUS = [load_sprite("cactus_small.png", (17, 35), lambda: make_cactus(17, 35))]
LARGE_CACTUS = [load_sprite("cactus_large.png", (25, 50), lambda: make_cactus(25, 50))]
BIRD = [
    load_sprite("bird_1.png", (46, 40), lambda: make_bird(0)),
    load_sprite("bird_2.png", (46, 40), lambda: make_bird(1)),
]
CLOUD = [load_sprite("cloud.png", (64, 24), make_cloud)]


class Dinosaur:
    def __init__(self):
        self.x = 60
        self.vel_y = 0.0
        self.jumping = False
        self.ducking = False
        self.frame_index = 0
        self.anim_timer = 0
        self.image = RUNNING[0]
        self.rect = self.image.get_rect(bottomleft=(self.x, GROUND_Y))

