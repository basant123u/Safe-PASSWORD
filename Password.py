filename1 = "user.txt1"
filename2 = "user.txt2"
filename3 = "user.txt3"
filename4 = "user.txt4"
filename5 = "user.txt5"
filename6 = "user.txt6"
filename7 = "user.txt7"
filename8 = "user.txt8"
filename9 = "user.txt9"
filename10 = "user.txt10"
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
import sys
import colorama
import time
from colorama import Fore
R = Fore.RED
B = Fore.BLUE
W = Fore.WHITE
Y = Fore.YELLOW
G = Fore.GREEN
BL = Fore.BLACK
print(f"{G}Starting...")
time.sleep(1)
print(f"""{R}
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                           {Y} -by Alpha X
                                                V 0.0.1""")
a = input(f"{W}PRESS ENTER TO PROCEED...")
if(a==""):
    for b in range(75):
        print(f"{BL}-",end='')
        time.sleep(0.0000000001)
    print()
    print(f"{R}[0] {B}STORE PASSWORD")
    print(f"{R}[1] {B}VIEW PASSWORDS")
    for b in range(75):
        print(f"{BL}-",end='')
        time.sleep(0.0000000001)
else:
    print(f"{R}BEHEN LE LODE GAANDMASTI MAT KAR...TERA MAA XHOD DUNGA")
print()
c = int(input())
if (c==0):
    with open(filename1, "w") as file1:
        d = file1.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")           #PASS : 1
        e = file1.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
        f = file1.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
        print(f"{R}saved successfully...")
        g2 = input(f"{G}want to continue y/n"+"\n")
        if(g2=="y"):
            with open(filename2, "w") as file2:
                x = file2.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")      #PASS : 2
                y = file2.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file2.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            clear()
            print(f"{Y}Thanks for using !!!")
            quit()
        g3 = input(f"{G}want to continue y/n"+"\n")
        if(g3=="y"):
            with open(filename3, "w") as file3:
                x = file3.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")         #PASS : 3
                y = file3.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file3.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g4 = input(f"{G}want to continue y/n"+"\n")
        if(g4=="y"):
            with open(filename4, "w") as file4:
                x = file4.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")         #PASS : 4
                y = file4.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file4.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g5 = input(f"{G}want to continue y/n"+"\n")
        if(g5=="y"):
            with open(filename5, "w") as file5:
                x = file5.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")           #PASS : 5
                y = file5.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file5.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g6 = input(f"{G}want to continue y/n"+"\n")
        if(g6=="y"):
            with open(filename6, "w") as file6:
                x = file6.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")            #PASS : 6
                y = file6.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file6.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g7 = input(f"{G}want to continue y/n"+"\n")
        if(g7=="y"):
            with open(filename7, "w") as file7:
                x = file7.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")            #PASS : 7
                y = file7.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file7.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g8 = input(f"{G}want to continue y/n"+"\n")
        if(g8=="y"):
            with open(filename8, "w") as file8:
                x = file8.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")             #PASS : 8
                y = file8.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file8.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g9 = input(f"{G}want to continue y/n"+"\n")
        if(g9=="y"):
            with open(filename9, "w") as file9: 
                x = file9.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")         #PASS : 9
                y = file9.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file9.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
        g10 = input(f"{G}want to continue y/n"+"\n")
        if(g10=="y"):
            with open(filename10, "w") as file10:
                
                x = file10.write("NAME : " + input(f"{Y}ENTER THE NAME : ") + "\n")          #PASS : 10
                y = file10.write("USERNAME : " + input(f"{Y}ENTER USERNAME : ") + "\n")
                z = file10.write("PASSWORD : " + input(f"{Y}ENTER PASSWORD : ") + "\n")
                print(f"{R}saved successfully...")
        else:
            print(f"{Y}Thanks for using !!!")
            quit()
            
if(c==1):
            try:
                print(f"{G}Gathering information...")
                time.sleep(2)
                print(f"{R}RESULT #1")
                print(f"{B}")
                print(open(filename1).read())
                print(f"{R}RESULT #2")
                print(f"{B}")
                print(open(filename2).read())
                print(f"{R}RESULT #3")
                print(f"{B}")
                print(open(filename3).read())
                print(f"{R}RESULT #4")
                print(f"{B}")
                print(open(filename4).read())
                print(f"{R}RESULT #5")
                print(f"{B}")
                print(open(filename5).read())
                print(f"{R}RESULT #6")
                print(f"{B}")
                print(open(filename6).read())
                print(f"{R}RESULT #7")
                print(f"{B}")
                print(open(filename7).read())
                print(f"{R}RESULT #8")
                print(f"{B}")
                print(open(filename8).read())
                print(f"{R}RESULT #9")
                print(f"{B}")
                print(open(filename9).read())
                print(f"{R}RESULT #10")
                print(f"{B}")
                print(open(filename10).read())
            except FileNotFoundError:
                print("CHUTIYE INPUT TOH DAAL LE")                                                                          