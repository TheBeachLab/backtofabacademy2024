import os
import subprocess
import sys

# Step 0. Translation if first parameter is '--translate'
if len(sys.argv) > 1:
    if sys.argv[1] == '--translate':
        subprocess.run(['git', 'add', '--all'])  # Modified files need to be added, otherwise, they are not translated
        subprocess.run(['python3', 'translate-en.py'])
        subprocess.run(['python3', 'translate-de.py'])

# Step 1. Concatenate chapters

# Step 1. README.md --> index.html in the current folder
subprocess.run(['pandoc', '-s', '-c', 'base.css', 'README.md', '-t', 'html', '-o', 'index.html', '--lua-filter=links-to-html.lua'], stderr=subprocess.DEVNULL)

# Step 2. /md/*.md --> /html/*.html in the documentation folders
documentation_folders = ['documentation/es/md', 'documentation/en/md', 'documentation/de/md']
for folder in documentation_folders:
    html_folder = os.path.join(os.path.dirname(folder), 'html')
    folder_files = [f for f in os.listdir(folder) if f.endswith('.md')]
    for f in folder_files:
        input_file = os.path.join(folder, f)
        output_file = os.path.join(html_folder, f"{os.path.splitext(f)[0]}.html")
        print(f"Converting {input_file} to {output_file}")
        subprocess.run(['pandoc', '-s', '-c', '../../../base.css', input_file, '-t', 'html', '-o', output_file, '--lua-filter=links-to-html.lua'], stderr=subprocess.DEVNULL)

# Step 3. Upload everything to GitHub
# If there is a commit message (excluding -translate), then upload
if len([arg for arg in sys.argv[1:] if arg != '--translate']) > 0:
    subprocess.run(['git', 'add', '--all']) 
    commit_message = ' '.join(arg for arg in sys.argv[1:] if arg != '--translate')
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'pull'])
    subprocess.run(['git', 'push'])
else:
    print("Not uploading (Empty commit message)")
