# Rwyn's Discord Rich Presence - Customizable RPC 
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
  
## Usage - Make sure you have all the dependencies.

### Following dependencies are needed if you want to make your RPC just like mine. But there's a problem with **pyfiglet** and only solution I could find was copying pyfiglet folder from python site-packages into my project folder, and adding the parameters in line 4 while using **pyinstaller.** 
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
* It's just an RPC and obviously there is no need for help, but if you upload the rpc you made with template (pypresence), it might be good to display them as examples.


### More info can be found in **[Qwertyquerty's Pypresence](https://github.com/qwertyquerty?tab=repositories)**
