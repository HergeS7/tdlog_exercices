



class Item:
    def __init__(self,prix, weight):
        self.price = prix     
        self.weight = weight  

    def display_item(self):
       
        print(f"Item: Price: {self.price}, Weight: {self.weight} kg")

item1 = Item( 45, 10)  
item1.display_item()                