import zipfile
from zipfile_infolist import print_info
import os

def unzip_file(path_to_zip_file, directory_to_extract_to):
    if zipfile.is_zipfile(path_to_zip_file):
        zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
        zip_ref.extractall(directory_to_extract_to)
        zip_ref.close()
        print "Unzipped the file ", path_to_zip_file, " to ", directory_to_extract_to
    else:
        print "Invalid zip file"

def zip_files(files_list):
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED

    modes = {
        zipfile.ZIP_DEFLATED: 'deflated',
        zipfile.ZIP_STORED: 'stored',
    }

    compressed_folder = 'compressed_folder.zip'

    print "Creating archive"
    zip_ref = zipfile.ZipFile(compressed_folder, mode='w')
    for file in files_list:
        try:
            print "adding file with compression mode", modes[compression]
            zip_ref.write(file, compress_type=compression)
        except:
            print "Unable to compress the file", file
            continue

    print 'Closing zipper'
    zip_ref.close()
    print_info(compressed_folder)

if __name__ == '__main__':
    # test driver program for unzipper
    destination_path = '/Users/schandramouli/Downloads/images-runzipped'
    zip_file_path = '/Users/schandramouli/Downloads/images-re.zip'
    unzip_file(zip_file_path, destination_path)
    files_list = os.listdir(destination_path)

