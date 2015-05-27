import os
import zipfile
import glob

def newarchivedirectory(zip_file):
    
    zf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    files_stored = [fn for fn in glob.glob("*") if os.path.isfile(fn)]
    parcial_path = os.path.split(os.path.dirname(zip_file))
    for file_to_zip in files_stored[1:]:
        zf.write(zip_file,os.path.join(parcial_path[-1],file_to_zip))
    list_files_ziped = zf.namelist()
    file_to_zip_formated =[]
    for file in list_files_ziped:
        file_to_zip_formated.append(file.replace("/","\\"))
    zf.close()
    
    return file_to_zip_formated