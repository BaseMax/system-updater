import subprocess
import sys
import os

def check_update_linux(distro):
    try:
        if distro in ['ubuntu', 'debian', 'mint']:
            print("Updating system using apt...")
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            subprocess.run(['sudo', 'apt', 'upgrade', '-y'], check=True)
        elif distro in ['centos', 'fedora', 'redhat']:
            print("Updating system using dnf...")
            subprocess.run(['sudo', 'dnf', 'update', '-y'], check=True)
        elif distro in ['arch', 'manjaro']:
            print("Updating system using pacman...")
            subprocess.run(['sudo', 'pacman', '-Syu', '--noconfirm'], check=True)
        elif distro in ['opensuse']:
            print("Updating system using zypper...")
            subprocess.run(['sudo', 'zypper', 'update', '-y'], check=True)
        else:
            print(f"Unsupported Linux distribution: {distro}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating: {e}")
        sys.exit(1)

def check_update_macos():
    try:
        print("Updating system using softwareupdate...")
        subprocess.run(['sudo', 'softwareupdate', '--install', '--all'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating macOS: {e}")
        sys.exit(1)

def check_update_unix():
    print("Checking for updates... Unix-based system is not yet supported.")
    sys.exit(1)

def detect_os():
    if sys.platform == 'darwin':
        return 'macos'
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        try:
            with open('/etc/os-release') as f:
                os_info = f.read().lower()
                if 'ubuntu' in os_info or 'debian' in os_info:
                    return 'ubuntu'
                elif 'centos' in os_info or 'fedora' in os_info:
                    return 'centos'
                elif 'arch' in os_info:
                    return 'arch'
                elif 'opensuse' in os_info:
                    return 'opensuse'
                elif 'redhat' in os_info:
                    return 'redhat'
                else:
                    return 'unknown_linux'
        except FileNotFoundError:
            print("Could not determine Linux distribution.")
            sys.exit(1)
    else:
        return 'unknown'

def main():
    os_type = detect_os()
    
    if os_type == 'ubuntu' or os_type == 'debian' or os_type == 'mint' or os_type == 'centos' or os_type == 'fedora' or os_type == 'arch' or os_type == 'opensuse':
        check_update_linux(os_type)
    elif os_type == 'macos':
        check_update_macos()
    else:
        check_update_unix()

if __name__ == '__main__':
    main()
