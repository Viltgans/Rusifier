import asyncio
import os.path
import string


async def main():
    global Text
    file_path = ':\\'
    file_name = "hackGU_cmn_a.cpk"
    for letter in string.ascii_uppercase:
        path_file = letter + file_path
        for (current, folders_in_current, files_in_current) in os.walk(path_file):
            for files in files_in_current:
                if files == file_name and files in files_in_current:
                    Text = current
                elif files != file_name and files not in files_in_current:
                    Text = "Путь не найден."
    return Text

if __name__ == '__main__':
    Text = "Путь определяется."
    print(Text)
    asyncio.run(main())
