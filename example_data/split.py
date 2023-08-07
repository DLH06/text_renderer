import os
import random
from tqdm import tqdm


if __name__ == "__main__":
    with open("text/mya/mya_new.txt", "r") as f:
        data = f.readlines()
        data = [each.replace("\n", "") for each in data]
    print(len(data))
    new_lines = []
    for index, line in enumerate(tqdm(data)):
        if len(line) <= 130:
            new_lines.append(line)
        else:
            temp = line.split()
            while True:
                splitter = random.randint(1, len(temp))
                split_line = " ".join(temp[:splitter])
                if len(split_line) < 130:
                    new_lines.append(split_line)
                    if splitter == len(temp):
                        break
                    else:
                        temp = temp[splitter:]
    print(len(new_lines))
    with open("text/mya/mya_new_3.txt", "w") as f:
        for line in data:
            f.writelines(line+"\n")