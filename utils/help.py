def help():
    print("1. Install All Modules")
    print("2. How To Use This UserBot")
    print("3. EXIT HELPBHELP GELP HEEEELP")
    user_input = input("...> ").lower()

    if user_input in ["1", "one", "один"]:
        return install_modules()
    elif user_input in ["2", "two", "два", "два блять"]:
        return how_to_use()
    elif user_input in ["3", "three", "help", "три", "помргите", "спасите"]:
        print("no.")
        return help()
    else:
        return quit()


def install_modules():
    modules_list = ["pyrogram", "gtts"]
    try:
        import os
        os.system(f"pip install {modules_list[0]} {modules_list[1]}")
    except:
        print("Some mistake in short xd")
        quit()


def how_to_use():
    print("You should change the configuration file and insert your data there,")
    print("namely: \"api_id\", \"api_hash\". api_id should be first in the list, namely api[0],")
    print("and it is logical that api_hash is api[1].")
    print("Next, run the main file with the command \"python main.py\"")
    print("and specify your login details and restart the file (and NO wAy), everthing works")
    print("(don't forget to install all the modules for this)\n\n")
    print("The author does not collect your login data in any way,")
    print("you create a file in the main directory with a script with the .session extension")
    print("it is created by the pyrogram module.\n")
    print("If something went wrong, you can report it to me in a telegram - t.me/whateverehoami")
    print("интересно кому я это пишу если никто юзать это не будет")
    quit()


help()
