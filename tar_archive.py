#!/usr/bin/env python3

import sys
import tarfile
import time
import os

def main():
    '''
    function to archive or unarchive tar files much easier,
    according to the single letter argument given when calling
    it, along with the name of file being archived or unarchived.
    arg: str
    file: str
    '''
    # i might possibly make the next iteraton of this little
    # extraction utility more interactive, and capable in the future,
    # but it is almost 1am as i write this, and i am getting too
    # tired to think clearly right now.

    # global variables
    datetime = time.strftime('%Y/%m/%d_%H:%M')
    suffix = '.' + datetime + '.backup.tar.gz'
    default_dir = os.getcwd()

    # if there are arguments called with the script, just like calling a regular
    # tar command order
    if len(sys.argv) > 1:
        # variable declarations
        arg = sys.argv[1]
        filename = sys.argv[2]
        path = sys.argv[3]
        # by default, the files will be *.tar.gz
        tar = tarfile.open(name=filename + suffix, mode='x:gz')

    # if there are no arguments given with the script
    else:
        # input variable creation
        arg = input('Would you like to [c]ompress or e[x]tract a tar archive?\n>> ')
        path = input('Please enter the (abs) path to the directory which contains the file(s)\nyou would like to compress or extract.\n>> ')
        filename = input('Please enter the name you would like appended to the archive.\n>> ')
        compression = input('Would you like to use compression type [gz], [bz2], or [xz]?\n>> ')
        name = filename + datetime + '.tar.' + compression
        tar = tarfile.open(name, mode='x:' + compression)

    # define function to put us in the working directory
    def ch_working_dir():
        '''
        when called, the function will change to the desired directory
        '''
        os.chdir(path)
        files = os.listdir()

    # define function for compression/creation of tarfile
    def make_tar_file():
        '''
        this is the main function of this program, which is to create a tarfile
        '''
        # (until i am able to add more to it when i have more time and i am not also completely exhausted haha)


    # try/except clause in case any typos or unintended chars get entered
    try:
        # program logic for the archive process

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
