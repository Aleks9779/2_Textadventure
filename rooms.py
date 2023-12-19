from characters import Character
import random
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._puzzle_solved = False  # Privates Attribut

    def enter_room(self, player):
        print(self.description)

    def complete_puzzle(self):
        self._puzzle_solved = True

# 1
class IntroRoom(Room):
    def __init__(self):
        description = "You are an aspiring ovenist in a small pizzeria, dreaming of becoming a master ovenist."
        super().__init__("Intro Room", description)

    def enter_room(self, player):
        super().enter_room(player)
        
        # Einführung in die Geschichte
        print("Welcome to the Pizza Text Adventure!")
        print(self.description)

        # Spieler wählt einen Namen für den Charakter
        player_name = input("Choose a name for your character: ")
        player.name = player_name
        print(f"Welcome, {player.name}! Your journey to become a master ovenist begins now.")

        # Information über das Spielziel
        print("Your goal is to master the art of pizza making and run your own pizzeria.")

        # Entscheidung, das Spiel zu verlassen oder fortzusetzen
        choice = input("Do you want to proceed to the next room? (yes/no): ")
        if choice.lower() == 'no':
            print("Exiting the game. Goodbye!")
            return False  # Beendet den Raum und das Spiel
        else:
            print("Moving to the next room...")
            return True  # Geht zum nächsten Raum
# 2
class PizzaKnowledgeRoom(Room):
    def __init__(self):
        description = "Learn about the history of pizza and the basic ingredients of a Margherita."
        super().__init__("Pizza Knowledge Room", description)

    def enter_room(self, player):
        super().enter_room(player)

        # Einführung in die Geschichte der Pizza
        print("The history of pizza began in Italy. The Margherita pizza was created in honor of Queen Margherita.")

        # Grundzutaten einer Margherita-Pizza
        print("The basic ingredients of a Margherita pizza are tomato, mozzarella, basil, and dough.")
        player.add_to_inventory("Margherita Ingredients", ["tomato", "mozzarella", "basil", "dough"])

        # Quiz
        print("Let's test your knowledge!")
        correct_answer = "tomato, mozzarella, basil, dough"
        answer = input("What are the ingredients of a Margherita pizza? ")

        # Überprüfen der Antwort
        if answer.lower() == correct_answer:
            print("Correct! You have passed the knowledge test.")
            return True  # Spieler geht zum nächsten Raum
        else:
            print("Incorrect. Game over.")
            return False  # Spielende
# 3
class TutorialPhase(Room):
    def __init__(self):
        description = "Learn the basics of operating an oven, including setting temperature and timing."
        super().__init__("Tutorial Phase", description)

    def enter_room(self, player):
        super().enter_room(player)

        # Einführung in die Bedienung eines Ofens
        print("Welcome to the Oven Tutorial!")
        print("In this tutorial, you will learn how to set the temperature and timing for baking pizzas.")

        # Interaktive Tutorial-Elemente
        temperature = input("Set the oven temperature (e.g., 200°C): ")
        time = input("Set the baking time (e.g., 20 minutes): ")

        # Überprüfen der Eingaben (einfache Validierung)
        if temperature.isdigit() and time.isdigit():
            print("Well done! You've successfully set the oven.")
            player.add_to_inventory("Oven Skills", {"temperature": temperature, "time": time})
            return True  # Spieler geht zum nächsten Raum
        else:
            print("Incorrect input. Let's try again.")
            return False  # Spieler bleibt im Tutorial
# 4
class FirstOrder(Room, Character):
    def __init__(self):
        description = "Receive and complete your first pizza order."
        super().__init__("First Order", description)

    def enter_room(self, player):
        super().enter_room(player)
        print("Your first order is a Margherita pizza.")

        attempts = 0
        correct_temperature = "200°C"
        correct_time = "20 minutes"
        correct_toppings = "tomato, mozzarella, basil"

        while attempts < Character.MAX_ATTEMPTS:
            temperature = input("Set the oven temperature (e.g., 200°C): ")
            time = input("Set the baking time (e.g., 20 minutes): ")
            toppings = input("Choose the toppings (e.g., tomato, mozzarella, basil): ")

            if temperature == correct_temperature and time == correct_time and toppings == correct_toppings:
                print("Perfect! The customer loved the pizza.")
                return True  # Spieler geht zum nächsten Raum
            else:
                attempts += 1
                print(f"Incorrect. You have {Character.MAX_ATTEMPTS - attempts} attempts left.")

        print("You failed to make the pizza correctly. Game over.")
        return False  # Spielende

