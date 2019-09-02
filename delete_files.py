import os
import fnmatch

dir_path = 'E:\\Web Development Tutorials\\PHP Framework\\Real Time Single Page Forum App with Pusher Laravel & vuejs'

# Get a list of all files in directory
for rootDir, subdirs, filenames in os.walk(dir_path):
    # Find the files that matches the given patterm
    for filename in fnmatch.filter(filenames, '*.vtt'):
        try:
            os.remove(os.path.join(rootDir, filename))
        except OSError:
            print("Error while deleting file")

        print('Files removed successfully')
