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
    print("")
    option = input()
    if(option.isdigit()):
        option = int(option)
    else:
        cprint("Not Valid", "red")

    if option == 1:
        vitruvianIsActive = False

