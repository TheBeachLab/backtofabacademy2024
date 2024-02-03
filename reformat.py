import os

def process_md_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace '##' with '#'
    content = content.replace('##', '#')

    # Replace '###' with '##' after the first pass
    content = content.replace('###', '##')

    with open(file_path, 'w') as file:
        file.write(content)

def process_directory(directory_path, num_passes=2):
    for _ in range(num_passes-1):
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                if file_name.endswith('.md'):
                    file_path = os.path.join(root, file_name)
                    process_md_file(file_path)

if __name__ == "__main__":
    directory_path = "documentation/es/md/w01/"  # Replace with the actual path
    process_directory(directory_path, num_passes=2)
