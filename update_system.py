import subprocess
import sys
import os

def update_linux(distro):
    update_commands = {
        'ubuntu': ['sudo', 'apt', 'update'],
        'debian': ['sudo', 'apt', 'update'],
        'mint': ['sudo', 'apt', 'update'],
        'centos': ['sudo', 'dnf', 'update', '-y'],
        'fedora': ['sudo', 'dnf', 'update', '-y'],
        'redhat': ['sudo', 'dnf', 'update', '-y'],
        'arch': ['sudo', 'pacman', '-Syu', '--noconfirm'],
        'manjaro': ['sudo', 'pacman', '-Syu', '--noconfirm'],
        'opensuse': ['sudo', 'zypper', 'update', '-y']
    }
    
    try:
        if distro in update_commands:
            print(f"Updating system using {update_commands[distro][1]}...")
            subprocess.run(update_commands[distro], check=True)
        else:
            raise ValueError(f"Unsupported Linux distribution: {distro}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating: {e}")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

def update_macos():
    try:
        print("Updating system using softwareupdate...")
        subprocess.run(['sudo', 'softwareupdate', '--install', '--all'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating macOS: {e}")
        sys.exit(1)

def update_unix():
    print("Unix-based system updates are not yet supported.")
    sys.exit(1)

def detect_os():
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
    os_type = detect_os()
    
    if os_type in ['ubuntu', 'debian', 'mint', 'centos', 'fedora', 'redhat', 'arch', 'manjaro', 'opensuse']:
        update_linux(os_type)
    elif os_type == 'macos':
        update_macos()
    else:
        update_unix()

if __name__ == '__main__':
    main()
