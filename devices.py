import time

class Device:
    def __init__(self, name, power):
        self.name = name
        self.power = power  # in Watts
        self.is_on = False
        self.start_time = None
        self.total_energy = 0  # kWh

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.start_time = time.time()

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            duration = (time.time() - self.start_time) / 3600  # in hours
            self.total_energy += (self.power * duration) / 1000  # kWh

    def get_energy_cost(self, unit_price=50):
        """Return total energy cost in Rs."""
        return round(self.total_energy * unit_price, 2)

    def get_status(self):
        return {
            "name": self.name,
            "power": self.power,
            "is_on": self.is_on,
            "energy_used": round(self.total_energy, 3),
            "cost": self.get_energy_cost()
        }

# Create some devices
devices = {
    "light": Device("Light", 10),
    "fan": Device("Fan", 70),
    "ac": Device("AC", 1200)
}
