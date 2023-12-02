import os
import shutil
import re
#1
# file = open("file1.txt").read()
# for i in file:


#2
# def path(folder):
#     total_files = 0
#     total_dirs = 0
#     for root, dirs, files in os.walk(folder):
#         total_files += len(files)
#         total_dirs += len(dirs)
#     print(f"Количество файлов: {total_files}")
#     print(f"Количество подпапок: {total_dirs}")
# path("C:\python\lesson11")
#3
# def delete(file):
#     shutil.rmtree(file)
# delete("C:\python\lesson11\Новая папка (2)")

#3
# url = 'http://test.com/dir1/dir2/dir3/page.html'
# domain = re.findall(r"[\w\]+\.[\w\]+", url)
# print(domain)

#5
txt = 'abcde abcde'
delete = 'abe'
for i in txt:
    if i in set(delete):
        txt = txt.replace(i, "")
        print(txt)
print(txt)