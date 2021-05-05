import asyncio
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data 
from server import *
from dataclasses import dataclass

@dataclass()
class HyperParameters:
    self.lr = 0.001
    self.gamma = 0.99
    self.tau = 1.
    self.seed = 1

class GlobalHypervisor(object):

    grads = []

    def __init__(self, global_model: nn.Module, workers: int):
        self.workers = workers
        self.model = global_model
        self.init_state_dict = global_model.state_dict()
        
    def __init__(self, model: nn.Module, state_dict, workers: int):
        self.workers = workers
        self.model = model.load_state_dict(state_dict)
        self.init_state_dict = state_dict

    async def aggregate_gradients_handler(self, gradient: dict):
        #for fast api
        pass

    async def state_dict_distribution_handler(self):
        #for fast api
        pass

    def update_thread(self):
        pass

    def dump(self):
        pass

    def load(self):
        pass

    def flush_gradients(self):
        self.grads = []
    

    
