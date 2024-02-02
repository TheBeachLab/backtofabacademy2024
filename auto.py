import os
import glob
import subprocess
import re
import sys

def concatenate_files(directory):
    # Get absolute path of the directory
    abs_directory = os.path.abspath(directory)

    # Get all markdown files that contain the word 'chapter'
    markdown_files = glob.glob(abs_directory + '/**/*chapter*.md', recursive=True)

    # Group files by parent directory
    files_by_directory = {}
    for file in markdown_files:
        dir_name, file_name = os.path.split(file)
        if dir_name not in files_by_directory:
            files_by_directory[dir_name] = []
        files_by_directory[dir_name].append(file)

    # For each directory, concatenate the files and save in the parent directory
    for dir_name, files in files_by_directory.items():
        # Sort the files to maintain chapter order
        files.sort()
        # Create the new file name
        new_file_name = re.sub(r'-chapter-\d{2}-', '-', os.path.basename(files[0]))
        new_file_path = os.path.join(os.path.dirname(dir_name), new_file_name)
        # Concatenate the files
        with open(new_file_path, 'w') as outfile:
            for file_name in files:
                with open(file_name, 'r') as infile:
                    outfile.write(infile.read())


# Step 0. Optional. Translation if first parameter is '--translate'
if len(sys.argv) > 1:
    if sys.argv[1] == '--translate':
        subprocess.run(['git', 'add', '--all'])  # Modified files need to be added, otherwise, they are not translated
        subprocess.run(['python3', 'translate-en.py'])
        subprocess.run(['python3', 'translate-de.py'])

# Step 1. Concatenate chapters
concatenate_files('documentation')

# Step 2. README.md --> index.html in the current folder
subprocess.run(['pandoc', '--katex', '--from', 'markdown+tex_math_single_backslash', '--filter', 'pandoc-sidenote', '--to', 'html5+smart', '--template=template', '--css=css/theme.css', '--css=css/skylighting-solarized-theme.css', '--wrap=none', '--output', "index.html", '--lua-filter=links-to-html.lua', "README.md"])


# Step 3. /md/*.md --> /html/*.html in the documentation folders
documentation_folders = ['documentation/es/md', 'documentation/en/md', 'documentation/de/md']
for folder in documentation_folders:
    html_folder = os.path.join(os.path.dirname(folder), 'html')
    folder_files = [f for f in os.listdir(folder) if f.endswith('.md')]
    for f in folder_files:
        input_file = os.path.join(folder, f)
        output_file = os.path.join(html_folder, f"{os.path.splitext(f)[0]}.html")
        print(f"Converting {input_file} to {output_file}")
        subprocess.run(['pandoc', '--katex', '--from', 'markdown+tex_math_single_backslash', '--filter', 'pandoc-sidenote', '--to', 'html5+smart', '--template=template', '--css=../../../css/theme.css', '--css=../../../css/skylighting-solarized-theme.css', '--wrap=none', '--output', output_file, '--toc', '--lua-filter=links-to-html.lua', input_file])


# Step 4. Optional. Upload everything to GitHub
# If there is a commit message (excluding -translate), then upload
if len([arg for arg in sys.argv[1:] if arg != '--translate']) > 0:
    subprocess.run(['git', 'add', '--all']) 
    commit_message = ' '.join(arg for arg in sys.argv[1:] if arg != '--translate')
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'pull'])
    subprocess.run(['git', 'push'])
else:
    print("Not uploading (Empty commit message)")
