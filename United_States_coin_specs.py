import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **key_word_arguments):

        # Loop through all of the keys and store them as well as the values
        for key, value in key_word_arguments.items():
            # Sets the keys and values, setting up all of the states
            setattr(self,key,value)
                  
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.orginal_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin has been Spent!!!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${}.00 Coin".format(int(self.original_value))
        else:
            return "0.{} cents Coin".format(int(self.original_value * 100))

class Penny(Coin):
    def __init__(self):
        data = {
            "name": "Penny",
            "original_value": 0.01, # Cents
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "number_of_edges": 1,
            "diameter": 21.21, # Millimeters
            "thickness": 1.95, # Millimeters
            "mass": 5 # Grams
            }      
        super().__init__(**data)

    def __str__(self):
        if self.original_value >= 1:
            return "${}.00 Coin".format(int(self.original_value))
        else:
            return "0.0{} cents Coin".format(int(self.original_value * 100))

class Nickle(Coin):
    def __init__(self):
        data = {
            "name": "Nickle",
            "original_value": 0.05, # Cents
            "clean_color": "silver",
            "rusty_color": "greenish",
            "number_of_edges": 1,
            "diameter": 24.26, # Millimeters
            "thickness": 2, # Millimeters
            "mass": 8.1 # Grams
            }      
        super().__init__(**data)

    def __str__(self):
        if self.original_value >= 1:
            return "${}.00 Coin".format(int(self.original_value))
        else:
            return "0.0{} cents Coin".format(int(self.original_value * 100)) 

class Dime(Coin):
    def __init__(self):
        data = {
            "name": "Dime",
            "original_value": 0.10, # Cents
            "clean_color": "silver",
            "rusty_color": "greenish",
            "number_of_edges": 1,
            "diameter": 17.91, # Millimeters
            "thickness": 1.35, # Millimeters
            "mass": 2.268 # Grams
            }      
        super().__init__(**data)

class Quarter(Coin):
    def __init__(self):
        data = {
            "name" : "Quarter",
            "original_value": 0.25, # Cents
            "clean_color": "silver",
            "rusty_color": "greenish",
            "number_of_edges": 1,
            "diameter": 24.26, # Millimeters
            "thickness": 3.15, # Millimeters
            "mass": 5.670 # Grams
            }      
        super().__init__(**data)

class Half_Dollar(Coin):
    def __init__(self):
        data = {
            "name": "Half Dollar",
            "original_value": 0.50, # Cents
            "clean_color": "silver",
            "rusty_color": "greenish",
            "number_of_edges": 1,
            "diameter": 30.61, # Millimeters
            "thickness": 2.15, # Millimeters
            "mass": 11.34 # Grams
            }      
        super().__init__(**data)


class Golden_Dollar(Coin):
    def __init__(self):
        data = {
            "name": "Golden Dollar",
            "original_value": 1.00, # Dollar Coin
            "clean_color": "gold",
            "rusty_color": None,
            "number_of_edges": 1,
            "diameter": 24.26, # Millimeters
            "thickness": 2, # Millimeters
            "mass": 8.1 # Grams
            }      
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color

coins = [Penny(), Nickle(), Dime(), Quarter(), Half_Dollar(), Golden_Dollar()]    
        
for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.number_of_edges, coin.mass]

    print()
    print("Specs for a", coin.name ,":")
    
    string = "{} - Color: {}, Value: {}, Diameter: {}(mm), Thickness: {}(mm), Number of Edges: {}, Mass: {}(g)".format(*arguments)
    print(string)
