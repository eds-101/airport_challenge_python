class Airport:

    def __init__(self, arg_capacity = 5):
        self.hangar = []
        self.capacity = arg_capacity

    def land(self, plane):
        self.at_capacity()
        self.check_weather(self.set_weather(), "land")
        self.hangar.append(plane)

    def view_hangar(self):
        return self.hangar

    def take_off(self, plane):
        self.hangar.remove(plane)
        self.check_weather(self.set_weather(), "take_off")
        self.view_hangar()

    def at_capacity(self):
        if len(self.hangar) >= self.capacity:
            raise Exception("Airport is full") 
        else:
            return

    def set_weather(self):
        import random
        num = random.randint(0, 100)
        return "stormy" if num > 90 else "sunny"

    def check_weather(self, weather, mode):
        if weather == "stormy":
            if mode == "land":
                raise Exception("Can't land, bad weather!")
            elif mode == "take_off":
                raise Exception("Can't take off, bad weather!")

