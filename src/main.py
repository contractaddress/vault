import pydoc
import os
import subprocess
import json
from time import sleep
from getpass import getpass
from vault import create_vault, load_vault, save_vault, VAULTFILE
from commands import delete_entry, add_entry


def logo():
    print("""
 ██▒   █▓ ▄▄▄       █    ██  ██▓  ▄▄▄█████▓
▓██░   █▒▒████▄     ██  ▓██▒▓██▒  ▓  ██▒ ▓▒
 ▓██  █▒░▒██  ▀█▄  ▓██  ▒██░▒██░  ▒ ▓██░ ▒░
  ▒██ █░░░██▄▄▄▄██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ 
   ▒▀█░   ▓█   ▓██▒▒▒█████▓ ░██████▒▒██▒ ░ 
   ░ ▐░   ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   
   ░ ░░    ▒   ▒▒ ░░░▒░ ░ ░ ░ ░ ▒  ░  ░    
     ░░    ░   ▒    ░░░ ░ ░   ░ ░   ░      
      ░        ░  ░   ░         ░  ░       
     ░                                     
    """)

logo()


def clear_screen():
    if os.name == 'nt': #checks if OS is windows or unix based
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])


#---- MAIN ----#
def main():
    if not os.path.exists(VAULTFILE):
        print("no vault file exists, creating one !")
        master_password = getpass("Create master password: ")
        vault_data, salt = create_vault(master_password)
    else:
        master_password = getpass("Enter your password: ")
        try:
            vault_data, salt = load_vault(master_password)
        except Exception:
            print("Invalid password or the vault is corrupted")
            return

    while True:
        clear_screen()
        logo()
        print('\n--- Vault Menu ---')
        print('(1) View entries')
        print('(2) Add entry')
        print('(3) Delete entry')
        print('(4) Save & Exit')
        choice = input('> ')

        if choice == '1':
            pydoc.pager(json.dumps(vault_data, indent=4))

        elif choice == '2':
            vault_data = add_entry(vault_data)

        elif choice == '3':
            vault_data = delete_entry(vault_data)

        elif choice == '4':
            save_vault(vault_data, master_password, salt)
            print('Bye!')
            break

        else:
            print('command not found')
            sleep(1)

main()
