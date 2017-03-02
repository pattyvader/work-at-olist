def read_file(name_file):
    try:
        file_csv = open(name_file, "r")

        return file_csv
    except IOError as error_import:
        print("Error: {0}".format(error_import))
