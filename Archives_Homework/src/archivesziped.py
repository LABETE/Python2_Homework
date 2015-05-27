import zipfile
import os
import glob

def zippedfiles(zipfilename):
    path = os.getcwd()
    zip_file = os.path.join(path, os.path.basename(zipfilename)+".zip")
    files_to_zip = [os.path.basename(fn) for fn in glob.glob(zipfilename+"\*") if os.path.isfile(fn)]
    zf = zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED)
    file_to_zip = os.path.split(zipfilename)
    file_to_zip = file_to_zip[-1]
    for file in files_to_zip:
        zf.write(os.path.join(path,file),os.path.join(file_to_zip,file))
    list_ziped_files = zf.namelist()
    zf.close()
    sorted_ziped_files = []
    for file in list_ziped_files:
        sorted_ziped_files.append(file.replace("/","\\"))
    return sorted_ziped_files