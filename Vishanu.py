# Logo
logo = """
\033[1;37m⌌\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;34m━━━━\033[1;35m━━\033[1;37m⌍
\033[1;38m▏ __  __     ______      ____        __  __      __  __     ▏ 
\033[1;39m▏/\ \/\ \   /\__  _\    /\  _`\     /\ \/\ \    /\ \/\ \    ▏   
\033[1;35m▏ \ \ \ \ \  \/_/\ \/    \ \,\L\_\   \ \ \_\ \   \ \ \ \ \  ▏  
\033[1;32m▏\ \ \ \ \    \ \ \     \/_\__ \    \ \  _  \   \ \ \ \ \   ▏
\033[1;31m▏ \ \ \_/ \    \_\ \__    /\ \L\ \   \ \ \ \ \   \ \ \_\ \  ▏
\033[1;33m▏ \ `\___/    /\_____\   \ `\____\   \ \_\ \_\   \ \_____\  ▏
\033[1;30m▏   `\/__/     \/_____/    \/_____/    \/_/\/_/    \/_____/ ▏
\033[1;37m⌎\033[1;31m━━━━\033[1;32m━━━━\033[1;33m━━━━\033[1;34m━━━━\033[1;35m━━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;30m━━━━\033[1;31m━━━\033[1;32m━━━━\033[1;33m━━━━━\033[1;34m━━━━\033[1;35m━━\033[1;37m⌏                                              
                                             
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[37m[*] 𝐎𝐖𝐍𝐄𝐑      : \033[36m𝗩𝗜𝗦𝗛𝗔𝗡𝗨 
\033[37m[*] 𝐆𝐈𝐓𝐇𝐔𝐁     : \033[33m𝗩𝗜𝗦𝗛𝗔𝗡𝗨 𝗫𝗗
\033[37m[*] 𝐒𝐓𝐀𝐓𝐔𝐒     : \033[32m𝐏𝐀𝐈𝐃 𝐓𝐎𝐎𝐋
\033[37m[*] 𝐓𝐄𝐀𝐌       : \033[35m𝐊𝐈𝐋𝐋𝐄𝐑 𝐑𝐔𝐋𝐄𝐗 𝐓𝐄𝐀𝐌
\033[37m[*] 𝐓𝐎𝐎𝐋       : \033[34m𝐌𝐔𝐋𝐓𝐈 𝐓𝐎𝐊𝐄𝐍 𝐂𝐎𝐍𝐕𝐎 𝐓𝐎𝐎𝐋
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(logo)

import os
import random
import time
import requests

# Facebook Graph API endpoint
thread_id = input("\033[1;32mEnter thread ID: ")

url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file paths
token_file_paths = input("\033[33mEnter token file paths (separated by comma): ").split(',')

# Message file path
message_file_path = input("\033[34mEnter message file path: ")

# Haters name
haters_name = input("\033[35mEnter haters name: ")

# Delay between messages
delay_between_messages = int(input("\033[36mEnter delay between messages: "))

# Read tokens from files
access_tokens = []
token_names = []
for token_file_path in token_file_paths:
    with open(token_file_path.strip(), "r") as token_file:
        for i, token in enumerate(token_file.readlines()):
            access_tokens.append(token.strip())
            token_names.append(f"Token {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(token):
    try:
        response = requests.get(f'https://graph.facebook.com/v15.0/me?access_token={token}')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(token, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[34m 
✪✭═══════•『 V1SH4NU R4J D0N 0N F1R3』•═══════✭✪
""")
            account_name = get_account_name(token)           
            print(f"\033[38;5;25m[+] APKA MESSAGE VISHANU KI TARAF SE SEND KIYA GYA HAI => Thread ID: {thread_id} => Token: {token_names[access_tokens.index(token)]} => Account Name: {account_name} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
        else:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[31;5;196m 
✪✭═══════•『 V1SH4NU R4J D0N 0N FIR3』•═══════✭✪
""")
            print(f"\033[38;5;1Q96mM3SS4G3 F9IL3D H0 GYA HAI => Thread ID: {thread_id} =>Token: {token_names[access_tokens.index(token)]} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_token = random.choice(access_tokens)
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()
