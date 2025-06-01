import torch
import torch.nn as nn
import torch.optim as optim
import random
import collections
import copy
import numpy as np

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )

    def forward(self, x):
        return self.net(x)

class DQNAgent:
    def __init__(self, state_dim, action_dim):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.memory = collections.deque(maxlen=10000)
        self.gamma = 0.99
        self.epsilon = 0.5
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.999
        self.learning_rate = 0.0005
        self.batch_size = 64
        self.model = DQN(state_dim, action_dim)
        self.target_model = copy.deepcopy(self.model)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()
        self.target_update_freq = 100
        self.frame_count = 0

    def store_experience(self, state, action, reward, next_state, done):
        state = np.copy(np.ascontiguousarray(state, dtype=np.float32))
        next_state = np.copy(np.ascontiguousarray(next_state, dtype=np.float32))
        self.memory.append((state, action, reward, next_state, done))

    def train(self, state, action, reward, next_state, done):
        self.frame_count += 1
        self.store_experience(state, action, reward, next_state, done)
        if len(self.memory) < self.batch_size:
            return

        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        states = np.ascontiguousarray(states, dtype=np.float32)
        next_states = np.ascontiguousarray(next_states, dtype=np.float32)
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        q_values = self.model(states).gather(1, actions.unsqueeze(1)).squeeze(1)
        with torch.no_grad():
            next_q_values = self.target_model(next_states).max(1)[0]
        targets = rewards + (1 - dones) * self.gamma * next_q_values
        loss = self.criterion(q_values, targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        if self.frame_count % self.target_update_freq == 0:
            self.target_model.load_state_dict(self.model.state_dict())
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randrange(self.action_dim)
        state = np.copy(np.ascontiguousarray(state, dtype=np.float32))
        state = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            q_values = self.model(state)
        return q_values.argmax().item()