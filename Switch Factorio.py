# import json
import os

variables = []
MODPACKNAMEFILE = "modpackname.txt"


'''
def getValuesFromFile():
    global variables
    log("\nGetting values from file")
    try:
        with open("Switch Factorio.json", "r+") as f:
            variables = json.loads(f.read())
            log("\nSuccess")
    except FileNotFoundError:
        log("\nFile not found")
        with open("Switch Factorio.json", "w") as f:
            f.write(json.dumps("['mods - DrakeNJack',{'mods - DrakeNJack','mods - Alone'}]"))
        getValuesFromFile()
'''


def getIntInput(stringMessage, stringErrorMessage, intUpperBound, intLowerBound=1):
    while True:
        try:
            choice = int(getInput(stringMessage))
            if intLowerBound <= choice <= intUpperBound:
                return choice
            else:
                print(stringErrorMessage)
        except ValueError:
            print(stringErrorMessage)


def getInput(stringMessage):
    return input(stringMessage)


def log(stringLog):
    with open("Switch Factorio log_latest.txt", "a") as f:
        f.write(stringLog)


def resetLog():
    try:
        os.remove("Switch Factorio log_previous.txt")
    except FileNotFoundError:
        pass
    try:
        os.rename("Switch Factorio log_latest.txt", "Switch Factorio log_previous.txt")
    except FileNotFoundError:
        pass
    log("Log Begin:")


def menu():
    subfolders = [f.path for f in os.scandir(os.curdir) if f.is_dir()]
    modfolders = []
    for folder in subfolders:
        try:
            with open(folder + "\\{}".format(MODPACKNAMEFILE), "r") as f:
                name = f.read()
                log("\nFound modpack named: {}".format(name))
                # print("Found modpack named: {}".format(name))
            modfolders.append(folder)
        except FileNotFoundError:
            pass
    modpackname = ""
    with open("mods\\{}".format(MODPACKNAMEFILE), "r") as f:
        modpackname = f.read()
    log("\nCurrent modpack is {}".format(modpackname))
    stringMessage = "Current modpack is {}.\nPlease select one of the options below:\n1). Keep this modpack\n".format(modpackname)
    counter = 2
    indexholder = {}
    for i in range(len(modfolders)):
        with open(modfolders[i] + "\\{}".format(MODPACKNAMEFILE), "r") as f:
            name = f.read()
            if name != modpackname:
                stringMessage += "{}). {}\n".format(counter, name)
                indexholder["{}".format(counter)] = name
                counter += 1
    print(indexholder)
    stringMessage += "{}). Create a new modpack\n".format(counter)
    choice = getIntInput(stringMessage, "Out of bounds. Enter between 1 and {}".format(counter), counter, 1)
    if choice != 1:
        if choice == counter:
            log("\nCreating new modpack")
            name = ""
            nameAvailable = False
            while not nameAvailable:
                name = getInput("Please name your modpack: ")
                if name != modpackname:
                    found = False
                    for value in indexholder:
                        if indexholder[value] == name:
                            found = True
                    if not found:
                        nameAvailable = True
                    else:
                        log("\nName \"{}\" already in use".format(name))
                        print("Name \"{}\" already in use".format(name))
                else:
                    log("\nName \"{}\" already in use".format(name))
                    print("Name \"{}\" already in use".format(name))

            modsfolder = "mods - " + name
            log("\n Creating a new modpack named {}".format(name))
            os.makedirs(modsfolder)
            os.makedirs("saves - " + name)
            with open(modsfolder+"\\{}".format(MODPACKNAMEFILE), "w") as f:
                f.write(name)
            log("\nModpack {} created".format(name))
            print("Modpack {} created".format(name))
            menu()
        else:
            log("\nSwitching active modpack from {} to {}".format(modpackname, indexholder[str(choice)]))
            os.rename("mods", "mods - " + modpackname)
            os.rename("saves", "saves - " + modpackname)
            os.rename("mods - " + indexholder[str(choice)], "mods")
            os.rename("saves - " + indexholder[str(choice)], "saves")
            log("\nSuccess")
            print("Success")


if __name__ == "__main__":
    os.chdir(os.environ.get("APPDATA") + "\\Factorio")
    resetLog()
    try:
        with open("mods\\{}".format(MODPACKNAMEFILE), "r") as f:
            pass
    except:
        name = getInput("Please name your first/default modpack: ")
        with open("mods\\{}".format(MODPACKNAMEFILE), "w") as f:
            f.write(name)
    # getValuesFromFile()
    menu()
