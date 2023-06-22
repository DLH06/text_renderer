import random
from typing import List


class myaNameGenerator:
    def __init__(self) -> None:
        with open("text/mya_name_part.txt", "r") as f:
            self.data = f.readlines()
            self.data = [each.replace("\n", "") for each in self.data]

    def __generate_name(self) -> str:
        name_2 = random.choice(self.data) + " " + random.choice(self.data)
        name_add = random.choice(self.data)

        return random.choice([name_2, name_2 + " " + name_add])

    def generate_names(self, num_names: int) -> List[str]:
        return [self.__generate_name() for _ in range(num_names)]


if __name__ == "__main__":
    name_generator = myaNameGenerator()
    names = name_generator.generate_names(10)
    with open("text/mya_name.txt", "w") as f:
        for name in names:
            f.writelines(name+"\n")