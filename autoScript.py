
from os import listdir, remove, rmdir, rename, mkdir, symlink
from os.path import exists, join
from zipfile import ZipFile


class AutoScript:

    JMSCRIPT_FOLDER = r"C:\Program Files (x86)\World of Warcraft\_retail_\jmScript"
    WOW_FOLDER = r"C:\Program Files (x86)\World of Warcraft\_retail_"

    JM_IN_DOWNLOAD_FOLDER = r"C:\Users\firmi\Downloads\jm.zip"
    JM_IN_RETAIL_FOLDER = r"C:\Program Files (x86)\World of Warcraft\_retail_\jm.zip"

    SHORTCUT_NAME = "jMorph Loader - Atalho.lnk"
    DESKTOP_PATH = r"C:\Users\firmi\Desktop"

    @classmethod
    def deleting_retail(cls):
        """
        This method deletes the previous elements in the directories and previous directories in wow's retail folder
        :return: None
        """
        # Verifying if the original directory and the zip file exists
        if exists(cls.JMSCRIPT_FOLDER) is False:
            return f"O caminho '{cls.JMSCRIPT_FOLDER}' não pode ser encontrado, portanto não pode ser excluído."
        elif exists(cls.JM_IN_RETAIL_FOLDER) is False:
            return f"O caminho '{cls.JM_IN_RETAIL_FOLDER}' não pode ser encontrado, portanto não pode ser excluído."
        else:
            # Removing the files before removing the directory
            for file in listdir(cls.JMSCRIPT_FOLDER):
                remove(join(cls.JMSCRIPT_FOLDER, file))

            # Removing files and directories
            rmdir(cls.JMSCRIPT_FOLDER)
            remove(cls.JM_IN_RETAIL_FOLDER)

            return None

    @classmethod
    def moving_new_files(cls):
        """
        This method moves the brand new 'jm.zip' file from downloads folder to wow folder
        :return: None
        """
        # Verifying if the 'jm.zip' file exists
        if exists(cls.JM_IN_DOWNLOAD_FOLDER) is False:
            return f"O arquivo '{cls.JM_IN_DOWNLOAD_FOLDER}' não existe."
        else:
            rename(cls.JM_IN_DOWNLOAD_FOLDER, cls.JM_IN_RETAIL_FOLDER)
            return None

    @classmethod
    def extracting_zip_files(cls):
        """
        This method extract every content from the zip file and places in a directory
        :return: None
        """
        # Creating a new folder for the extracted files
        mkdir(cls.JMSCRIPT_FOLDER)

        # Extracting the files
        with ZipFile(cls.JM_IN_RETAIL_FOLDER) as file:
            file.extractall(cls.JMSCRIPT_FOLDER)

        # Replacing the folder that was inside the zip file for the one that was created
        old_folder = r"C:\Program Files (x86)\World of Warcraft\_retail_\jmScript\jm"
        for file in listdir(old_folder):
            rename(join(old_folder, file), join(cls.JMSCRIPT_FOLDER, file))
        rmdir(old_folder)

        return None

    @classmethod
    def updating_shotcuts(cls):
        """
        This method removes the old desktop shortcut and replaces with the new one.
        :return: None
        """
        source = join(cls.JMSCRIPT_FOLDER, "jMorph Loader.exe")
        path = join(cls.DESKTOP_PATH, cls.SHORTCUT_NAME)
        # Verifying if the shortcut exists
        if exists(path) is False:
            symlink(source, path)
            return None
        # Removing the old one and replacing it
        else:
            remove(path)
            symlink(source, path)
            return None


if __name__ == '__main__':
    AutoScript.deleting_retail()
    AutoScript.moving_new_files()
    AutoScript.extracting_zip_files()
    AutoScript.updating_shotcuts()
