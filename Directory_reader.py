import os, sys

#Author: Propser Orjiogo(Tempah)


"""
this is a function that takes a directory as an argument
and reads the content of all files within the directory 
before pasting into a new file
"""


def copy_file_content(directory_path, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                try:
                    with open(filepath, 'r') as file:
                        output.write(directory_path)
                        output.write('\n\n')
                        output.write(file.read())
                        output.write('\n')
                except Exception as e:
                    print(f'Error reading {filepath}: {e}')
                    
                    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python script.py <source_dir> <output_file>')
    else:
        source_dir = sys.argv[1]
        output_file = sys.argv[2]
    copy_file_content(source_dir, output_file)