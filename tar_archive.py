#!/usr/bin/env python3

import sys
import subprocess
import time

def main():
    '''
    function to archive or unarchive tar files much easier,
    according to the single letter argument given when calling
    it, along with the name of file being archived or unarchived.
    arg: str
    file: str
    '''
    # i might possibly make the next iteraton of this little
    # extraction utility more interactive, but it is almost 2am, 
    # and i am getting too tired to think clearly right now.

    # variable declarations
    datetime = time.strftime('%Y/%m/%d_%H:%M')
    suffix = datetime + '.backup.tar.gz'
    arg = sys.argv[1]
    absolute_path = sys.argv[2]
    path_split = absolute_path.split('/')
    filename = pathpath_split[-1]

    # try/except clause in case any typos or unintended chars get entered
    try:
        # program logic for the archive process
        if arg == 'z':
            subprocess.Popen(['tar czvf', '~/Documents/' + filename + '.' + suffix, absolute_path])
        # program logic for the unarchive process
        elif arg == 'u':
            subprocess.Popen(['tar xzvf', absolute_path])
        # hippity hoppity, easter's on its way!
        elif arg == 'hello' and absolute_path == 'world':
            print('You have found the magic easter egg! Make a wish, and the\ntoothe fairy will leave you a present under the christmas tree')
            quit()
        # if the input argument fits neither above, raise error
        else:
            raise ValueError


    except Exception as err:
        print(err)
        quit()

if __name__ == '__main__':
    main()
