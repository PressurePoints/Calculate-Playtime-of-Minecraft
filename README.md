# Introduction
This is a simple code for calculating your playtime of minecraft.
The code will output a txt file in the work path named playtime.txt, which has the following format:

> Total playtime: XX h
> 
> Version: "Version name1", Total playtime: XX h
> - Save: "Save name1", playtime: XX h
> - Save: "Save name2", playtime: XX h
> 
> Version: "Version name2", Total playtime: XX h
> - Save: "Save name1", playtime: XX h
> - Save: "Save name2", playtime: XX h

Tips: The version and save is orderd by the playtime(from big to small).

# How to use
1. check if you are satisfied with the default settings in the code. Which means:
    - You are playing **Minecraft java edition**.
    - **Version isolation** are enabled. So your file path should be like this:
    
        .minecraft
        |── ......
        ├── versions
        │   ├── ......
        │   ├── "Your version name"
        │   │   ├── ......
        │   │   ├── saves
        │   │   │   ├── ......
        │   │   │   ├── "Your save name"
        │   │   │   │   ├── ......
        │   │   │   │   ├── stats
        │   │   │   │   │   ├── YourFullUUID.json

2. **Run the .exe file in the dist folder**.
3. Enter your **.minecraft path** and **your UUID** in the terminal. 
    > Tips: You can find your UUID in the stats folder or search in this [website](https://mcuuid.net/).
4. Wait for the code to finish. The playtime.txt will be in the work path.