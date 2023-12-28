class Computer:
    def __init__(self, cpu, memory):
        self._cpu = cpu
        self._memory = memory

    @property
    def cpu(self):
        return self._cpu

    @property
    def memory(self):
        return self._memory

    @cpu.setter
    def cpu(self, value):
        self._cpu = value

    @memory.setter
    def memory(self, value):
        self._memory = value

    def make_computations(self):
        result = self._cpu + self._memory
        return f"Arithmetic computations result: {result}"

    def __str__(self):
        return f"Computer: CPU={self._cpu}, Memory={self._memory}"


class Phone:
    def __init__(self):
        self._sim_cards_list = []

    @property
    def sim_cards_list(self):
        return self._sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self._sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self._sim_cards_list):
            sim_card = self._sim_cards_list[sim_card_number - 1]
            return f"Calling {call_to_number} from sim card {sim_card}."

    def __str__(self):
        return f"Phone: Sim Cards List={self._sim_cards_list}"


class SmartPhone(Computer, Phone):
    def use_gps(self, location):
        return f"Using GPS to navigate to {location}."

    def __str__(self):
        return f"SmartPhone: CPU={self.cpu}, Memory={self.memory}, Sim Cards List={self.sim_cards_list}"



computer_obj = Computer(cpu="Intel", memory=8)
phone_obj = Phone()
phone_obj.sim_cards_list = ["Beeline", "Megafon", "MTS"]
smartphone1_obj = SmartPhone(cpu="Snapdragon", memory=12)
smartphone1_obj.sim_cards_list = ["Vodafone", "AT&T"]
smartphone2_obj = SmartPhone(cpu="Apple A14", memory=16)
smartphone2_obj.sim_cards_list = ["Verizon", "T-Mobile"]


print(computer_obj)
print(phone_obj)
print(smartphone1_obj)
print(smartphone2_obj)


print(computer_obj.make_computations())
print(phone_obj.call(1, "+996 777 99 88 11"))
print(smartphone1_obj.use_gps("Home"))
print(smartphone2_obj.use_gps("Office"))


class Computer:
    def __init__(self, cpu, memory):
        self._cpu = cpu
        self._memory = memory

    def __eq__(self, other):
        return self._memory == other._memory

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._memory < other._memory

    def __le__(self, other):
        return self._memory <= other._memory

    def __gt__(self, other):
        return self._memory > other._memory

    def __ge__(self, other):
        return self._memory >= other._memory

    def __str__(self):
        return f"Computer: CPU={self._cpu}, Memory={self._memory}"

computer1 = Computer(cpu="Intel", memory=8)
computer2 = Computer(cpu="AMD", memory=16)

print(computer1 == computer2)
print(computer1 != computer2)
print(computer1 < computer2)
print(computer1 <= computer2)
print(computer1 > computer2)
print(computer1 >= computer2)
