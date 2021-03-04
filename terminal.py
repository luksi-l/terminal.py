print("please login!")
name = input("username:")
import time
print("--------------------------------------------------------------------------------")
print("                            welcome " + name)
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to exit? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
elif answer == "version":
    print("version of console is 2.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("jupyter")
    print("tkinter")
    print("sys")
    print("math")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
elif answer == "pkg install":
    print("what do you want to install?")
    print()
    print("pkg install <package>")
elif answer == "pkg install gedit":
    print("geting informations...")
    time.sleep(2)
    print("loading . . .")
    time.sleep(3)
    print("next packages will be installed:")
    print("gedit running package")
    print("gedit 64x")
    print("gedit 32x")
    print("gedit 86x")
    print("gedit numbers")
    print("5 installed, 0 removed, 0 upgraded, 1 updated")
    answer5 = input("do you want to continue(y/n) ")
    if answer5 == "y":
        print("gedit running package installing")
        time.sleep(6)
        print("gedit 64x installing")
        time.sleep(3)
        print("gedit 32x installing")
        time.sleep(1)
        print("gedit 86x installing")
        time.sleep(2)
        print("gedit numbers installing")
        time.sleep(7)
        print("done!")
    else:
        print("abort!")
elif answer == "jupyter":
    import jupyter
elif answer == "tkinter":
    import tkinter
elif answer == "sys":
    import sys
elif answer == "math":
    import math
    print("now do math!")
elif answer == "math pi":
    print("pi is:")
    math.pi
elif answer == "luksi-h":
    print("NOTE:IF YOU INSTALL THIS TOOL YOU CAN'T BACK TO TERMINAL")
    answer6 = input("ARE YOU SURE YOU WANT TO INSTALL THOSE TOOLS[y/n]")
    if answer6 == "y":
        print("installing hydra tools . . .")
        time.sleep(4)
        print("installing hydra examples . . .")
        time.sleep(2)
        print("installing hydra packages . . .")
        time.sleep(5)
        print("installing nmap tools . . .")
        time.sleep(1)
        print("installing nmap examples . . .")
        time.sleep(2)
        print("installing nmap packages . . .")
        time.sleep(4)
        print("done...")
        time.sleep(1)
        print("welcome to hacker zone!")
        print("now chosse one of this programs . . .")
        print("nmap,hydra.")
        luksi = input("answer: ")
        if luksi == "nmap":
            print("do this command:")
            print("nmap -v -sn 192.168.0.0/16 10.0.0.0/8")
            nmap = input(">>>")
            if nmap == "nmap -v -sn 192.168.0.0/16 10.0.0.0/8":
                print("scaning . . .")
                time.sleep(2)
                print("1 address found(0 host) . . .")
                time.sleep(1)
                print("to be continued . . .")
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
        else:
            print("do this command:")
            print("i will make text files with info")
            print("hydra -l user -P passlist.txt ftp://192.168.0.1")
            hydra = input(">>>")
            if hydra == "hydra -l user -P passlist.txt ftp://192.168.0.1":
                print("getting password . . .")
                time.sleep(2)
                print("getting email . . .")
                time.sleep(1)
                print("done!")
                time.sleep(1)
                print("to be continued . . .")
                time.sleep(1)
                quit()
            else:
                print("looks like you don't like to hack . . .")
                time.sleep(1)
                print("okay . . .")
                time.sleep(1)
                print("say goodbye to your computer . . .")
                print(">:)")
                time.sleep(1)
                print("goodbye!")
                quit()
    else:
        print("abort!")
        print("installing this is dangerous!")
elif answer == "amongus":
            print("""⠀             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀this is your appearance""")
else:
    print("no command found")
