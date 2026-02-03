


def print_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("הקובץ לא נמצא.")
    except Exception as e:
        print("אירעה שגיאה:", e)


print_file_contents("./example.txt")

def print_file(filename):
    try:
        with open(filename, 'w') as f:
            a = f.write("hello baba")
            print(a)
    except FileNotFoundError:
        print("לא הוספת כלום")
print_file("./example.txt")

def copy_file(source_filename, traget_filename):
    try:
        with open(source_filename, 'r') as f:
            content = f.read()
        with open(traget_filename, 'w') as f:
            f.write(content)
            print("bravo")
    except FileNotFoundError:
        print("ya rien")
copy_file("./source.txt", "./traget.txt")

def file_line(filename):
    try:
        with open(filename, 'r') as f:
            line_count = 0
            for line in f:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("זה לא נכון")
        return -1
num = file_line("./example.txt")
if num != -1:
    print(num)

def pyton_word(filename,word):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        words = content.split()
        count = words.count(word)
        return count
    except FileNotFoundError:
        print("il et pas")
        return -1
num = pyton_word("./example.txt",'python')
print(num)

import os

def copy_py_to_txt(py_filename):
    try:
        base, ext = os.path.splitext(py_filename)
        if ext != ".py":
            print("זה לא קובץ פייתון.")
            return

        txt_filename = base + ".txt"

        with open(py_filename, 'r', encoding='utf-8') as src:
            content = src.read()
        with open(txt_filename, 'w', encoding='utf-8') as dst:
            dst.write(content)

        print("נוצר הקובץ:", txt_filename)

    except FileNotFoundError:
        print("הקובץ לא נמצא.")
    except Exception as e:
        print("אירעה שגיאה:", e)

copy_py_to_txt("example.py")

def replace_in_file(filename, search_text, replace_text):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace(search_text, replace_text)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print("ההחלפה בוצעה בהצלחה.")

    except FileNotFoundError:
        print("הקובץ לא נמצא.")
    except Exception as e:
        print("אירעה שגיאה:", e)
replace_in_file("example.txt", "שלום", "היי")

def append_lines_to_file(filename, lines):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
        print("השורות נוספו בהצלחה.")
    except FileNotFoundError:
        print("הקובץ לא נמצא.")
    except Exception as e:
        print("אירעה שגיאה:", e)
append_lines_to_file("example.txt", ["שורה חדשה 1", "שורה חדשה 2", "שורה חדשה 3"])

