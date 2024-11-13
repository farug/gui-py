import lib

def get_repo_info(username, password):
    remote_host = '10.10.10.10'
    remote_path = '/home/user/repo'
    local_folder = './repo'
    lib.scp_download_file(remote_host, remote_path, local_folder, username, password)

def get_logs(remote_host, username, password, remote_path):
    local_folder = './logs'
    lib.scp_download_file(remote_host, remote_path, local_folder, username, password)

def get_file(remote_host, username, password):
    remote_path = '/home/user/file.txt'
    local_folder = './file.txt'
    lib.scp_download_file(remote_host, remote_path, local_folder, username, password)

def send_file(remote_host, username, password):
    remote_path = '/home/user/file.txt'
    local_folder = './file.txt'
    lib.scp_upload_file(remote_host, remote_path, local_folder, username, password)
