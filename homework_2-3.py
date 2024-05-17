class Computer:
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def __make_computations(self, operator):
        if operator == '+':
            return self.__cpu + self.__memory
        elif operator == '-':
            return self.__cpu - self.__memory
        elif operator == '*':
            return self.__cpu * self.__memory
        elif operator == '/':
            if self.__memory != 0:
                return self.__cpu / self.__memory
            else:
                return "Division by zero"

    def info(self):
        return f"CPU: {self.__cpu}, Memory: {self.__memory}"


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().init(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        return f"CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Memory Card: {self.__memory_card}"

computer = Computer(3.2, 8)

print("Computer info:")
print(computer.info())
print("CPU:", computer.get_cpu())
print("Memory:", computer.get_memory())
print("Addition result:", computer._Computer__make_computations('+'))
print("Subtraction result:", computer._Computer__make_computations('-'))
print("Multiplication result:", computer._Computer__make_computations('*'))
print("Division result:", computer._Computer__make_computations('/'))

laptop = Laptop(2.5, 16, "512GB SSD")

print("\nLaptop info:")
print(laptop.info())
print("CPU:", laptop.get_cpu())
print("Memory:", laptop.get_memory())
print("Memory Card:", laptop.get_memory_card())
print("Addition result:", laptop._Computer__make_computations('+'))
print("Subtraction result:", laptop._Computer__make_computations('-'))
print("Multiplication result:", laptop._Computer__make_computations('*'))
print("Division result:", laptop._Computer__make_computations('/'))