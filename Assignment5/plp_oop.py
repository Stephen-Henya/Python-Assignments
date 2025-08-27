# Smartphone class with inheritance

class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def info(self):
        print(
            f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB, Color: {self.color}")

# Inheritance: GamingSmartphone extends Smartphone


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, color, cooling_system, processor):
        super().__init__(brand, model, storage, color)
        self.cooling_system = cooling_system
        self.processor = processor

    def play_game(self, game):
        print(
            f"{self.brand} {self.model} is playing {game} with {self.processor} chipset and a {self.cooling_system} cooling system!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy A15", 256, "Black")
phone1.info()
phone1.call("0789654321")

gaming_phone = GamingSmartphone("Asus", "ROG Phone 9 Pro", 512, "Midnight Black", "liquid", "SnapDragon 8 Gen 3")
gaming_phone.info()
gaming_phone.play_game("OG Fortnite")
