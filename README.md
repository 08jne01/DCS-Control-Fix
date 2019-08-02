# DCS-Control-Fix

Python is required

# How to use

- Make a backup of your controls
- Put this script in the input folder in the saved games so it is along side all your module control folders.
- Edit the ids and old_ids list so that they contain the large ids they look like this -> BBCBD090-048B-11e5-8001-444553540000
don't include the curly braces. The old and new ids must be in the same position in the list otherwise it will replace it with incorrect ids.
- To get your old id simply look at one of your controls and you should see the controls something like "Joystick - HOTAS Warthog {BBCBD090-048B-11e5-8001-444553540000}.diff.lua"
simply copy the ID between the curly braces and add it to the old_ids list.
- To get the new ids you must run dcs and save a control scheme on one plane. This will add the new control files with their respective ids to your new saved games.
- Add these to ids list making sure that the same controllers are in the same place in the list.
- After you retrive all the new ids delete the new config folder and replace it with your old one.
- Open a command prompt at that location and then type python fix.py
- The program will run and fix your ids!
