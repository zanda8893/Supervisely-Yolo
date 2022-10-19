#!/usr/bin/python3
from os import listdir, remove
import sys
import json

base_dir = "./"
colour_ints = {"blue_cone": 0,
               "yellow_cone": 1,
               "orange_cone": 2,
               "large_orange_cone": 3,
               "unknown_cone": 4}


def convert(folders):  # folders is a list of strings
    for folder in folders:
        jsons = sorted(listdir(base_dir + folder + "/ann"))

        for num, file in enumerate(jsons):

            if file.endswith(".json"):
                with open(base_dir + folder + "/ann/" + file, "r") as f:
                    jsondict = json.load(f)
                    convertedTXT = open(base_dir + folder + "/ann/" + file[:-8] + "txt", "w")
                    print(base_dir + folder + "/ann/" + file)

                    size = (jsondict["size"]["width"], jsondict["size"]["height"], )
                    print(size)

                    for cone in jsondict["objects"]:
                        print(cone["classTitle"])
                        print(str(colour_ints[cone["classTitle"]]))

                        convertedTXT.write(str(colour_ints[cone["classTitle"]]) + " " +
                                           str(((cone["points"]["exterior"][1][0] +
                                                 cone["points"]["exterior"][0][0]) / 2) / size[0]) + " " +
                                           str(((cone["points"]["exterior"][1][1] +
                                                 cone["points"]["exterior"][0][1]) / 2) / size[1]) + " " +
                                           str((cone["points"]["exterior"][1][0] -
                                                cone["points"]["exterior"][0][0]) / size[0]) + " " +
                                           str((cone["points"]["exterior"][1][1] -
                                                cone["points"]["exterior"][0][1]) / size[1]) + "\n")
                    convertedTXT.close()
                    remove(base_dir + folder + "/ann/" + file)


if __name__ == '__main__':
    folders = sorted(listdir(base_dir))  # Load folders from base directory

    if "--no-interactive" not in sys.argv:
        print("Select which folder to convert or * to convert all")
        for num, filename in enumerate(folders):  # print list of folders to select from
            print("    ", filename, " ", num)

        choice = str(input("Enter choice: "))

        if choice == "*":  # if all folders are selected
            convert(folders)
        else:  # if a specific folder is selected
            convert([folders[int(choice)]])

    convert(folders)
