Scripts
=======

Just random scripts that I use that might be useful to others.

dvorak.xlsm
-----------

Keyboard Layout switcher written in Excel. Used it to bypass IT permissions
to set my keyboard layout to Dvorak. It write to the layout to the registry
so that the next time you log in the layout should be the default.


You'll have to know layout the code you want though (0010409 for Dvorak which is what I use). See
[here](http://msdn.microsoft.com/en-us/library/windows/desktop/dd318691\(v=vs.85\).aspx)
and [here](http://msdn.microsoft.com/en-us/library/windows/desktop/dd318693\(v=vs.85\).aspx) for more details.

When opened in Excel, press Alt+F8 and run the ShowWin macro.

movemp3.py
----------
Scans the list of audio files in a directory (source_dir) it's sub dirs
and moves the files to dest_dir/artistname if dest_dir/artistname exists.
If there are 10 or more files by artist in source_dir the dest_dir/artistname
is created.

You need to have puddletag installed to run this (http://puddletag.sf.net).

**Usage: python movemp3.py source_dir dest_dir**
