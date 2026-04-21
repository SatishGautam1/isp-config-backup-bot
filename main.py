import datetime
import os
from netmiko import ConnectHandler

if not os.path.exists('backups'):
    os.makedirs('backups')

def run_backup(ip, device_tupe):
    device = {
        'device_type': device_tupe,
        'host': ip,
        'username': 'admin',
        'password': 'admin',
    }

    try:
        print(f"Connecting to {ip}...")
        with ConnectHandler(**device) as session:
            # Logic to switch commands based on device type
            command = "/export" if "mikrotik" in device_type else "show run"
            config = session.send_command(command)
            
            # Save file with timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"backups/{ip}_{timestamp}.txt"
            
            with open(filename, "w") as f:
                f.write(config)
            print(f"Done! Saved to {filename}")

    except Exception as e:
        print(f"Failed to backup {ip}: {e}")

if __name__ == "__main__":
    # Test with one IP first (Add this IP to your devices.txt)
    with open("devices.txt", "r") as f:
        for line in f:
            if line.strip():
                addr, dtype = line.strip().split(',')
                run_backup(addr, dtype)