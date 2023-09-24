from colorama import init, Fore
import requests, random, re, sys ,os, time, platform
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from tkinter import Tk
from tkinter.filedialog import askopenfilename

init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
yellow= Fore.YELLOW
mag = Fore.MAGENTA
white= Fore.WHITE
blue = Fore.BLUE




# for validating numbers 
def numberValidator(number, name):
    
    url = 'https://login.microsoftonline.com/common/GetCredentialType?mkt=en-US'

    payload_template = {
        "isOtherIdpSupported": True,
        "checkPhones": False,
        "isRemoteNGCSupported": True,
        "isCookieBannerShown": False,
        "isFidoSupported": True,
        "country": "US",
        "forceotclogin": False,
        "isExternalFederationDisallowed": False,
        "isRemoteConnectSupported": False,
        "federationFlags": 0,
        "isSignup": False,
        "flowToken": "AQABAAEAAAAtyolDObpQQ5VtlI4uGjEPmVTvB5eZTaL_xvRdNX8zoF_M9oCPfpR1_3-Wz9ETrDbl5ca9Avq0LYJkoyoMgY5LIhrw_zFYKZPKDynsKoHPZfgeKmWiIAs1DXbLOrj1FwddvGzTm1ABWqIWhpNkryjIGv9-pljgbUnhPWj9pTn9ffvUpp8V2MtaAhrj46pyDne0WQmgpo5yxrOcie6NRDmX-vIRN1MIuXjLJ27VP51D0OM2hEp1OD47P6dtU6fk3-n2oCqUh1nP1tJCP1Pr47Uw2d3Hx3uCPYHHQJ8S3DkYwNqi4ieYGWQoRIaGrswGKuHiQRsyIuf8jtXEVXyOGqJhVIrV13orhsMe8QFdNAQE95yTcr7oSV6cXL7EWJdelszMsPUosCWSNdpwVI3lFGrKkYHetSaT2PrQem5AJIKBpKpvdLzk4q_P1P5_HA5hrOLCjH451cW4GJ2aVLL8wejgiEdppAzICHiHJOAthyGUP1R7w0z62wD6Ml9QOrRuqGS1KRxOCycJSUhLQcXDX5yIL1PCokaNJIAca5y1wkJb4zMbwhsGoVaUnWZK8XjTWYovsLqEn1dvUW_GrQxdQzwyIAA",
        "isAccessPassSupported": True,
        "username": number
    }


    headers = {
        "Host": "login.microsoftonline.com",
        # (other headers here)
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close"
    }

    response = requests.post(url,headers=headers,json=payload_template)
    x = response.json()
    # print(x)
    if_exists_result = x["IfExistsResult"]

    if if_exists_result == 5 or if_exists_result == 0:
        print (f'{mag}==> Valid.....{green}{number}')
        save(number,name)
        
    else:
        print (f'{mag}==> Invalid...{red}{number}')
        
# numberValidator('sawdyk12d3@gmail.com')

#Generating 150,000 numbers
def numberGenerator(name,number):
    try:
        print('Generating leads, please hold ....')
        if len(number) == 3:
            start = number
            starting = int(start+"0000000")
            ending = int(start+"9999999")
            for i in range(150000):
                number1 = random.randint(starting,ending)
                original = "1"+str(number1)
                save(original,name)
        else:
            start = number
            starting = int(start+"000001")
            ending = int(start+"999999")
            for i in range(150000):
                number1 = random.randint(starting,ending)
                original = "1"+str(number1)
                save(original,name)
        print("done")
    except:
        pass


# to save 
def save(number, name):
    with open(name, 'a') as save:
        save.write(f"{number}\n")
        

def get_file_path():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt")],title="Select File to Validate")
    root.destroy()
    return file_path


