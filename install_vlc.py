import requests
import hashlib
import os

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()
    print(f'Step 1: Expected SHA-256 hash value = {expected_sha256}.')

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()
    print(f'Step 2: The VLC installer file donwloaded successfully!')

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):
        print(f'Step 3: Verified the integrity of the downloaded VLC installer = {expected_sha256}.')

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)
        print(f'Step 4: VLC installer successfully saved to {installer_path}')

def get_expected_sha256():
    """Downloads the text file containing the expected SHA-256 value for the VLC installer file from the 
    videolan.org website and extracts the expected SHA-256 value from it.

    Returns:
        str: Expected SHA-256 hash value of VLC installer
    """
    # Send GET message to download the file
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract text file content from response message
        file_content = resp_msg.text.split()[0]
        return file_content

def download_installer():
    """Downloads, but does not save, the .exe VLC installer file for 64-bit Windows.

    Returns:
        bytes: VLC installer file binary data
    """
    # Send GET message to download the file
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract binary file content from response message
        file_content = resp_msg.content
        return file_content

def installer_ok(installer_data, expected_sha256):
    """Verifies the integrity of the downloaded VLC installer file by calculating its SHA-256 hash value 
    and comparing it against the expected SHA-256 hash value. 

    Args:
        installer_data (bytes): VLC installer file binary data
        expected_sha256 (str): Expeced SHA-256 of the VLC installer

    Returns:
        bool: True if SHA-256 of VLC installer matches expected SHA-256. False if not.
    """    
    # Send GET message to download the file
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract binary file content from response message body
        installer_data = resp_msg.content
        # Calculate SHA-256 hash value
        expected_sha256 = hashlib.sha256(installer_data).hexdigest()
        return expected_sha256
    
def save_installer(installer_data):
    """Saves the VLC installer to a local directory.

    Args:
        installer_data (bytes): VLC installer file binary data

    Returns:
        str: Full path of the saved VLC installer file
    """
    # Send GET message to download the file
    file_url = 'https://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
        # Extract binary file content from response message
        installer_data = resp_msg.content
        # Save the binary file to disk
        installer_path = os.path.join(os.getenv('TEMP'), 'vlc-3.0.17.4-win64.exe')
        with open(installer_path, 'wb') as file:
            file.write(installer_data)
        return installer_path

if __name__ == '__main__':
    main()