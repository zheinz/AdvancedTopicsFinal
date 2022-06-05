#Import required libraries
from ray import tune
from ray.tune.registry import register_env
from ray.rllib.env import PettingZooEnv
from pettingzoo.butterfly import pistonball_v6
import supersuit as ss

#Define function to create the pistonball environemnt and apply necessary wrappers
def env_creator():
    env = pistonball_v6.env(n_pistons=20, time_penalty=-0.1, continuous=False, random_drop=False, random_rotate=False, ball_mass=0.75, ball_friction=0.3, ball_elasticity=1.5, max_cycles=125)
    env = ss.resize_v0(env, x_size=84, y_size=84, linear_interp=True)
    env = ss.color_reduction_v0(env, mode='full')
    env = ss.dtype_v0(env, 'float32')
    env = ss.normalize_obs_v0(env, env_min=0, env_max=1)
    env = ss.resize_v0(env, x_size=32, y_size=32, linear_interp=True)
    env = ss.flatten_v0(env)
    return env

#register the environment 
register_env("pistonball", lambda config: PettingZooEnv(env_creator()))
test_env = PettingZooEnv(env_creator())
obs_space = test_env.observation_space
act_space = test_env.action_space

#Train the model with the following hyperparameters and using a single policy for all the agents
tune.run(
    "APEX",
    name="NameOfModel",
    stop={"timesteps_total": 15000000},
    checkpoint_freq=10,
    local_dir="~/ray_results/",
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
)


