# PredatorPreyPy

A trivial ABM implementation of a Predator-Prey system in the Python programming language.

## Usage

To use this package follow this short example:

~~~python
import predatorpreypy as ppp
dims = (10,10)
n_predators, n_prey = 50 , 50
SIM_TIME = 10
env = ppp.Environment(dims, n_predators, n_prey)
for step in range(SIM_TIME):
    env.tick()
    
print(len(env.predators), len(env.prey))
~~~

## License

This project is subject to the MIT license, for further details refer to the ```LICENSE```.
