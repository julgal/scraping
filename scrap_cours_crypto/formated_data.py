import os

def remove_duplicate_lines(input_file_name, output_file_name):
    single_lines = set()
    save_lines = []

    with open(input_file_name, 'r') as input_file:
        for line in input_file:
            if line not in single_lines:
                single_lines.add(line)
                save_lines.append(line)

    with open(output_file_name, 'w') as output_file:
        for line in save_lines:
            output_file.write(line)


def check_file_exists():
    folder = "Data"
    base = "data"
    extend = ".txt"
    num_file = 0
    while True:
        name_file = base + str(num_file) + extend
        complet_path = os.path.join(folder, name_file)
        if not os.path.exists(complet_path):
            break
        num_file += 1
    return name_file


def clean_up_files():
    old_name = "new_data.txt"
    new_name = "Data/" + check_file_exists()
    html_path = "./cours.html"
    file_path = "./data.txt"

    os.remove(file_path)
    os.remove(html_path)
    os.rename(old_name, new_name)


if __name__ == "__main__":
    remove_duplicate_lines('data.txt', 'new_data.txt')
    clean_up_files()

