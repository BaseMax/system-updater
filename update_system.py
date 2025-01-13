import subprocess
import sys
import os
import shutil

def display_system_info():
    """Display basic system information like disk usage and memory usage."""
    print("\nSystem Information:")
    print("-------------------")
    try:
        subprocess.run(['df', '-h'], check=True)
        subprocess.run(['free', '-h'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while fetching system info: {e}")

def check_updates_linux(distro):
    """Check for available updates on Linux based on the distribution."""
    check_commands = {
        'ubuntu': ['sudo', 'apt', 'list', '--upgradable'],
        'debian': ['sudo', 'apt', 'list', '--upgradable'],
        'mint': ['sudo', 'apt', 'list', '--upgradable'],
        'centos': ['sudo', 'dnf', 'check-update'],
        'fedora': ['sudo', 'dnf', 'check-update'],
        'redhat': ['sudo', 'dnf', 'check-update'],
        'arch': ['sudo', 'pacman', '-Qu'],
        'manjaro': ['sudo', 'pacman', '-Qu'],
        'opensuse': ['sudo', 'zypper', 'list-updates']
    }
    
    try:
        if distro in check_commands:
            print(f"Checking for updates using {check_commands[distro][1]}...")
            subprocess.run(check_commands[distro], check=True)
        else:
            print(f"Cannot check for updates: Unsupported distribution {distro}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while checking updates: {e}")
        sys.exit(1)

def backup_system_files():
    """Backup critical system files before performing updates."""
    backup_dir = '/tmp/system_backup'
    os.makedirs(backup_dir, exist_ok=True)
    critical_files = ['/etc/fstab', '/etc/hostname', '/etc/hosts', '/etc/passwd']
    
    try:
        for file in critical_files:
            if os.path.exists(file):
                shutil.copy(file, os.path.join(backup_dir, os.path.basename(file)))
                print(f"Backed up {file} to {backup_dir}")
            else:
                print(f"File {file} does not exist, skipping backup.")
    except Exception as e:
        print(f"Error occurred while backing up files: {e}")
        sys.exit(1)

def update_linux(distro):
    """Update Linux system based on the distribution."""
    update_commands = {
        'ubuntu': ['sudo', 'apt', 'update', '&&', 'sudo', 'apt', 'upgrade', '-y'],
        'debian': ['sudo', 'apt', 'update', '&&', 'sudo', 'apt', 'upgrade', '-y'],
        'mint': ['sudo', 'apt', 'update', '&&', 'sudo', 'apt', 'upgrade', '-y'],
        'centos': ['sudo', 'dnf', 'update', '-y'],
        'fedora': ['sudo', 'dnf', 'update', '-y'],
        'redhat': ['sudo', 'dnf', 'update', '-y'],
        'arch': ['sudo', 'pacman', '-Syu', '--noconfirm'],
        'manjaro': ['sudo', 'pacman', '-Syu', '--noconfirm'],
        'opensuse': ['sudo', 'zypper', 'update', '-y'],
        'yum': ['sudo', 'yum', 'update', '-y']
    }
    
    try:
        if distro in update_commands:
            print(f"Updating system using {update_commands[distro][1]}...")
            subprocess.run(update_commands[distro], shell=True, check=True)
        else:
            raise ValueError(f"Unsupported Linux distribution: {distro}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating: {e}")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

def update_macos():
    """Update macOS using the built-in softwareupdate tool."""
    try:
        print("Updating system using softwareupdate...")
        subprocess.run(['sudo', 'softwareupdate', '--install', '--all'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating macOS: {e}")
        sys.exit(1)

def update_unix():
    """Handle updates for other Unix-based systems."""
    print("Unix-based system updates are not yet supported.")
    sys.exit(1)

def detect_os():
    """Detect the operating system and return the distribution name."""
    if sys.platform == 'darwin':
        return 'macos'
    elif sys.platform in ['linux', 'linux2']:
        try:
            with open('/etc/os-release') as f:
                os_info = f.read().lower()
                for distro in ['ubuntu', 'debian', 'mint', 'centos', 'fedora', 'redhat', 'arch', 'manjaro', 'opensuse']:
                    if distro in os_info:
                        return distro
                return 'unknown_linux'
        except FileNotFoundError:
            print("Could not determine Linux distribution.")
            sys.exit(1)
    else:
        return 'unknown'

def main():
    """Main function to manage the update process."""
    os_type = detect_os()

    display_system_info()

    proceed = input("Do you want to proceed with updating the system? (y/n): ")
    if proceed.lower() != 'y':
        print("Update canceled.")
        sys.exit(0)
    
    backup_system_files()

    if os_type in ['ubuntu', 'debian', 'mint', 'centos', 'fedora', 'redhat', 'arch', 'manjaro', 'opensuse']:
        check_updates_linux(os_type)
        update_linux(os_type)
    elif os_type == 'macos':
        update_macos()
    else:
        update_unix()

if __name__ == '__main__':
    main()
