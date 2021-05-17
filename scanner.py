import pyfiglet
import sys
import socket
from datetime import datetime
"""
This Project in a Development !!!
17 May 2021

"""
def intro(target):
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)
    
    # Add Banner 
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

def main(target):  
    try:
        
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
            
    except KeyboardInterrupt:
            print("\nUser Interrupt")
            sys.exit()
    except socket.gaierror:
            print("\nHostname Could Not Be Resolved")
            sys.exit()
    except socket.error:
            print("\Server not responding")
            sys.exit()

if __name__ == '__main__':

    # Defining a target
    if len(sys.argv) == 2:
        # translate hostname to IPv4
        target = socket.gethostbyname(sys.argv[1])
        
        # Intro
        intro(target)
        main(target) 
    else:
        print("Invalid ammount of Argument")