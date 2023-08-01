import random
import math
from tqdm import tqdm


class enGenerator:
    def __init__(self) -> None:
        pass

    def generate_year(self) -> str:
        return str(random.randint(1900, 2070))

    def generate_month(self) -> str:
        return str(random.randint(1, 12))

    def generate_month_word(self) -> str:
        return random.choice(
            [
                "JAN",
                "FEB",
                "MAR",
                "APR",
                "MAY",
                "JUN",
                "JUL",
                "AUG",
                "SEP",
                "OCT",
                "NOV",
                "DEC",
            ]
        )

    def generate_day(self) -> str:
        return str(random.randint(1, 31))

    def generate_date_num(self) -> str:
        space = random.choice(["", " "])
        splitter = space + random.choice(["/", "-", "."]) + space
        dates = [
            self.generate_day()
            + splitter
            + self.generate_month()
            + splitter
            + self.generate_year(),
            self.generate_year()
            + splitter
            + self.generate_month()
            + splitter
            + self.generate_day(),
        ]
        return random.choice(dates)

    def generate_date_word(self) -> str:
        dates = [
            self.generate_day()
            + " "
            + self.generate_month_word()
            + " "
            + self.generate_year(),
            self.generate_year()
            + " "
            + self.generate_month_word()
            + " "
            + self.generate_day(),
        ]
        return random.choice(dates)

    def generate_number(self) -> str:
        return str(
            math.ceil(
                random.random() * random.choice([0] + [10**i for i in range(1, 11)])
            )
        )


class myaGenerator:
    def __init__(self) -> None:
        self.en_generator = enGenerator()
        self.mapping_dict = {
            "1": "၁",
            "2": "၂",
            "3": "၃",
            "4": "၄",
            "5": "၅",
            "6": "၆",
            "7": "၇",
            "8": "၈",
            "9": "၉",
            "0": "၀",
        }
        self.translation = str.maketrans(self.mapping_dict)

    def generate_year(self) -> str:
        year = self.en_generator.generate_year()
        return year.translate(self.translation)

    def generate_month(self) -> str:
        month = self.en_generator.generate_month()
        return month.translate(self.translation)

    def generate_day(self) -> str:
        day = self.en_generator.generate_day()
        return day.translate(self.translation)

    def generate_date_num(self) -> str:
        date = self.en_generator.generate_date_num()
        return date.translate(self.translation)

    def generate_number(self) -> str:
        num = self.en_generator.generate_number()
        return num.translate(self.translation)


if __name__ == "__main__":
    mya_generator = myaGenerator()
    en_generator = enGenerator()

    NUM_DATE_EN = 3000
    NUM_DATE_MYA = 3000

    with open("text/en/en_date.txt", "w") as f:
        for i in tqdm(range(NUM_DATE_EN), desc="Generate in English"):
            date = en_generator.generate_date_num()
            f.writelines(date + "\n")

    with open("text/mya/mya_date.txt", "w") as f:
        for i in tqdm(range(NUM_DATE_EN), desc="Generate in Burmese (Myanmar)"):
            date = mya_generator.generate_date_num()
            f.writelines(date + "\n")