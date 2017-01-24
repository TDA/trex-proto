import zipfile
import os

def unzip_file(path_to_zip_file, directory_to_extract_to):
    if zipfile.is_zipfile(path_to_zip_file):
        zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
        zip_ref.extractall(directory_to_extract_to)
        zip_ref.close()
        print "Unzipped the file ", path_to_zip_file, " to ", directory_to_extract_to
    else:
        print "Invalid zip file"

# Might need refactoring on this one, as its way too long
# lets try moving out the configs first
def zip_files(files_list):
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED

    print "Compression type", compression
    modes = {
        zipfile.ZIP_DEFLATED: 'deflated',
        zipfile.ZIP_STORED: 'stored',
    }
    print "Mode", modes[compression]

    compressed_folder = 'compressed_folder.zip'

    print "Creating archive"
    zip_ref = zipfile.ZipFile(compressed_folder, mode='w')
    for file in files_list:
        if not file.startswith('.'):
            try:
                print "adding file", file, "with compression mode", modes[compression]
                zip_ref.write(file, compress_type=compression)
            except Exception as ex:
                print ex
                print "Unable to compress the file", file
                continue
    print 'Closing zipper'
    zip_ref.close()


if __name__ == '__main__':
    # test driver program for unzipper
    destination_path = '/Users/schandramouli/Downloads/images-runzipped'
    zip_file_path = '/Users/schandramouli/Downloads/images-text.zip'
    unzip_file(zip_file_path, destination_path)
    dest_dir = os.path.join(destination_path, "images-text")
    files_list = os.listdir(dest_dir)
    print files_list
    os.chdir(dest_dir)
    zip_files(files_list)

