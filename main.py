import re
from data import *


def get_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
        
    except FileNotFoundError:
        print("File not found")


def remove_extra_information(file_path, old_string, file_content, file_output_path):
    new_string = 'symbol'
    with open(file_output_path, 'w') as file:
        new_contents = file_content.replace(old_string, new_string).replace('%', ' ').replace(',1', '').replace(' ', '').replace('cls', '')
        file.write(new_contents)
        
    return new_contents
    

def get_key(file_content):
    return file_content[:file_content.find('\n')]


def replace_symbol(match):
    list(KEY)
    symbol_index = int(match.group(0)[7:])
    return KEY[symbol_index]


def decrypting_file(file_content, file_output_path, replace_symbol):
    new_contents = re.sub(r'symbol~\d+', replace_symbol, file_content)
    with open(file_output_path, 'w') as file:
        file.write(new_contents)
    
    return new_contents
    

def final_formating(file_content, file_output_path):
    new_contents = file_content.replace('echooff', 'echo off').replace('.exe', '.exe ').replace('/t', '/t ').replace(KEY, '').replace("Disabled", " Disabled")
    with open(file_output_path, 'w') as file:
        file.write(new_contents)


if __name__ == "__main__":
    file_content = get_file_content(file_path)
    file_content = remove_extra_information(file_path, old_string, file_content, file_output_path)
    
    KEY = get_key(file_content)

    file_content = decrypting_file(file_content, file_output_path, replace_symbol)
    final_formating(file_content, file_output_path)

