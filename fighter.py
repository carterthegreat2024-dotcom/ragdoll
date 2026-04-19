class HumanoidFighter:
    def __init__(self, health=100):
        self.health = health
        self.is_knocked_down = False
        self.is_ragdoll = False

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.trigger_ragdoll()

    def trigger_ragdoll(self):
        self.is_ragdoll = True
        print('Ragdoll triggered!')

    def impact_collision(self):
        if not self.is_knocked_down:
            self.is_knocked_down = True
            print('Fighter knocked down!')

    def balance(self):
        if self.is_ragdoll:
            self.is_knocked_down = False
            self.is_ragdoll = False
            print('Self-balancing activated!')

    def status(self):
        return {"health": self.health, "knocked_down": self.is_knocked_down, "ragdoll": self.is_ragdoll}

# Example usage:
# fighter = HumanoidFighter()
# fighter.take_damage(20)
# fighter.impact_collision()
# fighter.balance()
# print(fighter.status())