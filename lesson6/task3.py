class Worker:
    name = ''
    surname = ''
    position = ''

    _income = {"wage": 0, "bonus": 0}

    def set_wage(self, wage):
        self._income["wage"] = wage

    def set_bonus(self, bonus):
        self._income["bonus"] = bonus

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self, hours):
        return self._income["wage"] * hours + self._income["bonus"]

p = Position()
p.name = 'Denys'
p.surname = 'Golotiuk'
p.position = 'junior professor'

p.set_wage(100);
p.set_bonus(1000);

print(p.get_full_name(), 'total income is', p.get_total_income(40))
