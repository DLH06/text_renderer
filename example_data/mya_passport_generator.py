import random
import string


class passportGenerator:
    def __init__(self) -> None:
        self.sex = ["N", "M"]
        with open("text/mya_township.txt", "r") as f:
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
    pp_generator = passportGenerator()

    NUM_NRC = 1000
    NUM_NO = 1000
    NUM_TYPE = 500

    with open("text/passport.txt", "w") as f:
        for _ in range(NUM_NRC):
            f.writelines(pp_generator.nrc_generate() + "\n")
        for _ in range(NUM_NO):
            f.writelines(pp_generator.no_generate() + "\n")
        for _ in range(NUM_TYPE):
            f.writelines(pp_generator.type_generate() + "\n")
