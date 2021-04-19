# VirtualPianoBot
A virtual piano player, that you can train to play different songs, as well as the built-in songs.


# Setup:

  1. Ensure you have python installed. (Python 3.8 recommended)
     
     If you don't have python, get it at https://www.python.org/downloads/release/python-385/
     
  2. Go into your terminal and execute these following commands,
  
     `cd downloads` OR `cd Downloads`
     
     `git clone https://github.com/azh412/VirtualPianoBot.git`
     
     `pip3 install pyautogui`

     `pip3 install termcolor`
         
# Usage:

   To run the bot, execute `python3 VirtualPianoBot` to play one song, into the terminal.
   
   If you want a mashup, run `python3 mashup.py`
   
   (Note: With Mac, you need to add `sudo` to the beginning of the `python3` commands, and enter your sudo password, usually your computer password.)
   
   Then, choose a song name based on the txt files in the new folder in Downloads.
     
   Lastly, switch to the window you want to play the piano on, and press the `esc` key to start and hold the `esc` key to stop the bot!
   
# Add new songs

   If you want to add new songs to play:
   
   1. Find / create a virtual piano sheet for that song.
   
   2. Add the sheet into a txt file in the `sheets` folder.
   
   3. Run `python3 sheetanalyze.py` and enter the sheet name. (Based on the name you gave the file when you made it)
   
      You can also manually change the sheet by following these criteria:
      
      The character `|` should be replaced with a new line,
      
      The character `-` should have a space before and after it, to become ` - `,
      
      Characters that should be played rapidly should have a ` - ` in between characters,
      
      And finally, characters grouped together with brackets, (i.e `[abcd]`) should not have any braces.
      
   4. If you used `sheetanalyzer.py`, there would be a new file created in your file system. Delete the old file and replace it with the new one. You should also take the new lines at the beginning out.
   
   5. In `virtualpianobot.py` or `mashup.py`, add the song to the list `w` and insert a `Song()` given the examples shown.
   
   That's it! Consider making a `pull request` to contribute and add the song to the default bot!

