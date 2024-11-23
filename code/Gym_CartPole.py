import gym
# import time

env = gym.make('CartPole-v1', render_mode="human")
state = env.reset()

print(env.action_space)

for _ in range(1000):
    env.render() # 进行渲染，会弹出一个窗口显示CartPole一游戏

    action = env.action_space.sample() # 随机均匀抽样一个动作，实际不会用这行代码

    observation, reward, terminated, truncated, info = env.step(action)
    print(observation, reward, terminated, truncated)

    if terminated or truncated:
        break

    # time.sleep(1)

env.close()


# import gym
# env = gym.make('CartPole-v1', render_mode = "human")
# for episode in range(10):
#   env.reset()
#   print("Episode finished after {} timesteps".format(episode))
#   for _ in range(100):
#     env.render()
#     env.step(env.action_space.sample())
# env.close()


