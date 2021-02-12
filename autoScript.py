
import os
import zipfile as zp

# 1 - deletar a pasta 'jm' e o arquivo jm.zip em 'C:\Program Files (x86)\World of Warcraft\_retail_'


def deleting():
    file_zip = "C:\\Program Files (x86)\\World of Warcraft\\_retail_\\jm.zip"
    old_folder = "C:\\Program Files (x86)\\World of Warcraft\\_retail_\\jm"
    if os.path.exists(file_zip) or os.path.exists(file_zip) is False:
        return "Um dos arquivos não existem!"
    # Removing files before removing directories
    for file in os.listdir(old_folder):
        os.remove(f"C:\\Program Files (x86)\\World of Warcraft\\_retail_\\jm\\{file}")
    # Removing files and directories
    os.rmdir(old_folder)
    os.remove(file_zip)

    return None


print(deleting())
# 2 - mover o arquivo jm.zip de 'C:\Users\firmi\Downloads' para 'C:\Program Files (x86)\World of Warcraft\_retail_'


def moving():
    new_morph = r"C:\Users\firmi\Downloads\jm.zip"
    wow_folder = r"C:\Program Files (x86)\World of Warcraft\_retail_\jm.zip"
    if os.path.exists(new_morph) is False:
        return "Não há um novo arquivo zip!"
    os.rename(new_morph, wow_folder)
    return "Jmorph movido!"


print(moving())

# 3 - Extrair o arquivo jm.zip no diretório corrente


def extracting():
    zip_file = r"C:\Program Files (x86)\World of Warcraft\_retail_\jm.zip"
    os.mkdir(r"C:\Program Files (x86)\World of Warcraft\_retail_\jmScript")
    extracted = r"C:\Program Files (x86)\World of Warcraft\_retail_\jmScript"
    with zp.ZipFile(zip_file) as file:
        file.extractall(extracted)

    old_folder = r"C:\Program Files (x86)\World of Warcraft\_retail_\jmScript\jm"
    for file in os.listdir(old_folder):
        os.rename(old_folder + f"\\{file}", f"C:\\Program Files (x86)\\World of Warcraft\\_retail_\\jmScript\\{file}")
    os.rmdir(old_folder)


print(extracting())
