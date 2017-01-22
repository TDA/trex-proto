import zipfile

def unzip_file(path_to_zip_file, directory_to_extract_to):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

if __name__ == '__main__':
    destination_path = '/Users/swapns/Downloads/test-folder'
    zip_file_path = '/Users/swapns/Downloads/jce_policy-8.zip'
    unzip_file(zip_file_path, destination_path)
    print "Unzipped the file ", zip_file_path, " to ", destination_path
