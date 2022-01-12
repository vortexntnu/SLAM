

In order to use the config_converter.py you need: 
1. An old zed 2 calibration file
2. A new ros calibration file

To use the script one needs to use the terminal. Example: ~/vortex_ws/src/SLAM/zed2_params/scripts python3  oldFile.txt newFile.txt
If you are not in the scripts folder you need to include the relative path to the files.
Once you run the command, a new config file will be created, and by default will have a name that is equal to the date of its creation.

Alternativly you can type your own name:
Example:
~/vortex_ws/src/SLAM/zed2_params/scripts python3  oldFile.txt newFile.txt updatedConfigFile.txt

The new config file will automatically have the same stereo parameters that is found in the old zed 2 calibration file.
