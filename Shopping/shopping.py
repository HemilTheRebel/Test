from Shopping.items import Items
from dataclasses import dataclass
from typing import List

@dataclass 
class Basket(object):
    items : List[Items]
    def total(self):
        if len(self.items) > 0 :
            cost = 0
            for i in range(len(self.items)):
               cost += self.items[i].Price * self.items[i].Quantity
            return cost
        return 0 

