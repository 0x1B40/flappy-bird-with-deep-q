import pygame
import random
import numpy as np

# Game constants
WIDTH, HEIGHT = 400, 600
BIRD_X = 100
BIRD_SIZE = 30
PIPE_WIDTH = 50
PIPE_GAP = 150
PIPE_SPEED = 3
GRAVITY = 0.6
FLAP_VEL = -10
PIPE_SPAWN_INTERVAL = 100

class FlappyBirdGame:
    def __init__(self):
        self.bird_y = HEIGHT // 2
        self.bird_vel = 0
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.frame_count = 0
        self.episode_count = 0
        self.failure_count = 0
        self.manual_mode = True
        self.spawn_pipe()

    def spawn_pipe(self):
        gap_y = random.randint(150, HEIGHT - 150 - PIPE_GAP)
        pipe = {'x': WIDTH, 'gap_y': gap_y, 'passed': False}
        self.pipes.append(pipe)

    def get_state(self):
        state = np.empty(4, dtype=np.float32)
        if not self.pipes:
            state[0] = self.bird_y / HEIGHT
            state[1] = self.bird_vel / 10
            state[2] = 1.0
            state[3] = 0.5
        else:
            next_pipe = self.pipes[0]
            state[0] = self.bird_y / HEIGHT
            state[1] = self.bird_vel / 10
            state[2] = (next_pipe['x'] - BIRD_X) / WIDTH
            state[3] = next_pipe['gap_y'] / HEIGHT
        state = np.ascontiguousarray(state, dtype=np.float32)
        return state

    def step(self, action):
        reward = 0.1
        self.frame_count += 1

        if action == 1:
            self.bird_vel = FLAP_VEL

        self.bird_vel += GRAVITY
        self.bird_y += self.bird_vel

        if self.pipes:
            gap_center = self.pipes[0]['gap_y']
            distance_to_gap = abs(self.bird_y - gap_center) / HEIGHT
            reward -= distance_to_gap * 0.2

        bird_rect = pygame.Rect(BIRD_X, self.bird_y, BIRD_SIZE, BIRD_SIZE)
        for pipe in self.pipes:
            pipe['x'] -= PIPE_SPEED
            top_pipe = pygame.Rect(pipe['x'], 0, PIPE_WIDTH, pipe['gap_y'] - PIPE_GAP // 2)
            bottom_pipe = pygame.Rect(pipe['x'], pipe['gap_y'] + PIPE_GAP // 2, PIPE_WIDTH, HEIGHT)
            if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
                self.game_over = True
                reward = -1.0
                if not self.manual_mode:
                    self.failure_count += 1

        if self.bird_y < 0 or self.bird_y > HEIGHT:
            self.game_over = True
            reward = -1.0
            if not self.manual_mode:
                self.failure_count += 1

        if self.pipes and self.pipes[0]['x'] < BIRD_X and not self.pipes[0]['passed']:
            self.pipes[0]['passed'] = True
            self.score += 1
            reward = 1.0

        if self.frame_count % PIPE_SPAWN_INTERVAL == 0:
            self.spawn_pipe()

        self.pipes = [pipe for pipe in self.pipes if pipe['x'] + PIPE_WIDTH > 0]
        return self.get_state(), reward, self.game_over

    def reset(self):
        self.bird_y = HEIGHT // 2
        self.bird_vel = 0
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.frame_count = 0
        self.episode_count += 1
        self.spawn_pipe()