def run():
    try:
        x = 1
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')
            
        print()
        print(f"""
        
        {red}GENERATOR & VALIDATOR v1
                            {white}Coded by Pop(G)
                            {red}telegram: https:t.me/iampopg
                            
        """)
        print()
        if not os.path.exists('result'):
            os.makedirs('result')
        print(f"""
            
            {yellow} [1] {mag}Generate number leads
            {yellow} [2] {mag}Validate leads
            {yellow} [3] {mag}Generate and validate
            {yellow} [4] {mag}Exit
            
            """)
    
        option = input(f"{yellow}Enter an option: ")
       
        while option not in ['1', '2', '3', '4']:
            print(red + 'Enter between 1-4, check the option above')
            option = input("Enter an option: ")
            
         # for generate 
        if option == '1':
            print(f'{yellow}Enter the first 3/4 starting number of your target without +1(e.g 513 or 5134)')
            target = input(": ")
            
            if len(target) == 3 or len(target) == 4:
                output = input(yellow + "Enter name to save the generated number: ")
                if not output.endswith('.txt'):
                    output= output+".txt"
                # output = 'result/' + output
                numberGenerator(output,target)
                print()
                input(f"{mag}Done and saved to {green}{output}")
                run()
            else: 
                print()
                print(f"I repeate, Enter {red}Enter the first 3/4 starting number of your target without +1(e.g 513 or 5134) ")
                time.sleep(3)
                sys.exit()
        
        # for validate
        elif option == '2':
            print()
            print("MAKE SURE YOU ARE CONNECTED TO INTERNET")
            print()
            name = input("Enter name to save the validate numbers: ")
            name = "result/" + name
            print(yellow + "Now Select file to validate")
            time.sleep(1)
            number_list = get_file_path()  # Use the drag-and-drop function
            with open(number_list, 'r') as read:
                numbers = read.readlines()
                with ThreadPoolExecutor(max_workers=64) as executor:
                    executor.map(lambda number: numberValidator(number.strip(), name), numbers)
            input(f"{mag}Valid numbers saved to {green} {name}")
            run()
        
        
        # for generate and validate
        elif option == '3':
            print()
            print("MAKE SURE YOU ARE CONNECTED TO INTERNET")
            print()
            print(f'{yellow}Enter the first 3/4 starting number of your target without +1 (e.g 513 or 5134)')
            target = input(": ")
            
            if len(target) == 3 or len(target) == 4:
                output = input(yellow + "Enter name to save the generated number: ")
                if not output.endswith('.txt'):
                    output= output+".txt"
                valid = input(f'{yellow}Enter name to save the Validated number: ')
                valid = 'result/' + valid
                numberGenerator(output,target)
                print()
                print(f"{mag}Done generating and generated number saved to {green}{output}")
                time.sleep(1)
                print(f"{mag}Starting to Validate .....")
                time.sleep(2)
                
                with open(output, 'r') as read:
                    numbers = read.readlines()
                    with ThreadPoolExecutor(max_workers=64) as executor:
                        executor.map(lambda number: numberValidator(number.strip(), valid), numbers)
                input(f"{mag}Valid numbers saved to {green} {valid}")
                run()
                
                
            else: 
                print()
                print(f"I repeate, Enter {red}Enter the first 3/4 starting number of your target without +1(e.g 513 or 5134) ")
                time.sleep(3)
                sys.exit()
                
        elif option == '4':
            print("Thanks for you time")
            time.sleep(2)
            sys.exit()
        
        
        else:
            sys.exit()
            
    except ValueError as e:
        print(f"{red}You are only allow to Enter number:")
        time.sleep(3)
        sys.exit()
    
    except FileNotFoundError:
        print()
        print(f"{red} File not found... Dont forget to put .txt if it's a text file")
    except KeyboardInterrupt:
        print()
        print()
        print("Thanks for you time")
        time.sleep(2)
    except ImportError:
        print(red + 'Colorama or request not found installed on your system')
        print()
        print('Installing now ...')
        time.sleep(1)
        os.system(f"pip install requests")
        os.system(f"pip install colorama")
        print('Done installing, please run the program again, Thanks')
        time.sleep(1)
        sys.exit()
        
run()