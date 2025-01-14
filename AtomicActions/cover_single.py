from pyrfuniverse.envs import ToborRobotiq85ManipulationEnv
import numpy as np
import pybullet as p
import math


if __name__ == '__main__':
    env = ToborRobotiq85ManipulationEnv(
        'cover_single',
        scene_file='CoverSingle.json',
        left_init_joint_positions=[-90, 45, 0, 75, 0, 60, 0],
        right_init_joint_positions=[-90, -45, 0, -75, 0, -60, 0]
    )
    env.reset()

    pi = math.pi

    env.step('right', np.array([0.299000114, 0.8, 0.826999784]))
    env.step('right', np.array([0.299000114, 0.730461419, 0.826999784]))
    env.close_gripper('right')
    env.step('right', np.array([0.15, 1.1, 0.95]))
    env.wait(150)

    env.step('right', np.array([0.299000114, 0.8, 0.826999784]))
    env.step('right', np.array([0.299000114, 0.730461419, 0.826999784]))

    env.open_gripper('right')

    while True:
        env._step()