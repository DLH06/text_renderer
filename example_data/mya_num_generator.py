import random
import math


class enGenerator:
    def __init__(self) -> None:
        pass

    def generate_year(self):
        return str(random.randint(1900, 2070))

    def generate_month(self):
        return str(random.randint(1, 12))

    def generate_day(self):
        return str(random.randint(1, 31))

    def generate_date(self):
        splitter = random.choice(["/", "-"])
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

    def generate_number(self):
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

    def generate_year(self):
        year = self.en_generator.generate_year()
        return year.translate(self.translation)

    def generate_month(self):
        month = self.en_generator.generate_month()
        return month.translate(self.translation)

    def generate_day(self):
        day = self.en_generator.generate_day()
        return day.translate(self.translation)

    def generate_date(self):
        date = self.en_generator.generate_date()
        return date.translate(self.translation)

    def generate_number(self):
        num = self.en_generator.generate_number()
        return num.translate(self.translation)
