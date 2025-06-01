import pygame
import numpy as np
from pygame import sndarray
import os

# Constants
WIDTH, HEIGHT = 400, 600
BIRD_X = 100
BIRD_SIZE = 30
PIPE_WIDTH = 50
PIPE_GAP = 150
ASSETS_PATH = "assets"

class FlappyBirdRenderer:
    def __init__(self):
        pygame.display.quit()
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.font = pygame.font.SysFont(None, 36)
        self.frame_count = 0

        assets_exist = os.path.isdir(ASSETS_PATH)

        if assets_exist:
            try:
                self.bird_sprite_1 = pygame.image.load(os.path.join(ASSETS_PATH, "bird1.png")).convert_alpha()
                self.bird_sprite_1 = pygame.transform.scale(self.bird_sprite_1, (BIRD_SIZE, BIRD_SIZE))
            except:
                self.bird_sprite_1 = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
                self.bird_sprite_1.fill((255, 255, 0))

            try:
                self.bird_sprite_2 = pygame.image.load(os.path.join(ASSETS_PATH, "bird2.png")).convert_alpha()
                self.bird_sprite_2 = pygame.transform.scale(self.bird_sprite_2, (BIRD_SIZE, BIRD_SIZE))
            except:
                self.bird_sprite_2 = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
                self.bird_sprite_2.fill((255, 200, 0))

            try:
                self.pipe_sprite_full = pygame.image.load(os.path.join(ASSETS_PATH, "pipe.png")).convert_alpha()
                self.pipe_sprite_full = pygame.transform.scale(self.pipe_sprite_full, (PIPE_WIDTH, HEIGHT))
            except:
                self.pipe_sprite_full = pygame.Surface((PIPE_WIDTH, HEIGHT))
                self.pipe_sprite_full.fill((0, 128, 0))

            try:
                self.background = pygame.image.load(os.path.join(ASSETS_PATH, "background.png")).convert()
                self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
            except:
                self.background = pygame.Surface((WIDTH, HEIGHT))
                self.background.fill((135, 206, 235))

            try:
                self.ground = pygame.image.load(os.path.join(ASSETS_PATH, "ground.png")).convert()
                self.ground = pygame.transform.scale(self.ground, (WIDTH, 50))
            except:
                self.ground = pygame.Surface((WIDTH, 50))
                self.ground.fill((139, 69, 19))
        else:
            self.bird_sprite_1 = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
            self.bird_sprite_1.fill((255, 255, 0))
            self.bird_sprite_2 = pygame.Surface((BIRD_SIZE, BIRD_SIZE))
            self.bird_sprite_2.fill((255, 200, 0))
            self.pipe_sprite_full = pygame.Surface((PIPE_WIDTH, HEIGHT))
            self.pipe_sprite_full.fill((0, 128, 0))
            self.background = pygame.Surface((WIDTH, HEIGHT))
            self.background.fill((135, 206, 235))
            self.ground = pygame.Surface((WIDTH, 50))
            self.ground.fill((139, 69, 19))

        self.ground_y = HEIGHT - 50
        self.init_sounds()

    def init_sounds(self):
        sample_rate = 44100
        t = np.linspace(0, 0.1, int(0.1 * sample_rate), False)
        flap_wave = 32767 * np.sin(440 * 2 * np.pi * t)
        flap_array = np.ascontiguousarray(np.array([flap_wave, flap_wave]).T.astype(np.int16))
        self.flap_sound = sndarray.make_sound(flap_array)
        point_wave = 32767 * np.sin(880 * 2 * np.pi * t)
        point_array = np.ascontiguousarray(np.array([point_wave, point_wave]).T.astype(np.int16))
        self.point_sound = sndarray.make_sound(point_array)
        crash_wave = 32767 * np.sin(220 * 2 * np.pi * t)
        crash_array = np.ascontiguousarray(np.array([crash_wave, crash_wave]).T.astype(np.int16))
        self.crash_sound = sndarray.make_sound(crash_array)

    def render(self, game):
        self.frame_count += 1
        self.screen.blit(self.background, (0, 0))

        for pipe in game.pipes:
            gap_y = pipe['gap_y']
            top_height = gap_y - PIPE_GAP // 2
            bottom_y = gap_y + PIPE_GAP // 2
            bottom_height = HEIGHT - bottom_y

            # Scale and draw top pipe
            top_pipe_img = pygame.transform.scale(self.pipe_sprite_full, (PIPE_WIDTH, top_height))
            top_pipe_img = pygame.transform.flip(top_pipe_img, False, True)
            self.screen.blit(top_pipe_img, (pipe['x'], 0))

            # Scale and draw bottom pipe
            bottom_pipe_img = pygame.transform.scale(self.pipe_sprite_full, (PIPE_WIDTH, bottom_height))
            self.screen.blit(bottom_pipe_img, (pipe['x'], bottom_y))

        bird_sprite = self.bird_sprite_1 if (self.frame_count // 10) % 2 == 0 else self.bird_sprite_2
        self.screen.blit(bird_sprite, (BIRD_X, game.bird_y))
        self.screen.blit(self.ground, (0, self.ground_y))

        # UI text
        score_text = self.font.render(f'Score: {game.score}', True, (0, 0, 0))
        mode_text = self.font.render('Manual' if game.manual_mode else 'AI', True, (0, 0, 0))
        attempts_text = self.font.render(f'Attempts: {game.episode_count}', True, (0, 0, 0))
        failure_text = self.font.render(f'Failures: {game.failure_count}', True, (0, 0, 0)) if not game.manual_mode else None

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(mode_text, (10, 50))
        self.screen.blit(attempts_text, (10, 130))
        if failure_text:
            self.screen.blit(failure_text, (10, 90))

        pygame.display.flip()

    def play_flap_sound(self):
       # self.flap_sound.play()
       pass 

    def play_point_sound(self):
        #self.point_sound.play()
        pass

    def play_crash_sound(self):
        #self.crash_sound.play()
        pass
