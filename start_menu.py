import os
import glob
from termcolor import colored, cprint



print("                          .%@@@%                           ")
print("                    @#               #@                    ")
print("        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        ")
print("        @     @                             @     @        ")
print("        @   @             @@@@@@@             @   @        ")
print("        @ @@@@           @@@@@@@@@           @@@@ @        ")
print("        @@ @@@@@@@.       @@@@@@@       ,@@@@@@@ @@        ")
print("        @      @@@@@@@@    ,@@@,    @@@@@@@@      @        ")
print("       &@            *%@@@@@@@@@@@@@%*            @&       ")
print("       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       ")
print("        @               @@@@@@@@@@@               @        ")
print("      @ @               @@@@@@@@@@@               @ @      ")
print("      @ @               @@@@@@@@@@@               @ @      ")
print("        @               @@@@@@@@@@@               @        ")
print("       @@               @@@@@@@@@@@               @@       ")
print("       %@              @@@@@@@@@@@@@              @%       ")
print("        @            @@@.@@@@ @@@@.@@@            @        ")
print("        @@          @@@@ @@@@ @@@@ @@@@          @@        ")
print("        @ @        @@@@@ @@@@ @@@@ @@@@@        @ @        ")
print("        @     @ .@@@@    @@@@ @@@@    @@@@  @     @        ")
print("        @       @@@      @@@@ @@@@      @@@       @        ")
print("        @           @@   @@@@ @@@@   @@           @        ")
print("         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         ")
print("")
print("                         Vitruvian                         ")

QuickstartFiles = []
#i = 0
#for file in QuickstartFiles:
#   cprint(i + ") " + file, "file.color")
#   i++

vitruvianIsActive = True
while vitruvianIsActive == True:
    print("Choose an option")
    print("[1] Quit")
    print("[2] Add Password")
    print("[3] Delete Password")
    print("[4] List Passwords")
    option = input()
    if(option.isdigit()):
        option = int(option)
    else:
        cprint("Not Valid", "red")

    if option == 1:
        vitruvianIsActive = False
    elif option == 2:
        nameoffile = input("What is this password for? ")
        os.system("touch ~/Documents/vitruvian/Passwords/" + nameoffile + ".txt")
        password = input("What is the password for " + nameoffile + "? ")
        os.system("echo " + password + " >> ~/Documents/vitruvian/Passwords/" + nameoffile + ".txt")
    elif option == 3:
        filetodelete = input("what password do you want to delete? ")
        os.system("rm ~/Documents/vitruvian/Passwords/" + filetodelete + ".txt")
    elif option == 4:
        print(os.listdir(os.path.expanduser("~/Documents/vitruvian/Passwords")))
