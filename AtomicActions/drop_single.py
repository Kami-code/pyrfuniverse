from pyrfuniverse.envs import ToborRobotiq85ManipulationEnv
import numpy as np
import pybullet as p
import math

if __name__ == '__main__':
    env = ToborRobotiq85ManipulationEnv(
        'tamp',
        scene_file='DropSingle.json',
        left_init_joint_positions=[-90, 45, 0, 75, 0, 60, 0],
        right_init_joint_positions=[-90, -45, 0, -75, 0, -60, 0]
    )
    env.reset()

    pi = math.pi

    env.step('right', np.array([0.3, 0.85, 0.933]))
    env.step('right', np.array([0.3, 0.77, 0.933]))
    env.close_gripper('right')

    env.step('right', np.array([1, 0.85, 0.662]), orientation=p.getQuaternionFromEuler([pi / 2, pi / 2, 0]))
    env.open_gripper('right')

    # env.close()

    while True:
        env._step()