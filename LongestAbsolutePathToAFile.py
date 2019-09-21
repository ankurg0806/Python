# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
    # subdir1
    # subdir2
        # file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
    # subdir1
        # file1.ext
        # subsubdir1
    # subdir2
        # subsubdir2
            # file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

import re

def myfunct(s):
    mypattern = '\n[\t]+'
    mylistOfDirAndFiles = re.split(r'\n[\t]+',s)
    myListOfSeparators = re.findall(r'\n[\t]+',s)
    print(mylistOfDirAndFiles)
    print(myListOfSeparators)
    farthestFileSepLen = 0
    farthestFileSep = ''
    farthestFileSepIndex = -1
    for index, sep in enumerate(myListOfSeparators):
        if len(sep) > len(farthestFileSep):
            if mylistOfDirAndFiles[index+1].find('.') > 0:
                farthestFileSepLen = len(sep)
                farthestFileSep = sep
                farthestFileSepIndex = index
    if farthestFileSepIndex == -1:
        print("No file found")
        return 0
    myFilePath = mylistOfDirAndFiles[farthestFileSepIndex+1]
    for index in range(farthestFileSepIndex-1,-1,-1):
        if len(farthestFileSep) > len(myListOfSeparators[index]):
            myFilePath = mylistOfDirAndFiles[index+1] + '\\' + myFilePath
            farthestFileSep = myListOfSeparators[index]
    myFilePath = mylistOfDirAndFiles[0]+ '\\' + myFilePath
    print (myFilePath)
    return len(myFilePath)
        
print(myfunct("dir\n\tsubdir1\n\t\tsubsubdir1\n\t\t\tsubsubsubdir1\n\t\t\t\tfile1.txt\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

