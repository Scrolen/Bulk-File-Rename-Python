import os


def rename_files(src, des, name, ext):
    files = os.listdir(src)

    for x, file in enumerate(files):
        os.rename(os.path.join(src, file), os.path.join(des, name+''.join([str(x), ext])))


def main():

    source = str(input("Enter The Source Path Containing The Files You Would Like to Rename: "))
    decision = str(input("Would you like to save the renamed files in a different directory than the source directory? (Y/N)")).upper()

    if decision == "N":
        destination = source
    else:
        destination = str(input("Type The Destination Path You Would Like to Store The Renamed Files In: "))

    file_name = str(input("Enter The New Name You Would Like The Files To Have: "))

    extension = str(input("Enter The Extension of The Files (ex. .jpg): "))

    rename_files(source, destination, file_name, extension)
    print("Renaming Files...")
    print("Successfully Renamed Files!")


main()
