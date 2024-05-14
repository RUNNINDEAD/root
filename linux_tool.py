#!/usr/bin/env python3

import subprocess

# Function to display menu
def display_menu():
    print("=== MENU ===")
    print("1. Update system")
    print("2. Upgrade packages")
    print("3. Add a new user")
    print("4. Add a new group")
    print("5. Delete a user")
    print("6. Delete a group")
    print("7. Check network interfaces")
    print("8. Change network interface")
    print("9. Install vsftpd")
    print("10. Configure vsftpd.conf")
    print("11. Enable vsftpd")
    print("12. Reload vsftpd")
    print("13. Install SSH")
    print("14. Configure SSH")
    print("15. Enable SSH")
    print("16. Reload SSH")
    print("17. Exit")

# Function to update system
def update_system():
    subprocess.run(['sudo', 'apt', 'update'])

# Function to upgrade packages
def upgrade_packages():
    subprocess.run(['sudo', 'apt', 'upgrade'])

# Function to add a new user
def add_new_user():
    username = input("Enter username for the new user: ")
    password = input("Enter password for the new user: ")
    full_name = input("Enter full name for the new user: ")
    
    try:
        subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', '-c', full_name, username])
        subprocess.run(['echo', f'{username}:{password}', '|', 'sudo', 'chpasswd'])
        print(f"User '{username}' added successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to add user '{username}'.")

# Function to add a new group
def add_new_group():
    groupname = input("Enter group name: ")
    try:
        subprocess.run(['sudo', 'groupadd', groupname])
        print(f"Group '{groupname}' added successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to add group '{groupname}'.")

# Function to delete a user
def delete_user():
    username = input("Enter username to delete: ")
    try:
        subprocess.run(['sudo', 'userdel', '-r', username])
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user '{username}'.")

# Function to delete a group
def delete_group():
    groupname = input("Enter group name to delete: ")
    try:
        subprocess.run(['sudo', 'groupdel', groupname])
        print(f"Group '{groupname}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete group '{groupname}'.")

# Function to check network interfaces
def check_network_interfaces():
    subprocess.run(['ifconfig'])

# Function to change network interface
def change_network_interface():
    subprocess.run(['sudo', 'nmtui'])

# Function to install vsftpd
def install_vsftpd():
    subprocess.run(['sudo', 'apt', 'install', 'vsftpd'])

# Function to configure vsftpd.conf
def configure_vsftpd():
    subprocess.run(['sudo', 'nano', '/etc/vsftpd.conf'])

# Function to enable vsftpd
def enable_vsftpd():
    subprocess.run(['sudo', 'systemctl', 'enable', 'vsftpd'])
    subprocess.run(['sudo', 'systemctl', 'start', 'vsftpd'])
    print("vsftpd enabled and started successfully.")

# Function to reload vsftpd
def reload_vsftpd():
    subprocess.run(['sudo', 'systemctl', 'reload', 'vsftpd'])

# Function to install SSH
def install_ssh():
    subprocess.run(['sudo', 'apt', 'install', 'openssh-server'])

# Function to configure SSH
def configure_ssh():
    subprocess.run(['sudo', 'nano', '/etc/ssh/sshd_config'])

# Function to enable SSH
def enable_ssh():
    subprocess.run(['sudo', 'systemctl', 'enable', 'ssh'])
    subprocess.run(['sudo', 'systemctl', 'start', 'ssh'])
    print("SSH enabled and started successfully.")

# Function to reload SSH
def reload_ssh():
    subprocess.run(['sudo', 'systemctl', 'reload', 'ssh'])

# Main script
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        update_system()
    elif choice == '2':
        upgrade_packages()
    elif choice == '3':
        add_new_user()
    elif choice == '4':
        add_new_group()
    elif choice == '5':
        delete_user()
    elif choice == '6':
        delete_group()
    elif choice == '7':
        check_network_interfaces()
    elif choice == '8':
        change_network_interface()
    elif choice == '9':
        install_vsftpd()
    elif choice == '10':
        configure_vsftpd()
    elif choice == '11':
        enable_vsftpd()
    elif choice == '12':
        reload_vsftpd()
    elif choice == '13':
        install_ssh()
    elif choice == '14':
        configure_ssh()
    elif choice == '15':
        enable_ssh()
    elif choice == '16':
        reload_ssh()
    elif choice == '17':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Thank you - Script by RUNNINDEAD on github")
