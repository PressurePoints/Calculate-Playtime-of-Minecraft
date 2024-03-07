import os
import json
from datetime import datetime, timedelta

def calculate_playtime(stats_path,uuid):
    file_name = f"{uuid}.json"  # The file name is the UUID of the player
    file_path = os.path.join(stats_path, file_name)
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            # The play time is stored in the "minecraft:play_time" field
            play_time = data.get("stat.playOneMinute", 0) / 72000 # for low than 1.13

            if play_time == 0:
                play_time = data.get("stats",{}).get("minecraft:custom",{}).get("minecraft:play_one_minute", 0) / 72000 # for 1.13 to 1.17

            if play_time == 0:
                play_time = data.get("stats",{}).get("minecraft:custom",{}).get("minecraft:play_time", 0) / 72000 # for 1.17 and higher

            return play_time
    except FileNotFoundError:
        #print(f"File {file_path} not found.")
        return 0
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {file_path}.")
        return 0

def main():
    #minecraft_path = "E:\My_Game\MC\PCL2\.minecraft" # Change this to your .minecraft folder
    minecraft_path = input("Enter the path to the .minecraft folder:") or "E:\My_Game\MC\PCL2\.minecraft"
    work_path = os.path.join(minecraft_path, 'versions')
    if not os.path.exists(work_path):
        print(f"Path {work_path} not found.")
        return
    file_path = "playtime.txt"
    full_uuid = input("Enter your full UUID(like 6aaabf3d-9f7b-45e0-8f90-52f558bdbc73):") or "6aaabf3d-9f7b-45e0-8f90-52f558bdbc73"
    #full_uuid = "6aaabf3d-9f7b-45e0-8f90-52f558bdbc73" # Change this to your full UUID
    
    with open(file_path, 'w', encoding='utf-8') as file:  
        total_playtime = 0 # Total playtime for all versions  
        version_time_info = [] # Playtime for each version

        for version_name in os.listdir(work_path):
            saves_path = os.path.join(work_path, version_name, 'saves')

            if (not os.path.exists(saves_path)) or (not bool(os.path.isdir(saves_path))):
                #file.write(f"Version: {version_name} has no saves\n\n")
                version_time_info.append((version_name,0,[]))
                continue
            
            saves_time_info = [] # Playtime for each save in this version
            version_playtime = 0 # Total playtime for this version

            for saves_name in os.listdir(saves_path):
                if os.path.isfile(os.path.join(saves_path, saves_name)):
                    continue
                stats_path = os.path.join(saves_path, saves_name, 'stats')
                play_time = calculate_playtime(stats_path,full_uuid)
                saves_time_info.append((saves_name,play_time))
                version_playtime += play_time
            
            version_time_info.append((version_name,version_playtime,saves_time_info))

            total_playtime += version_playtime

        file.write(f"Total playtime: {total_playtime} h\n\n")
        # Sort versions by playtime
        for version_name, version_playtime, saves_time_info in sorted(version_time_info, key=lambda x: x[1], reverse=True):
            file.write(f"Version: {version_name}, Total playtime: {version_playtime} h\n")

            # Sort saves by playtime
            for save_name, playtime in sorted(saves_time_info, key=lambda x: x[1], reverse=True):
                file.write(f"\tSave: {save_name}, Playtime: {playtime} h\n")
            file.write("\n") # Empty line 

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
