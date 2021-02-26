import csv
import random

first_names = []
last_names = []
middle_names = []
middle_initials = []
fn_weights = []
ln_weights = []
mn_weights = []
mi_weights = []

# Load name data (first names are used for middle names)
with open('First Names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        name = str(line[0])
        weight = float(line[4])
        first_names.append(name)
        fn_weights.append(weight)
        middle_names.append(name)
        mn_weights.append(weight)
with open('Last Names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        name = str(line[0])
        weight = float(line[4])
        last_names.append(name)
        ln_weights.append(weight)
with open('Middle Initials.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        initial = str(line[0])
        weight = float(line[3])
        middle_initials.append(initial)
        mi_weights.append(weight)


def fill_fn_ln_list(lis):
    # Selects a name based on a weighted random choice.
    random_fn = random.choices(first_names, weights=fn_weights, k=20000)
    random_ln = random.choices(last_names, weights=ln_weights, k=20000)
    for x in range(20000):
        first_name = random_fn[x]
        last_name = random_ln[x]
        full_name = first_name + last_name
        lis.append(full_name)


def fill_fn_mi_ln_list(lis):
    # Selects a name based on a weighted random choice.
    random_fn = random.choices(first_names, weights=fn_weights, k=20000)
    random_mi = random.choices(middle_initials, weights=mi_weights, k=20000)
    random_ln = random.choices(last_names, weights=ln_weights, k=20000)
    for x in range(20000):
        first_name = random_fn[x]
        middle_initial = random_mi[x]
        last_name = random_ln[x]
        full_name = first_name + middle_initial + last_name
        lis.append(full_name)


def fill_fn_mn_ln_list(lis):
    # Selects a name based on a weighted random choice.
    random_fn = random.choices(first_names, weights=fn_weights, k=20000)
    random_mn = random.choices(middle_names, weights=mn_weights, k=20000)
    random_ln = random.choices(last_names, weights=ln_weights, k=20000)
    for x in range(20000):
        first_name = random_fn[x]
        middle_name = random_mn[x]
        last_name = random_ln[x]
        full_name = first_name + middle_name + last_name
        lis.append(full_name)


def find_matches(lis):
    # Check for possible anagrams
    counter = 0
    for x in range(len(lis)):
        if len(lis[x]) != 13:
            continue
        letter_dict = {}
        for letter in lis[x]:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict.update({letter: 1})

        unique = len(letter_dict)
        singles = 0
        doubles = 0
        triples = 0

        for key, value in letter_dict.items():
            if value == 1:
                singles += 1
            if value == 2:
                doubles += 1
            if value == 3:
                triples += 1

        if (unique == 8) and (singles == 4) and (doubles == 3) and (triples == 1):
            counter += 1
    return counter


if __name__ == '__main__':
    final_fn_ln_total = 0
    final_fn_mi_ln_total = 0
    final_fn_mn_ln_total = 0
    final_total = 0

    for i in range(20000):
        fn_ln_list = []
        fn_mi_ln_list = []
        fn_mn_ln_list = []
        fill_fn_ln_list(fn_ln_list)
        fill_fn_mi_ln_list(fn_mi_ln_list)
        fill_fn_mn_ln_list(fn_mn_ln_list)

        fn_ln_total = find_matches(fn_ln_list)
        fn_mi_ln_total = find_matches(fn_mi_ln_list)
        fn_mn_ln_total = find_matches(fn_mn_ln_list)
        total = fn_ln_total + fn_mi_ln_total + fn_mn_ln_total

        final_fn_ln_total += fn_ln_total
        final_fn_mi_ln_total += fn_mi_ln_total
        final_fn_mn_ln_total += fn_mn_ln_total
        final_total += total

        print("First Name, Last Name: " + str(fn_ln_total))
        print("First Name, Middle Initial, Last Name: " + str(fn_mi_ln_total))
        print("First Name, Middle Name, Last Name: " + str(fn_mn_ln_total))
        print("Total: " + str(total))

    print("First Name, Last Name (Average): " + str((final_fn_ln_total / 20000)))
    print("First Name, Middle Initial, Last Name (Average): " + str((final_fn_mi_ln_total / 20000)))
    print("First Name, Middle Name, Last Name (Average): " + str((final_fn_mn_ln_total / 20000)))
    print("Total (Average): " + str((final_total / 20000)))
