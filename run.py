import gym
import gym_examples

env = gym.make("gym_examples/GridWorld-v0", render_mode="human")

env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    _, _, done, _, _ = env.step(action)
    env.render()
