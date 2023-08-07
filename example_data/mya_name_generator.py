import random
from typing import List
import os
from tqdm import tqdm


class myaNameGenerator:
    def __init__(self) -> None:
        with open("text/db/mya_name_part.txt", "r") as f:
            self.data = f.readlines()
            self.data = [each.replace("\n", "") for each in self.data]

    def __generate_name(self) -> str:
        name_2 = random.choice(self.data) + " " + random.choice(self.data)
        name_add = random.choice(self.data)

        return random.choice([name_2, name_2 + " " + name_add])

    def generate_names(self, num_names: int) -> List[str]:
        return [self.__generate_name() for _ in range(num_names)]


if __name__ == "__main__":
    os.makedirs("text/gen_base/", exist_ok=True)
    name_generator = myaNameGenerator()

    NUM_NAME = 15000

    names = name_generator.generate_names(NUM_NAME)
    with open("text/gen_base/en_name.txt", "w") as f:
        for name in tqdm(names, desc="write name"):
            f.writelines(name+"\n")