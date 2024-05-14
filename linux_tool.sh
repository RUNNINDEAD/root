#!/bin/bash

# Function to display menu
display_menu() {
    echo "=== MENU ==="
    echo "1. Update system"
    echo "2. Upgrade packages"
    echo "3. Add a new user"
    echo "4. Add a new group"
    echo "5. Delete a user"
    echo "6. Delete a group"
    echo "7. Check network interfaces"
    echo "8. Change network interface"
    echo "9. Install vsftpd"
    echo "10. Configure vsftpd.conf"
    echo "11. Enable vsftpd"
    echo "12. Reload vsftpd"
    echo "13. Install SSH"
    echo "14. Configure SSH"
    echo "15. Enable SSH"
    echo "16. Reload SSH"
    echo "17. Exit"
}

# Function to update system
update_system() {
    sudo apt update
}

# Function to upgrade packages
upgrade_packages() {
    sudo apt upgrade
}

# Function to add a new user
add_new_user() {
    read -p "Enter username for the new user: " username
    read -sp "Enter password for the new user: " password
    echo
    read -p "Enter full name for the new user: " full_name
    
    # Check if the user already exists
    if id "$username" &>/dev/null; then
        echo "User '$username' already exists."
    else
        # Create the user with specified password and full name
        sudo useradd -m -s /bin/bash -c "$full_name" "$username"
        echo "$username:$password" | sudo chpasswd
        echo "User '$username' added successfully."
    fi
}

# Function to add a new group
add_new_group() {
    read -p "Enter group name: " groupname
    
    # Check if the group already exists
    if grep -q "^$groupname:" /etc/group; then
        echo "Group '$groupname' already exists."
    else
        sudo groupadd "$groupname"
        echo "Group '$groupname' added successfully."
    fi
}

# Function to delete a user
delete_user() {
    read -p "Enter username to delete: " username
    if id "$username" &>/dev/null; then
        sudo userdel -r "$username"
        echo "User '$username' deleted successfully."
    else
        echo "User '$username' does not exist."
    fi
}

# Function to delete a group
delete_group() {
    read -p "Enter group name to delete: " groupname
    if grep -q "^$groupname:" /etc/group; then
        sudo groupdel "$groupname"
        echo "Group '$groupname' deleted successfully."
    else
        echo "Group '$groupname' does not exist."
    fi
}

# Function to check network interfaces
check_network_interfaces() {
    ifconfig
}

# Function to change network interface using nmtui
change_network_interface() {
    sudo nmtui
}

# Function to install vsftpd
install_vsftpd() {
    sudo apt install vsftpd
}

# Function to configure vsftpd.conf
configure_vsftpd() {
    sudo nano /etc/vsftpd.conf
}

# Function to enable vsftpd
enable_vsftpd() {
    sudo systemctl enable vsftpd
    sudo systemctl start vsftpd
    echo "vsftpd enabled and started successfully."
}

# Function to reload vsftpd
reload_vsftpd() {
    sudo systemctl reload vsftpd
}

# Function to install SSH
install_ssh() {
    sudo apt install openssh-server
}

# Function to configure SSH
configure_ssh() {
    sudo nano /etc/ssh/sshd_config
}

# Function to enable SSH
enable_ssh() {
    sudo systemctl enable ssh
    sudo systemctl start ssh
    echo "SSH enabled and started successfully."
}

# Function to reload SSH
reload_ssh() {
    sudo systemctl reload ssh
}

# Main script
while true; do
    display_menu
    read -p "Enter your choice: " choice

    case $choice in
        1) update_system ;;
        2) upgrade_packages ;;
        3) add_new_user ;;
        4) add_new_group ;;
        5) delete_user ;;
        6) delete_group ;;
        7) check_network_interfaces ;;
        8) change_network_interface ;;
        9) install_vsftpd ;;
        10) configure_vsftpd ;;
        11) enable_vsftpd ;;
        12) reload_vsftpd ;;
        13) install_ssh ;;
        14) configure_ssh ;;
        15) enable_ssh ;;
        16) reload_ssh ;;
        17) echo "Exiting..."; break ;;
        *) echo "Invalid choice. Please enter a valid option." ;;
    esac
done

echo "Thank you - Script by RUNNINDEAD on github"
