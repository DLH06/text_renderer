from typing import List

def get_data_from_file(path: str, num_line: int, num_dump: int) -> List[str]:
    result = []
    with open(path, "r") as f:
        data = f.readlines()
        if num_line != -1:
            data = data[:num_line]
        
        result = data*num_dump
        
    return result

if __name__ == "__main__":
    all_files = [
        ("text/en/country_code.txt", -1, 20),
        ("text/en/en_text.txt", -1, 100),

        ("text/db/mya_township.txt", -1, 10),

        ("text/gen_base/date_cant_convert.txt", -1, 1),
        ("text/gen_base/en_name.txt", -1, 1),
        ("text/gen_base/en_passport.txt", -1, 1),
    ]

    with open("text/en_ocr.txt", "w") as f:
        for item in all_files:
            data = get_data_from_file(item[0], item[1], item[2])
            for line in data:
                f.writelines(line.replace("\n", "")+"\n")

    all_files = [
        ("text/mya/mya_blood_type.txt", -1, 200),
        ("text/mya/mya_name.txt", -1, 1),
        ("text/mya/mya_new_2.txt", -1, 1),
        ("text/mya/mya_text.txt", -1, 200),

        ("text/mya/locations/city.txt", -1, 10),
        ("text/mya/locations/district.txt", -1, 50),
        ("text/mya/locations/region_and_state.txt", -1, 200),
        ("text/mya/locations/village.txt", -1, 100),
        
        ("text/gen_base/date_can_convert.txt", -1, 1),
        ("text/gen_base/mya_id_full.txt", -1, 1),
    ]

    with open("text/mya_ocr.txt", "w") as f:
        for item in all_files:
            data = get_data_from_file(item[0], item[1], item[2])
            for line in data:
                f.writelines(line.replace("\n", "")+"\n")
