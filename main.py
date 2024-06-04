import os
selectedMap = 'gm_construct'
#пиздец мне лень думать
def maplistget(directoryd):
    futurePurpose = directoryd
    mapfolder = directoryd + '\garrysmod\downloadlists'
    directorylist = os.listdir(mapfolder)
    n = 4
    maplist = ([item[:-n] for item in directorylist])
    print(maplist)
    choose = int(input(''))
    selectedMap = maplist[choose]
    startserver(futurePurpose)
    return selectedMap

def startserver(folder):
    print(List)
    print(maplistget)
    os.chdir(folder)
    os.system(
        f'start srcds.exe +maxplayers 5 -console +host_workshop_collection 2571938184 +gamemode sandbox +map {List} +r_hunkalloclightmaps 0')


List = maplistget(input('Enter the directory of your server \nIt is like: *****\steamapps\common\GarrysModDS\n'))