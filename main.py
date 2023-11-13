import pygetwindow as gw
import time
import pypresence

def getWatching():
    titles = gw.getAllTitles()
    index = -1
    for i in range(len(titles)):
        if "1moviestv" in titles[i]:
            index = i
            break
    if index != -1:
        full = titles[index]
        rest = full[6:len(full)] # "Watch " is 6 characters
        fullIndex = rest.find("full")
        return rest[0:fullIndex]
    return None

def ShowString(current):
    last = str(current).rindex(":")
    return current[0:last]
    

try:
    clientId = 979442737990471710
    RPC = pypresence.Presence(client_id=clientId)
    RPC.connect()
    start = int(time.time())
    while True:
        fullWatching = getWatching()
        if fullWatching is None:
            continue
        else:
            seasonindex = fullWatching.find("Season")
            watching = ""
            if seasonindex != -1:
                watching = ShowString(fullWatching)
            else:
                watching = fullWatching
            RPC.update(state="Watching", large_image='my_project'
                    , start=start, details=watching)
            time.sleep(5)
except pypresence.exceptions.DiscordNotFound:
    print("Discord is not running")
except pypresence.exceptions.ServerError:
        print("Connection to Discord has been closed")
except pypresence.exceptions.InvalidID:
        print("Discord was closed!")
