import subprocess
import requests


def check_internet_connection():
    try:
        # Attempt to make a connection to Google's DNS server
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

if __name__ == "__main__":
    wifi_name = input("Enter your WiFi name (SSID): ")
    wifi_password = input("Enter your WiFi password: ")

    if connect_wifi(wifi_name, wifi_password):
        if check_internet_connection():
            print("Connected to WiFi successfully!")
            print(f"Password is {wifi_password}")
        else:
            print("Failed to connect to WiFi.")
