# Rwyn's Discord Rich Presence - Customizable RPC 
### **[Rwyn's Northstar SexMod RPC (pre-built exe ready 2 go)](https://github.com/rwynx/Rwyns-NorthstarSexModRPC/releases)** and a blank template for you to make your own RPC. 

## Usage - Make sure you have all the dependencies.
* If you want to use Northstar SexMod RPC, go to **[Releases](https://github.com/rwynx/Rwyns-NorthstarSexModRPC/releases)** tab and download the pre-built exe, IF you want to build it yourself/or make your own, continue to read.
* `pip install nuitka`
* `pip install termcolor` for colored text.
* `pip install pyfiglet` alternatively you can try with `pip install pyfiglet --force` for ASCII text.
* IF YOU WANT AN ASCII TEXT on console print: pyfiglet fucked for some reason and Chrome/Windows detects this code as virus, so my advice is to build an exe it with;
`pyinstaller --add-data "Python 3.10.4\Lib\site-packages\pyfiglet;./pyfiglet" --onefile your-app-name.py`
* IF YOU DONT WANT AN ASCII TEXT on console print: just simply delete that line, otherwise exe won't work.
* I use **pyinstaller**, you can use whatever you like. But make sure you have the right parameters ^
* Original exe icon is not included in this package.

## Additional Info
* **rwyn-northstar-sexmodrpc.py** is the main project.
* You can use **"empty_template.py"** to make a customized RPC.
* Everything you need to change addressed in the template.

## Contact
**Discord:** Rwyn#9860

**Originally forked from:** **[Qwertyquerty](https://github.com/qwertyquerty)** please visit their Github if you wish to find more info.

## FAQ
**(WIP) Not done yet.**
