import numpy as np

from .parameters import METABOLISM

class Agent:
    def __init__(self, env, x, y, energy):
        self._env = env
        self._x = x
        self._y = y
        self._energy = energy
        
    def move(self, dx, dy):
        if self.energy <= 0:
            return
        
        self._x += dx
        self._y += dy
        
        if self._x >= self._env.X_MAX:
            self._x = 0
        elif self._x < 0:
            self._x = self._env.X_MAX-1
            
        if self._y >= self._env.Y_MAX:
            self._y = 0
        elif self._y < 0:
            self._y = self._env.Y_MAX-1
        
        self._energy -= METABOLISM
        
    def find_agent(self, agents):
        for a in agents:
            if self.x == a.x and self.y == a.y and self != a:
                return a
        return None
    
    def _breed(self, other, agents, cls):
        if not other is None:
            energy_breed = np.round((self.energy + other.energy) / 2)
            offspring = cls(self._env, self.x, self.y, energy_breed)
            agents.append(offspring)
          
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def energy(self):
        return self._energy
    
class Prey(Agent):
    def eat(self, amount):
        self._energy += amount
        
    def get_eaten(self):
        self._energy = 0
        
    def breed(self):
        p = self.find_agent(self._env.prey)
        self._breed(p, self._env.prey, Prey)
        
class Predator(Agent):
    def eat(self):
        p = self.find_agent(self._env.prey)
        if not p is None:
            self._energy += p.energy
            p.get_eaten()
        
    def breed(self):
        p = self.find_agent(self._env.predators)
        self._breed(p, self._env.predators, Predator)