import paramiko
from scp import SCPClient
import os

def scp_download_file(remote_host, remote_path, local_folder, username, password, local_filename=None):
    # Ensure the local folder exists
    os.makedirs(local_folder, exist_ok=True)
    
    # Determine the local file path
    if local_filename is None:
        local_filename = os.path.basename(remote_path)
    local_file_path = os.path.join(local_folder, local_filename)
    
    # Set up the SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the remote host
        ssh.connect(remote_host, username=username, password=password)
        
        # Use SCP to download the file
        with SCPClient(ssh.get_transport()) as scp:
            scp.get(remote_path, local_file_path)
        
        print(f"File downloaded to {local_file_path}")
    finally:
        ssh.close()

# Example usage
# scp_download_file('remote_host', '/remote/path/to/file.txt', '/path/to/local/folder', 'username', 'password')

def get_remote_file_list(remote_host, remote_path, username, password):
    """Fetches a list of files from the remote path that match the date pattern."""
    # Set up the SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the remote host
        ssh.connect(remote_host, username=username, password=password)
        
        # Execute the command to list files in the remote directory
        stdin, stdout, stderr = ssh.exec_command(f'ls {remote_path}')
        file_list = stdout.read().decode().splitlines()
        
        # Filter files that end with a date pattern
        date_filtered_files = [f for f in file_list if f.endswith(('.log', '.txt')) and any(char.isdigit() for char in f[-6:])]
        
        return date_filtered_files
    finally:
        ssh.close()

def extract_date_from_filename(filename):
    """Extracts date and time information from the filename."""
    # Assuming the date is in the format 'ddmmyy_hh_mm' or 'ddmmyyhhmm'
    parts = filename.split('_')
    if len(parts) > 1:
        date_raw_part = parts[-3]  # Get the date part before the last underscore
        date_part = date_raw_part[-6:]
        time_min_part = parts[-1].split('.')[0]  # Get the time part before the file extension
        time_hour_part = parts[-2]
        time_part = time_hour_part + time_min_part
        
        # Return the date and time as separate values
        return date_part, time_part
    else:
        # Handle the case where date and time are concatenated
        date_part = filename[-12:-4]  # Extract the last 12 characters for date and time
        time_part = filename[-4:-4+4]  # Extract the last 4 characters for time
        return date_part, time_part
    return None, None
