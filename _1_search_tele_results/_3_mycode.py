import csv
import re


# To update number in US number format if given as plain number
def _update_num(mob_num):
    upd_num = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', mob_num))
    return upd_num


# Retrieve each user record and swap if mobile number is in 3rd position
def _get_user_data(user_data):
    print("User data : ", user_data)
    user_data_strp = [data.strip() for data in user_data]  # strip spaces
    print("User data stripped: ", user_data_strp)
    is_num = any(char.isdigit() for char in user_data_strp[2])  # any all in python
    if is_num:
        if user_data_strp[2].isnumeric():
            num_formt = _update_num(user_data_strp[2])
            # num_formt = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', user_data[2]))
            user_data_strp[2] = num_formt
        user_data_strp[2], user_data_strp[3] = user_data_strp[3], user_data_strp[2]
    return user_data_strp


# Write data to output.txt file
def _write_data_to_file(fname, phone_data, out_file):
    heading = "Matches for: "+fname
    out_file.write(heading)
    row_no = 1
    for data in phone_data.values():
        if fname.lower() in (data[0].lower(), data[1].lower()):
            if fname.lower() == data[0].lower():
                res_rec = "Result "+str(row_no)+" : "+data[0]+", "+data[1]+", "+data[2]+", "+data[3]
            elif fname.lower() == data[1].lower():
                res_rec = "Result " + str(row_no) + " : " + data[1] + ", " + data[0] + ", " + data[2] + ", " + data[3]
            out_file.write('\n')
            out_file.write(res_rec)
            row_no += 1
    if row_no == 1:
        out_file.write('\n')
        out_file.write('No results found')
    out_file.write('\n')


# Read data from csv file
def read_data_from_csv():
    phone_data = {}
    with open('phone_dataset.csv') as file_obj:
        reader = csv.reader(file_obj)
        print("CSV Data ", reader)
        counter = 1
        for row in reader:
            print('row :', row)
            phone_data[counter] = _get_user_data(row[0].split(','))
            counter += 1
    return phone_data


# Read query names from text and write end result  to out text file
def write_data_to_txt(p_data):
    with open('query.txt') as in_data:
        names = in_data.readlines()
        # content = [x.rstrip() for x in names]
        content = []
        for x in names:
            content.append(x.rstrip())

        print("---Search names : ", content)
        out_file = open("output.txt", "w")
        for first_name in content:
            _write_data_to_file(first_name, p_data, out_file)


if __name__ == '__main__':
    # 1. Read data from csv and store in a dictionary
    ph_data = read_data_from_csv()
    print("Phone data : ", ph_data)

    # 2. Read query users, search and retrieve results
    write_data_to_txt(ph_data)
    print("Success")
