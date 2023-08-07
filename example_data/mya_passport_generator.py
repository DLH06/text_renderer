import random
import string
import os
from tqdm import tqdm


class passportGenerator:
    def __init__(self) -> None:
        self.sex = ["N", "M"]
        with open("text/db/mya_township.txt", "r") as f:
            self.township = f.readlines()
            self.township = [
                each.replace("\n", "").replace("-", "").replace(" ", "").upper()
                for each in self.township
            ]

    def nrc_generate(self) -> str:
        region_code = random.randint(1, 14)
        township = random.choice(self.township)
        sex = random.choice(self.sex)
        serial_number = "".join([str(random.randint(0, 9)) for _ in range(6)])
        return "{}/{}({}){}".format(region_code, township, sex, serial_number)

    def no_generate(self) -> str:
        return (
            random.choice(string.ascii_uppercase[:26])
            + random.choice(string.ascii_uppercase[:26])
            + "".join([str(random.randint(0, 9)) for _ in range(6)])
        )

    def type_generate(self) -> str:
        return random.choice(string.ascii_uppercase[:26]) + random.choice(
            string.ascii_uppercase[:26]
        )


if __name__ == "__main__":
    os.makedirs("text/gen_base/", exist_ok=True)
    pp_generator = passportGenerator()

    NUM_NRC = 15000
    NUM_NO = 15000
    NUM_TYPE = 10000

    with open("text/gen_base/en_passport.txt", "w") as f:
        for _ in tqdm(range(NUM_NRC), desc="en nrc generate"):
            f.writelines(pp_generator.nrc_generate() + "\n")
        for _ in tqdm(range(NUM_NO), desc="en num id generate"):
            f.writelines(pp_generator.no_generate() + "\n")
        for _ in tqdm(range(NUM_TYPE), desc="type generate"):
            f.writelines(pp_generator.type_generate() + "\n")
