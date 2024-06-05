import os


def Start(set, clientpath):
    n=4
    maplist = os.listdir(set)
    maplist = ([item[:-n] for item in maplist])
    print(maplist)
    choose = int(input(''))
    selectedmap = maplist[choose-1]
    print(selectedmap)
    os.chdir(clientpath)
    os.system(f'start srcds.exe +maxplayers 5 -console +host_workshop_collection 2571938184 +gamemode sandbox +map {selectedmap}  +r_hunkalloclightmaps 0')


pathserver = input('Enter the path to your server  \nIt is like:  *****\steamapps\common\GarrysModDS\n')
path = pathserver + '\garrysmod\downloadlists'
a = Start(path, pathserver)