class Character:
    MAX_ATTEMPTS = 3  # Statisches Attribut für maximale Versuche

    def __init__(self, name):
        self.name = name
        self._skill_level = 0  # Privates Attribut für Fähigkeitslevel
        self.inventory = {}    # Inventar für Gegenstände und Rezepte

    def _update_skill_level(self, level):  # Private Methode zur Aktualisierung des Fähigkeitslevels
        self._skill_level += level

    def get_skill_level(self):  # Getter-Methode für das Fähigkeitslevel
        return self._skill_level

    def set_skill_level(self, level):  # Setter-Methode für das Fähigkeitslevel
        self._skill_level = level

    @staticmethod
    def check_pizza_recipe(recipe, attempted_recipe):  # Statische Methode zur Überprüfung eines Rezepts
        return recipe == attempted_recipe

    def complete_challenge(self, challenge):  # Dynamische Methode zur Bewältigung von Herausforderungen
        # Logik zur Bewältigung von Herausforderungen basierend auf dem Charakter und dem Fähigkeitslevel
        success = challenge.attempt_challenge(self)
        if success:
            self._update_skill_level(1)  # Erhöhe Fähigkeitslevel bei Erfolg
        return success

    def add_to_inventory(self, item_name, item):  # Methode zum Hinzufügen eines Gegenstands zum Inventar
        self.inventory[item_name] = item

    def remove_from_inventory(self, item_name):  # Methode zum Entfernen eines Gegenstands aus dem Inventar
        if item_name in self.inventory:
            del self.inventory[item_name]

    def get_inventory_item(self, item_name):  # Methode zum Abrufen eines Gegenstands aus dem Inventar
        return self.inventory.get(item_name)


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        self.items[item_name] = item

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item(self, item_name):
        return self.items.get(item_name)

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = Inventory()

    def add_to_inventory(self, item_name, item):
        self.inventory.add_item(item_name, item)

    def remove_from_inventory(self, item_name):
        self.inventory.remove_item(item_name)

    def check_inventory_item(self, item_name):
        return self.inventory.get_item(item_name)

    def complete_challenge(self, challenge):
        # Angepasste Logik für den Spieler
        success = super().complete_challenge(challenge)
        # Hier können zusätzliche spieler-spezifische Logiken hinzugefügt werden
        return success
