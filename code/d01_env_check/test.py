import torch
import gymnasium as gym

print(f"cuda is available: {torch.cuda.is_available()}")
env = gym.make("CartPole-v1")
obs, info = env.reset(seed=42)
print(f"obs: {obs} info: {info}")

action = env.action_space.sample()
obs, reward, terminated, truncated, info = env.step(action)
print("obs:", obs, "reward:", reward, "terminated:", terminated,"truncated:", truncated)
print("info:",info)
env.close()