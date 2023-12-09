import numpy as np
import matplotlib.pyplot as plt
import gymnasium as gym

def episodic_semigradient_sarsa(env, policy, alpha, epsilon, num_episodes):
    # initialize value-function weights arbitrarily
    shape = (3, 3)  # TBD`
    weights = np.zeros(shape)

    # loop for each episode
    for episode in range(1, num_episodes + 1):
        # S, A <-- initial state and action of episode (e.g., epsilon-greedy)
        state = None  # d0 TBD
        action = None  # a0 TBD

        # loop for each step of episode
        terminal = False
        while not terminal:
            # take action A, observe R, S'
            next_state = None  # transition with p(s, a, s')
            reward = None  # get reward

            # if S' is terminal
            if next_state is None:  # tbd, probably a list of terminal states?
                # WEIGHT UPDATE STEP
                break  # go to next episode

            # choose a' as function of q(S', . , w) (e.g. epsilon greedy)
            next_action = None
            # WEIGHT UPDATE STEP

            state = next_state
            action = next_action

    return policy


def episodic_semigradient_nstep_sarsa(q_grid, policy, alpha, gamma, epsilon, n, num_episodes):
    # initialize value-function weights arbitrarily
    shape = (3, 3)  # TBD
    weights = np.zeros(shape)

    # all store and access operations (S, A, R) can take index mod n+1?

    # loop for each episode
    for episode in range(1, num_episodes + 1):
        # initialize and store non-terminal S0
        state = None  # d0 TBD
        # select and store action A0 ~ pi(·|S0), or epsilon greedy wrt q(S0, ·, w)
        action = None  # a0 TBD

        T_cap = np.inf
        # loop for t = 0, 1, 2...

        t = 0
        while True:
            if t < T_cap:
                # take action At, observe Rt+1, St+1
                next_state = None  # transition with p(s, a, s')
                reward = None  # get reward

                # if St+1 is terminal
                if next_state is None:  # tbd, probably a list of terminal states?
                    T_cap = t + 1
                else:
                    # select and store At+1 ~ pi(·|St+1) or epsilon greedy wrt q(St+1, ·, w)
                    next_action = None

            # tau is time whose estimate is being updated
            tau = t - n + 1
            if tau >= 0:
                G = None  # something, reward
                if tau + n < T_cap:
                    G = None  # some other update step
                # weight update step

            if tau == T_cap - 1:
                break

            # next timestep
            t += 1

    return policy


if __name__ == '__main__':

    # mountain car MDP
    # action space: Discrete(3) (left, no accel, right)
    # state space: Box([-1.2 -0.07], [0.6 0.07], (2,), float32)
    env = gym.make('MountainCar-v0', render_mode="human")
    observation, info = env.reset(seed=42)
    print(observation, info)  # s0

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()