# 5
class BossRecipe(Room):
    def __init__(self):
        description = "Your boss reveals a secret pizza recipe."
        super().__init__("Boss's Secret Recipe", description)
        self.secret_recipe = ["special sauce", "unique cheese blend", "exotic toppings"]

    def enter_room(self, player):
        super().enter_room(player)

        print(f"Your boss has decided to share the secret recipe of the Boss's Special with you.")
        player.add_to_inventory("Boss's Special", self.secret_recipe)
        print("The recipe for Boss's Special has been added to your inventory.")

        print("Now, it's time to prepare the Boss's Special for a customer.")
        return self.prepare_pizza_minigame(player)

    def prepare_pizza_minigame(self, player):
        print("To prepare the Boss's Special, add the ingredients in the correct order.")
        
        for ingredient in self.secret_recipe:
            player_input = input(f"Add the next ingredient ({'/'.join(self.secret_recipe)}): ")
            if player_input.lower() != ingredient:
                print("Oops, that's not the right ingredient. Let's start over.")
                return False  # Der Spieler hat das Minispiel nicht bestanden

        print("You successfully prepare the Boss's Special. The customer is delighted!")
        return True  # Der Spieler hat das Minispiel bestanden


# 6
class RunOutOfTomatoSauce(Room):
    def __init__(self):
        description = "You run out of tomato sauce and need to buy ingredients at the store."
        super().__init__("Run Out of Tomato Sauce", description)
        self.required_ingredients = ["tomato sauce", "olive oil", "garlic", "basil"]
        self.secret_recipe = "Store Run Pizza"

    def enter_room(self, player):
        super().enter_room(player)

        # Chef gibt die benötigten Zutaten
        print("Your boss gives you a list of ingredients to buy: " + ", ".join(self.required_ingredients))
        print("Remember the list or write it down.")

        # Spieler geht zum Laden
        print("You're at the store. Time to find the right ingredients.")
        purchased_ingredients = []
        for ingredient in self.required_ingredients:
            player_choice = input(f"Did you find {ingredient}? (yes/no): ")
            if player_choice.lower() == "yes":
                purchased_ingredients.append(ingredient)

        # Überprüfen, ob alle Zutaten gekauft wurden
        if set(purchased_ingredients) == set(self.required_ingredients):
            print("You've successfully bought all the ingredients.")
            player.add_to_inventory(self.secret_recipe, ["special dough", "unique sauce", "exotic cheese"])
            print(f"You've unlocked the secret recipe: {self.secret_recipe}.")
            return True  # Spieler geht zum nächsten Raum
        else:
            print("You missed some ingredients. Let's try again.")
            return False  # Spieler bleibt im Raum    

# 7
class VisitItaly(Room):
    def __init__(self):
        description = "Travel to Italy to learn more about the art of pizza making."
        super().__init__("Visit Italy", description)
        self.italian_classics_recipe = "Italian Classics"

    def enter_room(self, player):
        super().enter_room(player)

        # Beschreibung des Besuchs in Italien
        print("Your boss sends you on a journey to Italy, the birthplace of pizza.")
        print("Here, you learn about different regional styles and the history of pizza.")

        # Hinzufügen von interessanten Fakten und Informationen
        print("Did you know that the Margherita pizza was named after Queen Margherita of Savoy?")
        print("It's said to represent the colors of the Italian flag: red (tomato), white (mozzarella), and green (basil).")

        # Erweiterung des Wissens über Pizza
        player.add_to_inventory("Pizza History Knowledge", ["Margherita origin", "regional styles"])

        # Hinzufügen eines neuen Rezepts zum Inventar
        player.add_to_inventory(self.italian_classics_recipe, ["authentic ingredients", "traditional methods"])
        print(f"You've added the {self.italian_classics_recipe} recipe to your inventory.")

        return True  # Spieler geht zum nächsten Raum

# 8    
import random

class TheGreatPizzaBakeOff(Room):
    def __init__(self):
        description = "Compete in a grand pizza bake-off against rival chefs."
        super().__init__("The Great Pizza Bake-Off", description)
        self.pizza_orders = {
            "Margherita": {"temperature": "220°C", "time": "15 minutes"},
            "Pepperoni": {"temperature": "200°C", "time": "20 minutes"},
            "Hawaiian": {"temperature": "180°C", "time": "25 minutes"},
            "Veggie": {"temperature": "200°C", "time": "18 minutes"},
            "Four Cheese": {"temperature": "210°C", "time": "22 minutes"}
        }

    def enter_room(self, player):
        super().enter_room(player)
        print("Welcome to the Great Pizza Bake-Off! Show your skills against top chefs.")
        random_orders = random.sample(list(self.pizza_orders.keys()), 3)
        
        for order in random_orders:
            if not self.bake_pizza(player, order):
                print("You failed to impress the judges with your pizza. Better luck next time!")
                return False  # Der Spieler hat den Wettbewerb nicht gewonnen

        print("Congratulations! You've won the Great Pizza Bake-Off!")
        return True  # Der Spieler hat den Wettbewerb gewonnen

    def bake_pizza(self, player, order):
        correct_settings = self.pizza_orders[order]
        print(f"Your next order is: {order}.")
        temperature = input("Set the oven temperature (e.g., 220°C): ")
        time = input("Set the baking time (e.g., 20 minutes): ")

        if temperature == correct_settings["temperature"] and time == correct_settings["time"]:
            print(f"Perfect! You've successfully baked a {order} pizza.")
            return True
        else:
            print(f"Oops, that's not right for a {order} pizza.")
            return False
