import os
import re

reg = r'\{(.*?)\}'

#New ID
ids = ["new id of your joystick", "new id of your throttle", "new id of your pedals"]
#Corresponding old ID. The new and old must be in the same position in the list
old_ids = ["old id of your joystick", "old id of your throttle", "old id of your pedals"]

dir_path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(dir_path)


for directory in dirs:
    if (os.path.isdir(directory)):
        if (os.path.isdir(directory + "/joystick")):
            #path = path + "/" +"joystick/"
            files = os.listdir(directory + "/joystick")
            for controls in files:
                n = 0
                for id in old_ids:
                    reg = r'\{' + id + '\}'
                    s = re.sub(reg, "{" + ids[n] + "}", controls)
                    if (s != controls):
                        path = dir_path + "/" + directory + "/joystick/"
                        os.rename(path + controls, path + s)
                        print "Renaming file to {}".format(s)
                    n += 1
