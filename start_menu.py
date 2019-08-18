import os
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
    option = input()
    if(option.isdigit()):
        option = int(option)
    else:
        cprint("Not Valid", "red")

    if option == 1:
        vitruvianIsActive = False
    elif option == 2:
        nameoffile = input("What is this password for? ")
        os.system("touch ~/Documents/vitruvian/" + nameoffile + ".txt")
        password = input("What is the password for " + nameoffile + "? ")
        os.system("echo " + password + " >> ~/Documents/vitruvian/" + nameoffile + ".txt")
    elif option == 3:
        filetodelete = input("what password do you want to delete? ")
        os.system("rm ~/Documents/vitruvian/" + filetodelete + ".txt")
