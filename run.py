import os
current_dir = os.getcwd()
pdf_files = []
for file in os.listdir(current_dir):
    if file.endswith(".pdf"):
        pdf_files.append(file)
with open("README.md", "w") as f:
    for pdf_file in pdf_files:
        f.write('- ' + pdf_file + "\n")
f.close()
