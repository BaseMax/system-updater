# System Updater

This project provides a cross-platform script to check for system updates and update the system for various operating systems. It supports Windows, macOS, and Linux distributions such as Ubuntu, Debian, Fedora, CentOS, and more. The script also includes backup functionality for critical system files before updating.

## Features

- Displays system information such as disk usage and memory status.
- Checks for available updates for various Linux distributions.
- Supports system updates for Windows, macOS, and Linux.
- Backs up critical system files before performing updates.
- Compatible with major Linux distributions, including Ubuntu, Debian, Mint, Fedora, CentOS, and more.
- User-friendly interface for easy interaction.

## Installation

### Requirements

- Python 3.x
- Required tools for your OS (e.g., `apt`, `dnf`, `pacman`, etc. for Linux distributions, `systeminfo` for Windows, `softwareupdate` for macOS)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/BaseMax/system-updater.git
    cd system-updater
    ```

2. Install the necessary dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Script

To run the script, execute the following command:

```bash
python update_system.py
```

The script will automatically detect your operating system and proceed with checking for updates. You will be asked if you want to proceed with the update.

## What the Script Does
- Displays system information: The script will show relevant information based on your operating system.
- Backs up critical files: The script will back up important system configuration files before attempting updates.
- Checks for updates: The script will check for any available updates depending on your system's operating system and distribution.
- Performs updates: If you agree to proceed, the script will initiate the update process for your system.

### Supported Operating Systems

- **Windows: Uses ms-settings:windowsupdate to check for and initiate updates.
- **macOS: Uses softwareupdate to install available updates.
- **Linux: Supports major Linux distributions, including:
  - Ubuntu
  - Debian
  - Fedora
  - CentOS
  - Arch Linux
  - Manjaro
  - openSUSE
  - And others

### Example Output

```bash
System Information:
-------------------
OS: Windows 10
CPU: Intel Core i7
RAM: 16 GB
Disk: 500 GB

Do you want to proceed with updating the system? (y/n): y
Backed up /etc/fstab to /tmp/system_backup
Backed up /etc/hostname to /tmp/system_backup
Backed up /etc/hosts to /tmp/system_backup
Backed up /etc/passwd to /tmp/system_backup
Checking for updates using apt...
Updating system using apt...
...
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Copyright

© 2025 Max Base
