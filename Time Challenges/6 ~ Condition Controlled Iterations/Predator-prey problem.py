class PredatorPrey:
    def __init__(self, *args, data={"Prey": 30, "Predators": 5, "A": 0.8, "B": 0.5, "C": 0.1, "D": 0.3, "E": 2.718, "max_iters": 100}):
        for key,value in data.items():
            setattr(self, key, value)
        self.generation = 0
    def tick(self):
        prey_growth_rate = self.E ** (self.A - (self.C * self.Predators))
        self.Prey *= prey_growth_rate
        predator_growth_rate = self.E ** ((self.D * self.C * self.Prey) - self.B)
        self.Predators *= predator_growth_rate
        self.Prey = round(self.Prey)
        self.Predators = round(self.Predators)
        self.generation += 1
    def __str__(self):
        return f"Generation: {self.generation} | Prey: {self.Prey} | Predators: {self.Predators}"
    def run(self):
        while self.Prey > 2 and self.Predators > 2 and (self.max_iters == -1 or self.generation <= self.max_iters):
            print(self)
            self.tick()
    
Environment = PredatorPrey()
Environment.run()