# import scripts
import urllib
import urllib2
import os
import sys
import json

# init vars
api 		= 'http://squarespro.com/mattspi'
roms 		= '/home/pi/RetroPie/roms/'

# grab array of local games
local 		= []
for (path, dirnames, filenames) in os.walk(roms):
    local.extend(os.path.join(path, name).replace(roms,'') for name in filenames)

# grab array of remote games
response        = urllib2.urlopen(api + '/roms/read.php')
remote          = json.load(response)

# compare local and remote games
games 		= []
for game in remote:
	if game not in local:
		games.append(game)

# iterate all games to add and download to proper place
for filepath in games:
        # request the download
	encoded	 	= urllib.quote(filepath)
	download        = urllib2.urlopen(api + '/roms/downloads/' + encoded)
        # open local file for writing
        with open(roms + filepath, 'wb') as local_file:
                local_file.write(download.read())
