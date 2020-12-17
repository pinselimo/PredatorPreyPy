import numpy as np

from .parameters import FOOD_MIN_INIT, FOOD_MAX_INIT

class Environment:
    def __init__(self, dims, n_predators, n_prey):
        x_max, y_max = dims
        self.X_MAX = x_max
        self.Y_MAX = y_max
        
        self.predators = [
            Predator(
                self,
                np.random.randint(0, x_max),
                np.random.randint(0, y_max),
                np.random.randint(FOOD_MIN_INIT, FOOD_MAX_INIT)
                ) 
            for _ in range(n_predators)
            ]  
        
        self.prey = [
            Prey(
                self,
                np.random.randint(0, x_max),
                np.random.randint(0, y_max),
                np.random.randint(FOOD_MIN_INIT, FOOD_MAX_INIT)
                ) 
            for _ in range(n_prey)
            ]
    
    def tick(self):
        # breed
        for p in self.prey + self.predators:
            p.breed()
            
        # move
        for p in self.prey + self.predators:
            dx = np.random.randint(0,3)-1
            dy = np.random.randint(0,3)-1
            
            p.move(dx, dy)
        
        # feed
        for p in self.prey:
            p.eat(np.random.randint(0,3))
            
        for p in self.predators:
            p.eat()
            
        # check alive
        for p in self.prey:
            if p.energy <= 0:
                self.prey.remove(p)
        
        for p in self.predators:
            if p.energy <= 0:
                self.predators.remove(p)
    