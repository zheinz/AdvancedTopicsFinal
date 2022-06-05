#import the required libraries
from ray import tune
from ray.tune.registry import register_env
from ray.rllib.env import PettingZooEnv
from pettingzoo.butterfly import pistonball_v6
from pettingzoo.utils import save_observation
from ray.rllib.agents.dqn.apex import ApexTrainer
import supersuit as ss
import numpy as np
import random
import time

np.set_printoptions(threshold=np.inf)

#Define function to permutate the agents observations
def permutate(array):
    permutation = np.random.permutation(array)
    return permutation

#Define function to add noise to the agents observations
def addNoise(array):
    noise = np.full(1024, 0.5)
    return array + noise

#Define function to create the Pistonball Environment
def env_creator():
    env = pistonball_v6.env(n_pistons=20, time_penalty=-0.1, continuous=False, random_drop=False, random_rotate=False, ball_mass=0.75, ball_friction=0.3, ball_elasticity=1.5, max_cycles=125)
    env = ss.resize_v0(env, x_size=84, y_size=84, linear_interp=True)
    env = ss.color_reduction_v0(env, mode='full')
    env = ss.dtype_v0(env, 'float32')
    env = ss.normalize_obs_v0(env, env_min=0, env_max=1)
    env = ss.resize_v0(env, x_size=32, y_size=32, linear_interp=True)
    env = ss.flatten_v0(env)
    return env

#Register the environemnt with the same action space and observation space as used in the models training
register_env("pistonball", lambda config: PettingZooEnv(env_creator()))
test_env = PettingZooEnv(env_creator())
obs_space = test_env.observation_space
act_space = test_env.action_space
config= {
            "env": "pistonball",
            "log_level": "ERROR",
            "framework": "torch",

            "num_gpus":0,

            "buffer_size": 400000,
            "adam_epsilon": 0.00015,
            "double_q": True,
            "dueling": True,
            "final_prioritized_replay_beta": 1.0,
            "gamma": 0.99,
            "learning_starts": 10000,
            "lr": 0.0001,
            "n_step": 3,
            "num_atoms": 1,
            "num_envs_per_worker": 1,
            "num_workers": 3,
            "prioritized_replay": True,
            "prioritized_replay_alpha": 0.5,
            "rollout_fragment_length": 32,
            "target_network_update_freq": 10000,
            "timesteps_per_iteration": 15000,
            "train_batch_size": 512,

            "multiagent": {
                "policies": {
                    "single_policy": (None, obs_space, act_space, {}),
                },
                "policy_mapping_fn": (lambda agent_id: "single_policy")
            }            
        }    

#Restore the model from the saved checkpoints
APEXagent = ApexTrainer(env="pistonball", config=config)
APEXagent.restore("/home/zade/ray_results/SinglePolicy/APEX_pistonball_d16cf_00000_0_2022-05-19_21-12-53/checkpoint_000300/checkpoint-300") #MODEL 1 -- uncomment to use model 1
#APEXagent.restore("/home/zade/ray_results/SinglePolicy2/APEX_pistonball_2b49e_00000_0_2022-05-23_12-35-15/checkpoint_000300/checkpoint-300") #MODEL 2 -- uncomment to use model 2
#APEXagent.restore("/home/zade/ray_results/SinglePolicy3/APEX_pistonball_aa83f_00000_0_2022-05-23_16-27-53/checkpoint_000300/checkpoint-300") #MODEL 3 -- uncomment to use model 3

#Initalise reward and cycle counter variables to be used as performance metrics
cycleCounter = 0
rewardTotal = 0

#Create the environment and play a single game using the trained model, apply attacks during the game by uncommenting some of the lines below. 
env = env_creator()
env.reset()
for agent in env.agent_iter():
    cycleCounter+=1
    observation, reward, done, info = env.last()
    #choice = random.choices(["attack", "nothing"], [0.9, 0.1]) #Make choice to attak --uncomment for permutation attack
    #if choice[0] == "attack": observation = permutate(observation) #Apply the permutation attack -- uncomment for permutation attack
    #observation = addNoise(observation) #Apply noise to oberservation -- uncomment for noise attack
    rewardTotal += reward
    if done:
        action = None
    else:
        action = APEXagent.compute_single_action(policy_id="single_policy", observation=observation)
    env.step(action)
    #env.render(mode='human') # Uncomment to watch the model perform in game

#Print the performance metrics to be used for results and analysis.
print(rewardTotal)
print(cycleCounter)

