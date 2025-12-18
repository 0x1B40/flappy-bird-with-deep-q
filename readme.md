# Flappy Bird with Deep Q-Learning

An intelligent implementation of the classic Flappy Bird game featuring a Deep Q-Network (DQN) reinforcement learning agent that learns to play the game autonomously. This project demonstrates advanced AI techniques including experience replay, target networks, and epsilon-greedy exploration strategies.

## 🎮 Demo

[![Flappy Bird AI Gameplay](flappybird.png)](https://youtu.be/e0z_SxfxYTY)

*Click the image above to watch the AI agent learning to master Flappy Bird!*

## 🎯 Overview

This project combines classic game development with cutting-edge reinforcement learning to create an AI agent that can learn and master the Flappy Bird game. The implementation features a complete game environment built with Pygame and a sophisticated DQN agent that improves its performance through continuous learning.

The AI agent starts with no knowledge of the game and learns optimal strategies through trial and error, demonstrating the power of deep reinforcement learning in solving complex decision-making problems.

## ✨ Features

- **Complete Flappy Bird Game**: Full game mechanics with physics, collision detection, and scoring
- **Dual Gameplay Modes**: Manual player control and autonomous AI gameplay
- **Deep Q-Network Agent**: Advanced reinforcement learning implementation
- **Experience Replay**: Efficient learning through memory buffer sampling
- **Target Network**: Stable learning with periodic target network updates
- **Epsilon-Greedy Exploration**: Balanced exploration vs exploitation strategy
- **Real-time Training**: Visual feedback during AI learning process
- **Performance Tracking**: Episode counting and failure rate monitoring
- **Sound Effects**: Audio feedback for game events (flaps, points, crashes)

## 🧠 AI Implementation

### Deep Q-Learning Architecture
- **State Space**: 4-dimensional input (bird position, velocity, next pipe distance, gap position)
- **Action Space**: 2 actions (do nothing, flap)
- **Neural Network**: 3-layer architecture (128 → 128 → 2 neurons)
- **Optimizer**: Adam optimizer with learning rate 0.0005
- **Loss Function**: Mean Squared Error (MSE)

### Advanced Techniques
- **Experience Replay Buffer**: Capacity of 10,000 transitions
- **Target Network Updates**: Every 100 training steps
- **Epsilon Decay**: Starts at 0.5, decays to 0.01 minimum
- **Reward System**: Distance-based penalties and collision punishments

## 🛠️ Technology Stack

- **Language**: Python 3.9+
- **Game Framework**: Pygame 2.1.2
- **Deep Learning**: PyTorch 1.13.1
- **Scientific Computing**: NumPy 1.23.5
- **Development Tools**: pip, virtualenv

## 📋 Prerequisites

- **Python**: Version 3.9 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended for smooth training)
- **GPU**: Optional (CUDA-compatible GPU for accelerated training)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd flappy-bird-with-deep-q
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Game
```bash
python main.py
```

## 🎮 How to Play

### Manual Mode (Default)
- **SPACEBAR**: Make the bird flap/jump
- **R**: Restart the game (when game over)
- **M**: Switch to AI mode

### AI Mode
- **M**: Switch back to manual mode
- Watch the AI agent learn and improve over time!

### Game Controls Summary
```
SPACEBAR  - Flap (Manual mode)
R         - Restart (Manual mode, when game over)
M         - Toggle between Manual/AI modes
ESC/Cross - Quit game
```

## 🏗️ Project Structure

```
flappy-bird-with-deep-q/
├── main.py                 # Main game loop and entry point
├── game.py                 # Flappy Bird game logic and physics
├── dqn.py                  # Deep Q-Network agent implementation
├── render.py               # Rendering and sound management
├── requirements.txt        # Python dependencies
├── flappybird.png          # Game thumbnail/demo image
├── readme.md              # Project documentation
├── __pycache__/           # Python bytecode cache
├── output.log             # Training logs
└── debug.log              # Debug information
```

## 🧮 Game Mechanics

### Physics Parameters
- **Gravity**: 0.6 pixels/frame²
- **Flap Velocity**: -10 pixels/frame (upward)
- **Pipe Speed**: 3 pixels/frame
- **Pipe Gap**: 150 pixels
- **Bird Size**: 30x30 pixels
- **Game Area**: 400x600 pixels

### State Representation
The AI agent receives a 4-dimensional state vector:
1. **Bird Y Position**: Normalized bird height (0-1)
2. **Bird Velocity**: Normalized vertical velocity (-1 to 1)
3. **Next Pipe Distance**: Distance to next pipe obstacle (0-1)
4. **Pipe Gap Position**: Vertical position of pipe gap (0-1)

### Reward System
- **Survival Reward**: +0.1 per frame
- **Distance Penalty**: -0.2 × normalized distance from gap center
- **Collision Penalty**: -1.0 for crashes

## 🧠 Training Process

### Learning Algorithm
1. **Initialization**: Random weights, high exploration (ε = 0.5)
2. **Experience Collection**: Store state transitions in replay buffer
3. **Mini-batch Training**: Sample experiences for Q-value updates
4. **Target Network Sync**: Periodic updates for training stability
5. **Exploration Decay**: Gradually reduce random actions over time

### Training Metrics
- **Episode Count**: Total games played
- **Failure Rate**: Collision frequency tracking
- **Performance**: Score improvement over time
- **Convergence**: Learning stabilization indicators

## 📊 Performance Analysis

### Expected Learning Progression
- **Early Training**: Random behavior, frequent collisions
- **Mid Training**: Basic pattern recognition, improved survival
- **Late Training**: Expert-level play, consistent high scores
- **Convergence**: Stable performance with minimal exploration

### Key Performance Indicators
- Average score per episode
- Survival time distribution
- Learning curve analysis
- Exploration vs exploitation balance

## 🔧 Configuration

### DQN Hyperparameters (dqn.py)
```python
MEMORY_SIZE = 10000      # Experience replay buffer size
GAMMA = 0.99            # Discount factor
EPSILON_START = 0.5     # Initial exploration rate
EPSILON_MIN = 0.01      # Minimum exploration rate
EPSILON_DECAY = 0.999   # Exploration decay rate
LEARNING_RATE = 0.0005  # Neural network learning rate
BATCH_SIZE = 64         # Training batch size
TARGET_UPDATE_FREQ = 100 # Target network update frequency
```

### Game Constants (game.py)
```python
WIDTH, HEIGHT = 400, 600    # Game window dimensions
PIPE_SPEED = 3              # Pipe movement speed
GRAVITY = 0.6               # Gravity acceleration
FLAP_VEL = -10              # Flap impulse velocity
PIPE_GAP = 150              # Gap between pipe sections
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is developed as part of an academic assignment. Please refer to your institution's guidelines for usage and distribution.

## 🎓 Learning Objectives

This project demonstrates several key concepts in reinforcement learning and game AI:

- **Deep Q-Learning**: Value-based reinforcement learning
- **Experience Replay**: Efficient sample utilization
- **Target Networks**: Training stability techniques
- **Exploration Strategies**: Epsilon-greedy policies
- **Game State Representation**: Feature engineering for RL
- **Reward Shaping**: Effective reward function design

## 📚 References

- [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) - Mnih et al.
- [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236) - Mnih et al.
- [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) - Hasselt et al.

---

**Built with ❤️ using PyTorch and Pygame for an intelligent take on a classic game**
