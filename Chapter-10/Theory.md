**1.)**
shutil.copy() only copies one file to another location.

shutil.copytree() copues n entire folder and the subfolders and files inside it.

---
**2.)**
shutil.move('path/filename', 'path/newfilename') renames the file when path supplied is same but filename is changed.

---
**3.)**
Delete function is shutil module deletes the file permanently whereas in send2trash module, file is sent to the trash/bin, so that it can be recovered later if needed.

---
**4.)**
zipfile.ZipFile() method in zipfile module is equivalent of file object's open() method.