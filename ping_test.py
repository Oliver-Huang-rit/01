#!/usr/bin/env python3
# Author: Oliver Huang
# Date: 09/05/2021

import os
import sys
from os import system, name
import subprocess

#clear the terminal
if name == 'nt': # if the system is Windows
    _ = system('cls')
else: # if is other system
    _ = system('clear')

def findGatewayIP():
    # function to fint the IP of the gateway
    output = os.popen("netstat -nr").readlines()
    # get the output of the 'netstat -nr' command
    gateway_ip = ""
    for line in output:
        sent = False
        
        seg = line.split(" ")
        checker = True
        for ele in seg:
            if checker == True:
                if (ele == "0.0.0.0"): 
                    sent = True 
                    # turn sent to true if the current line is the line contains gateway IP infomation
                    checker = False
                    # turn the checker tp false to prevent further checking
                
        if (sent == True):
            for i in range(0, len(seg)):
                if seg[i] != "0.0.0.0":
                    temp_t = seg[i].split(".")
                    if (len(temp_t) > 1):
                        # check if current temp_t contains the gateway IP
                        gateway_ip = seg[i]
                        return gateway_ip
    return gateway_ip
    # return the gateway IP

def ping(host, times):
    # funtion to ping the inputed host by inputed times (only for pre-programed ping)
    param = '-n' if name == 'nt' else '-c'
    # if the system if windows, param set to -n
    # else param set tp -c

    command = ['ping', param, str(times), host]
    #create the command to ping

    return (subprocess.call(command) == 0)
    # return the result of the ping
    # if the ping success, True returned
    # if the ping failed, False returned

def custom_ping(host, times):
    # funtion to ping the inputed host by inputed times
    param = '-n' if name == 'nt' else '-c'
    # if the system if windows, param set to -n
    # else param set tp -c

    command = ['ping', param, str(times), host]
    #create the command to ping

    return str(subprocess.call(command))
    # return the result of the ping
    # if the ping success, True returned
    # if the ping failed, False returned

def main():
    # the main function that do the test
    gateway = findGatewayIP() # get the gateway IP
    sys.stdout.write("\033[1;34m")
    command = input("Enter Q/q to quit, or other to start the test: ")
    # ask the user if wanna quit
    sent = False
    if command != "Q" and command != "q" and command != "Q/q":
        sent = True
        # check the responed
    while sent == True:
        # ping itslef
        result = ping("127.0.0.1", 1)
        if (result == True):
            sys.stdout.write("\033[0;32m")
            print("\nSelf-ping succeeded!\n")
        else:
            sys.stdout.write("\033[0;31m")
            print("\nSelf-ping failed! Please contact your system administrator\n")
        # print the result

        sys.stdout.write("\033[1;34m")
        command = input("\nAbout to ping the gateway, enter Q/q to quit, or enter other to contiune the test: ")
        if command == "Q" or command == "q" or command == "Q/q":
            sent = False
            break
            # ask the user if wanna quit
        result = ping(gateway, 1)
        # ping the gateway
        if (result == True):
            sys.stdout.write("\033[0;32m")
            print("\nPing gateway succeeded!\n")
        else:
            sys.stdout.write("\033[0;31m")
            print("\nPing gateway failed! Please contact your system administrator\n")
        # print the result

        sys.stdout.write("\033[1;34m")
        command = input("\nAbout to ping '8.8.8.8', enter Q/q to quit, or enter other to contiune the test: ")
        if command == "Q" or command == "q" or command == "Q/q":
            sent = False
            break
            # ask the user if wanna quit
        result = ping("8.8.8.8", 1)
        # ping '8.8.8.8'
        if (result == True):
            sys.stdout.write("\033[0;32m")
            print("\nPing 8.8.8.8 succeeded!\n")
        else:
            sys.stdout.write("\033[0;31m")
            print("\nPing 8.8.8.8 failed! Please contact your system administrator\n")
        # pint the result

        sys.stdout.write("\033[1;34m")
        command = input("\nAbout to ping the RIT DNS Server, enter Q/q to quit, or enter other to contiune the test: ")
        if command == "Q" or command == "q" or command == "Q/q":
            sent = False
            break
            # ask the user if wanna quit
        ping("129.21.3.17", 1)
        # ping the RIT DNS server
        if (result == True):
            sys.stdout.write("\033[0;32m")
            print("\nPing RIT DNS server succeeded!\n")
        else:
            sys.stdout.write("\033[0;31m")
            print("\nPing RIT DNS server failed! Please contact your system administrator\n")
        # print the result

        sys.stdout.write("\033[1;34m")
        command = input("\nAbout to ping 'www.google.com', enter Q/q to quit, or enter other to contiune the test: ")
        if command == "Q" or command == "q" or command == "Q/q":
            sent = False
            break
            # ask the user if wanna quit
        result = ping("www.google.com", 1)
        # ping 'www.google.com'
        if (result == True):
            sys.stdout.write("\033[0;32m")
            print("\nPing www.google.com succeeded!\n")
        else:
            sys.stdout.write("\033[0;31m")
            print("\nPing www.google.com failed! Please contact your system administrator\n")
        # print the result

        sys.stdout.write("\033[1;34m")
        command = input("\nAll tests have been passed sucessfully! Enter Q/q to quit, enter other to contiune the test: ")
        if command == "Q" or command == "q" or command == "Q/q":
            sent = False
            break
            # ask the user if wanna quit

        command = input("Enter an ip or url you want to ping(Enter Q/q or blank to quit): ")
        # ask user to enter a destination the user wants to ping, or quit
        while command != "Q" and command != "q" and command != "Q/q" and command != "":
            result = custom_ping(command, 1)
            print(result)
            if result == "0":
                sys.stdout.write("\033[0;32m")
                print("\nPing", command, "succeeded!\n")
                # output of a successful ping
            elif result == "512":
                sys.stdout.write("\033[0;35m")
                print("Name or service not known:", command)
                # output if a unknown name or service is entered
            else:
                sys.stdout.write("\033[0;31m")
                print("\nPing", command, "failed! The service is down\n")
                # output if the service is down
            sys.stdout.write("\033[1;34m")
            command = input("\nAll tests have been passed sucessfully! Enter Q/q to quit, enter other to contiune the test: ")
            # ask user to enter a destination the user wants to ping, or quit
        
        sys.stdout.write("\033[1;34m")
        command = input("\nEnter Q/q to quit, enter other to restart the test: ")
        if command == "Q" or command == "q" or command == "Q/q":
            sent = False
            break
            # ask the user if wanna quit or restart the test

    sys.stdout.write("\u001b[37m")

if __name__ == '__main__':
    main()
    # run the main function