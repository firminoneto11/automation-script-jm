![GitHub repo size](https://img.shields.io/github/repo-size/firminoneto11/automation-script-jm)
![GitHub language count](https://img.shields.io/github/languages/count/firminoneto11/automation-script-jm)
![GitHub top language](https://img.shields.io/github/languages/top/firminoneto11/automation-script-jm)
![GitHub](https://img.shields.io/github/license/firminoneto11/automation-script-jm)
![GitHub last commit](https://img.shields.io/github/last-commit/firminoneto11/automation-script-jm)

<h1>automation-script-jm</h1>
<h2>This repository contains the script that i made in order do automate the extraction of a zip file.</h3>
<br/>
<hr/>
<div align='center'><h3>🤔 What is Jmorph? 🤔</h3></div>
<br/>
<p>Jmorph is a third party software that allows players in a game called 'World of Warcraft' to change and customize their appearances without having to actually change it in the ordinary way. However, the change made by the software can only be seen by the user's and not by other players, which makes Jmorph a usefull tool when it comes to changing the player's style at anytime wanted!</p>
<hr/>
<div align='center'><h3>😁 How can i download it? 😁</h3></div>
<br/>
<p>Jmorph can be downloaded at this <a href='https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-bots-programs/795619-jmorph-tmorph-morpher-recreated.html'>website</a>. Remember that you also need to have installed 'World of Warcraft' game, because this tool is designed for it.</p>
<hr/>
<div align='center'><h3>👻 Why did you made this script? 👻</h3></div>
<br/>
<p>World of Warcraft is a game with a long history now, and part of that history includes updates, and a lot of them! Everytime the game got updated i had to re-download the jMorph tool (once the owner had updated it as well), had to move it to my World of Warcraft's folder, had to unzip it and create a shortcut to the desktop area. All of these steps could be automated and thats how i came up with the idea.</p>
<hr/>
<div align='center'><h3>🤔 Will the script work for me as well? 🤔</h3></div>
<br/>
<p>Since i made the script based on my directory folder, the script it's not going to work if you don't make a couple changes in it. I'll show you what parts you have to change if you want to use it too.</p>
<h4>What you need to install -<h4>
<p>Before changing the code, make sure you have the following elements installed on your computer: </p>
<h5>* Applications</h5>

- [x] Python 3 or superior;
- [x] A source code editor. I use <a href='https://www.jetbrains.com/pycharm/'>PyCharm</a>, but feel free to use any other;

<h5>* Libraries</h5>
<p>Use these two following commands to install the libraries after you have installed Python -</p>

```python
# Installing 'pyinstaller'
pip install pyinstaller
  
# Installing 'zipfile'
pip install zipfile38
```
<p>Now that you are all set, these are the variables that you need to change in the code: </p>
<img src="https://github.com/firminoneto11/automation-script-jm/blob/main/assets/one.JPG" alt="first image of variables">
<br/>
<img src="https://github.com/firminoneto11/automation-script-jm/blob/main/assets/two.JPG" alt="second image of variables">
<p>Since all these variables are absolute paths, you just have to replace my path for yours and they MUST have the zip files at the end.</p>
<p>With the changes done, you now need to create an executable file (.exe), to run it as administrator, otherwise it will generate a 'PermissionError', because in order to create symbolic links, windows operational system requires permission.</p>
<p>To create the executable file, you just need to use the following command on your terminal: </p>

```python
# This line of code will create the executable file for the script and when you run it, it will pop up as administrator
pyinstaller --onefile --uac-admin "jmorph_Automation.py"
```
<hr/>
<div align='center'><h3>💻 Abstract 💻</h3></div>
<br/>
<p>Now, a quick recapture of what the script was made for:

- Deletes the previous files in the download folder and World of Warcraft's retail folder;
- Moves the new zip file from the download folder to World of Warcraft's retail folder;
- Extracts the new zip file in the World of Wacraft's retail folder;
- Updates the old jMorph shortcut in the desktop for the new one;

With this, everytime jMorph gets updated, you can just download it, run the script and it will automatically update the desktop shortcut without having to do it manually.

<hr/>
<div align='center'><h3>👾 Author 👾</h3></div>
<br/>
<p>Made with ♥ by <a href="https://github.com/firminoneto11">Firmino Neto</a>.
</p>
