import zipfile

def unzip_file(path_to_zip_file, directory_to_extract_to):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
    print "Unzipped the file ", path_to_zip_file, " to ", directory_to_extract_to

if __name__ == '__main__':
    # test driver program for unzipper
    destination_path = '/Users/swapns/Downloads/test-folder'
    zip_file_path = '/Users/swapns/Downloads/jce_policy-8.zip'
    unzip_file(zip_file_path, destination_path)

