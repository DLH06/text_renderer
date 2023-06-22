import random


class passportGenerator:
    def __init__(self) -> None:
        self.sex = ["N", "M"]
        with open("text/mya_township.txt", "r") as f:
            self.township = f.readlines()
            self.township = [
                each.replace("\n", "").replace("-", "").replace(" ", "").upper()
                for each in self.township
            ]

    def nrc_generator(self) -> str:
        region_code = random.randint(1, 14)
        township = random.choice(self.township)
        sex = random.choice(self.sex)
        serial_number = random.randint(100000, 999999)
        return "{}/{}({}){}".format(region_code, township, sex, serial_number)
    

if __name__ == "__main__":
    pp_generator = passportGenerator()

    NUM_NRC = 500

    with open("text/nrc_passport.txt", "w") as f:
        for _ in range(NUM_NRC):
            f.writelines(pp_generator.nrc_generator() + "\n")
