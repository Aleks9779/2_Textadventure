class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Item: {self.name}\nDescription: {self.description}")

class PizzaRecipe(Item):
    def __init__(self, name, ingredients):
        super().__init__(name, "This is a pizza recipe.")
        self.ingredients = ingredients

    def display_recipe(self):
        ingredient_list = ', '.join(self.ingredients)
        print(f"Recipe for {self.name}: {ingredient_list}")

    @staticmethod
    def check_pizza_recipe(attempted_recipe, correct_recipe):
        return attempted_recipe == correct_recipe

# Beispielhafte Verwendung
# margherita_recipe = PizzaRecipe("Margherita", ["tomato", "mozzarella", "basil", "dough"])
# margherita_recipe.display_recipe()
