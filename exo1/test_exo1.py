



class Item:
    def __init__(self,price, weight):
        self.price = price      
        self.weight = weight  

    def display_item(self):
       
        print(f"Item: Price: {self.price}, Weight: {self.weight} kg")

item1 = Item( 0.5, 10)  
item1.display_item()                