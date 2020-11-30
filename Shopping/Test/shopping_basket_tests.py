from Shopping.shopping import Basket, Items
from typing import List
import unittest
from dataclasses import dataclass


    

class ShoppingBasketTest(unittest.TestCase):
    def testEmptyBasket(self):
        basket = Basket([])
        self.assertEqual(basket.total(),0)
    
    def testSingleItemQuantityOne(self):
        basket = Basket([Items(100.00,1)])
        self.assertEqual(basket.total(),100.00)
    
    def testSingleItemQuantityMany(self):
        basket = Basket([Items(200.00,5)])
        self.assertEqual(basket.total(),1000.00)

    def testMultipleItemQuantityMultiple(self):
        basket = Basket([Items(200.00,5),Items(300.00,1),Items(100.00,10)])
        self.assertEqual(basket.total(),2300.00)


if __name__ == "__main__":
    pass