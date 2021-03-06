# Factorio-Modpack-Switcher
Allows for easy switching between factorio modpacks 

Requirements:
 - Python 3 (Any version should work)

Features:
 - Allows for multiple modpacks to be stored and switched out at ease
 - Has a log at %APPDATA%/Factorio
 - Each modpack has its own saves folder to keep your saves organised
 
How to use:
 - Run the file Switch Factorio.py (It'll crash if you don't have Factorio installed)
 - If it's your first time running, it'll ask you to give a name to your current modlist.
 - The script will check what modpacks already exist and will list all but the current one.
 - You can then enter 1 to keep the current modpack, from 2 to n to switch to the modpack in the 'n' position (where n is the number of modpacks) or n+1 to create a new modpack.
 - If you keep current modpack, the program terminates.
 - If you select a different modpack, that one will become the active modpack.
 - If you create a new modpack, then the list of all modpacks will show up again, updated with the new modpack.

NOTE:
Already have 2 mods and saves foldes in your Factorio directory? Simply create a new file "modpackname.txt" in the folder which isn't currently called "mods" in order for it to be recognised as a valid modpack directory. Open this file and write the modpack name on the first line, then save and close.
Example: 
![Example](Capture.PNG)
