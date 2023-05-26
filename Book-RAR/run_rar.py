import os
current_dir = os.getcwd()
pdf_files = []
for file in os.listdir(current_dir):
    if file.endswith(".rar"):
        pdf_files.append(file)
with open("README.md", "w") as f:
    for rar_file in pdf_files:
        f.write('- [' + rar_file + "](https://github.com/smiler666/Book-PDF-PHEI/blob/main/Book-RAR/" + rar_file + ")\n")
f.close()
