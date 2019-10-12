import os
import hashlib
import sys
import time
from random import randint
while (1!=0):
    print("Hai Hackster!")
    print("I will set your codes at Fire!")
    print("The Source Codes are hidden in a 4D point. Enter its Co-Ordinates!")
    i = input()
    j = input()
    k = input()
    l = input()
    t = randint(-10000,10000)
    x = randint(-10000,10000)
    y = randint(-10000,10000)
    z = randint(-10000,10000)
    
    if (t==i):    
        if (x==j):
            if (y==k):
                if (z==l):
                    print("Block busted!")
                    
                    
                    file_list = []
                    
                    rootdir = "C:/"
                    
                    print("...Program starting...")
                    print("...Collecting virus... ")
                    
                    for subdir, dirs, files in os.walk(rootdir):
                        for file in files:
                            filepath = subdir + os.sep + file
                    
                            if filepath.endswith(".exe") or filepath.endswith(".dll"):
                                file_list.append(filepath)
                    
                    print("...Virus definition complete...")
                    print("...Starting scan...")
                    def countdown():
                        for x in range(4):
                            print(x+1)
                            time.sleep(1)
                    
                    countdown()
                    
                    def Scan():
                        infected_list = []
                        for f in file_list:
                            virus_defs = open("VirusLIST.txt", "r")
                            file_not_read = False
                            print("Scanning: {}".format(f))
                            hash = hashlib.md5()
                            try:
                                with open(f, "rb") as file:
                                    try:
                                        buf = file.read()
                                        file_not_read = True
                                        hash.update(buf)
                                        FILE_HASHED = hash.hexdigest()
                                        print("File md5 checksum: {}".format(FILE_HASHED))
                                        for line in virus_defs:
                                            if FILE_HASHED == line.strip():
                                                print("...Malware Detected... !!! File name: {}".format(f))
                                                infected_list.append(f)
                                            else:
                                                pass
                                    except Exception as e:
                                        print("Could not read file | Error: {}".format(e))
                            except:
                                pass
                        print("...Infected files found..!!!".format(infected_list))
                        deleteornot = str(input("Would you like to delete the infected files (y/n): "))
                        if deleteornot.upper() == "y":
                            for infected in infected_list:
                                os.remove(infected)
                                print("File removed: {}".format(infected))
                        else:
                            print("Executed with exit code 0")
                            os.system("PAUSE")
                    Scan()

    if (t!=i or x!=j or y!=k or z!=l):    
        print("Block can't be Crooked!")
    print(t,x,y,z)
    
    # Hai Hackster!                                                                                                                 
    # I will set your codes at Fire!                                                                                                
    # The Source Codes are hidden in a 4D point.Enter its Co-Ordinates!                                                            
        #2                                                                                                                             
        #5                                                                                                                             
        #6                                                                                                                             
        #9 
    # Block can't be Crooked!                                                                                                       
        #1165 8095 -7044 -6470
        


