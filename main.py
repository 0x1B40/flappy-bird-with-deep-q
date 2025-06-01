import pygame
import asyncio
import time
from game import FlappyBirdGame, FLAP_VEL
from dqn import DQNAgent
from render import FlappyBirdRenderer

pygame.init()

async def main():
    try:
        game = FlappyBirdGame()
        agent = DQNAgent(state_dim=4, action_dim=2)
        renderer = FlappyBirdRenderer()
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game.manual_mode:
                        if game.game_over:
                            game.reset()
                        else:
                            game.bird_vel = FLAP_VEL
                            renderer.play_flap_sound()
                    if event.key == pygame.K_m:
                        game.manual_mode = not game.manual_mode
                    if event.key == pygame.K_r and game.manual_mode and game.game_over:
                        game.reset()

            if not game.game_over:
                state = game.get_state()
                action = agent.get_action(state) if not game.manual_mode else 0
                next_state, reward, done = game.step(action)
                if action == 1 and not game.manual_mode:
                    renderer.play_flap_sound()
                if reward == 1.0:
                    renderer.play_point_sound()
                if done and not game.manual_mode:
                    renderer.play_crash_sound()
                if not game.manual_mode:
                    agent.train(state, action, reward, next_state, done)
            else:
                if not game.manual_mode:
                    renderer.play_crash_sound()
                    await asyncio.sleep(1.0)
                    game.reset()

            renderer.render(game)
            clock.tick(60)
            await asyncio.sleep(1.0 / 60)
    except Exception as e:
        raise
    finally:
        pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())