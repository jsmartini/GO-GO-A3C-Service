from abc import ABC, abstractmethod
from torch.utils.data import Dataset, DataLoader
from collections import deque, namedtuple
from random import sample


memory = namedtuple(
    "MEMORY",
    (
        "CState", "Action", "NState", "Reward", "Terminal"
    )
)


class ReplayBuffer(ABC):

    def __init__(self, max_sz):
        self.MEM = deque(max_sz)
    
    def __len__(self):
        return len(self.MEM)

    def __add__(self, new: memory):
        self.MEM.append(new)
    
    @abstractmethod()
    def replay(self, **kwargs) -> Dataset:
        pass
        
    def _sample(self, batch_size = 32):
        return sample(self.MEM, min(batch_size, len(self)))


        