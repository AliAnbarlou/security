import subprocess

def get_nearby_modems():
    command_output = subprocess.check_output(['netsh', 'mbn', 'show', 'interfaces'], shell=True).decode('utf-8')
    
    modems = []
    
    if command_output:
        for line in command_output.splitlines():
            if 'Name' in line:
                modem_name = line.split(':')[-1].strip()
                modems.append(modem_name)
    
    return modems

nearby_modems = get_nearby_modems()

print("مودم‌های اطراف:")
for modem in nearby_modems:
    print(modem)

# در صورت نیاز می‌توانید مودم‌ها را در یک لیست نیز قرار دهید
# مثلا:
# list_of_modems = nearby_modems
