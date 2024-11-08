#!/usr/bin/env python


import os
import re
import subprocess


#dirs = ['../ZTT/datacards_modified', '../W/datacards_modified', '../HF/datacards_modified']  # rm ZTT for now
dirs = ['W/datacards_modified', 'HF/datacards_modified']


pattern = re.compile(r'dc_(\d+)\.txt')


files_dict = {}


os.system('mkdir datacards_modified')

for directory in dirs:
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            number = match.group(1)
            if number not in files_dict:
                files_dict[number] = {}
            files_dict[number][directory] = os.path.join(directory, filename)


for number, files in files_dict.items():
    if len(files) == len(dirs):  # Make sure all directories have this number
#        file1 = files['../ZTT/datacards_modified'] rm ZTT for now 
        file2 = files['W/datacards_modified']
        file3 = files['HF/datacards_modified']
        output_file = "dc_%s.txt" % str(number)
        

#        command = "combineCards.py %s %s %s > %s"% (str(file1) ,str(file2) ,str(file3), str(output_file))  # rm ZTT for now
        command = "combineCards.py %s %s > %s"% (str(file2) ,str(file3), str(output_file))
        
        print("Running command: %s" % (command) )
        os.system(command)
        os.system('mv dc_*txt Combo/datacards_modified')
    else:
        print("Skipping number %s, not all directories have the file." % str(number))


