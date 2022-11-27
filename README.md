# Rwyn's Discord Rich Presence - Customizable RPC 
### **[Rwyn's Northstar SexMod RPC (pre-built exe ready 2 go)](https://github.com/rwynx/Rwyns-NorthstarSexModRPC/releases)** and a blank template for you to make your own RPC. 

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
  
<img align="right" src="https://github.com/rwynx/Rwyns-NorthstarSexModRPC/blob/main/assets/assets-2.png?raw=true">

## Usage - Make sure you have all the dependencies.
* If you want to use **Northstar SexMod RPC**, go to **[Releases](https://github.com/rwynx/Rwyns-NorthstarSexModRPC/releases)** tab and download the pre-built exe, IF you want to build it yourself/or make your own, continue to read.
* `pip install nuitka`
* `pip install termcolor` for colored text.
* `pip install pyfiglet` alternatively you can try with `pip install pyfiglet --force` for ASCII text.
* IF YOU WANT AN ASCII TEXT on console print: pyfiglet fucked for some reason and Chrome/Windows detects this code as virus, so my advice is to build an exe it with;
`pyinstaller --add-data "Python 3.10.4\Lib\site-packages\pyfiglet;./pyfiglet" --onefile your-app-name.py`
* IF YOU DONT WANT AN ASCII TEXT on console print: just simply delete that line, otherwise exe won't work.
* I use **pyinstaller**, you can use whatever you like. But make sure you have the right parameters ^
* Original exe icon is not included in this package.

## Additional Info
* ~**rwyn-northstar-sexmodrpc.py** is the main project.~ It is not a part of this project anymore, you can still use the template or the released EXE.
* You can use **"empty_template.py"** to make a customized RPC. 
* Everything you need to change addressed in the template.

## Contributing
* There is no need for urgent help, but if you upload the rpc you made with template (pypresence), it might be good to display them as sample projects.

## FAQ
* **(WIP) Not done yet.**
* But more info can be found in **[Qwertyquerty's Pypresence](https://github.com/qwertyquerty?tab=repositories)**
