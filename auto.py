import os
import subprocess
import sys

# Step 0. Translation if first parameter is '--translate'
if len(sys.argv) > 0 and sys.argv[1] == '--translate':
    subprocess.run(['git', 'add', '--all']) # modified files need to be added, otherwise are not translated
    subprocess.run(['python3', 'translate-en.py'])
    subprocess.run(['python3', 'translate-de.py'])

# Step 1. File conversion from README.md to index.html in the current folder
subprocess.run(['pandoc', '-s', '-c', 'documentation/base.css', 'README.md', '-t', 'html', '-o', 'index.html', '--lua-filter=links-to-html.lua'], stderr=subprocess.DEVNULL)

# Step 2. File conversion from .md to .html in the documentation folder
documentation_folder = 'documentation'
documentation_folder_files = [f for f in os.listdir(documentation_folder) if f.endswith('.md')]
for f in documentation_folder_files:
    input_file = os.path.join(documentation_folder, f)
    output_file = os.path.join(documentation_folder, f"{os.path.splitext(f)[0]}.html")
    print(f"Converting {input_file} to {output_file}")
    subprocess.run(['pandoc', '-s', '-c', 'base.css', input_file, '-t', 'html', '-o', output_file, '--lua-filter=links-to-html.lua'], stderr=subprocess.DEVNULL)

# Step 3. Uploading everything to GitHub
# If there is a commit message (excluding -translate), then upload
if len([arg for arg in sys.argv[1:] if arg != '--translate']) > 0:
    subprocess.run(['git', 'add', '--all']) 
    commit_message = ' '.join(arg for arg in sys.argv[1:] if arg != '--translate')
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'pull'])
    subprocess.run(['git', 'push'])
else:
    print("Not uploading (Empty commit message)")
