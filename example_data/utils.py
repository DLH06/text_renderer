from typing import List

def get_data_from_file(path: str, num_line: int) -> List[str]:
    with open(path, "r") as f:
        data = f.readlines()
        if num_line != -1:
            data = data[:num_line]
        
    return data

if __name__ == "__main__":
    all_files = [
        ("text/en/country_code.txt", -1),
        ("text/en/en_date.txt", -1),
        ("text/en/en_text.txt", -1),
        ("text/en/mya_name.txt", -1),
        ("text/en/mya_township.txt", -1),
        ("text/en/passport.txt", -1),
    ]

    with open("text/en/en_ocr.txt", "w") as f:
        for item in all_files:
            data = get_data_from_file(item[0], item[1])
            for line in data:
                f.writelines(line)

    all_files = [
        ("text/mya/mya_date.txt", -1),
        ("text/mya/mya_tesseract_text.txt", -1),
        ("text/mya/mya_text.txt", -1),
    ]

    with open("text/mya/mya_ocr.txt", "w") as f:
        for item in all_files:
            data = get_data_from_file(item[0], item[1])
            for line in data:
                f.writelines(line)
