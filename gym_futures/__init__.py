from gym.envs.registration import register

from envs.futures_env import FuturesEnv
from envs.utils import TimeSeriesState


register(
    id='futures-v0',
    entry_point='gym_futures.envs:FuturesEnv',
)
