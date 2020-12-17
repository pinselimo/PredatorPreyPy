import numpy as np
np.random.seed(0)

from context import predatorpreypy as ppp

def test_agent_reproduction():
    env = ppp.Environment((10,10), 1, 100)
    for _ in range(10):
        env.tick()
    assert len(env.predators) <= 1