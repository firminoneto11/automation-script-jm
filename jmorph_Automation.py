from autoScript import AutoScript


def script_execution():
    # Step 1 - Deleting previous files
    AutoScript.deleting_retail()
    # Step 2 - Moving the new file
    AutoScript.moving_new_files()
    # Step 3 - Extracting zip file
    AutoScript.extracting_zip_files()
    # Step 4 - Updating shortcuts
    AutoScript.updating_shotcuts()

    print("Script de automação rodado com sucesso!")
    return input("Pressione enter para fechar: ")


print(script_execution())
