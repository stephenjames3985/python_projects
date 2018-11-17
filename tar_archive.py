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
    # i will make the next iteraton of this a more feature rich
    # and capable in the future, but it is getting super late as
    # i write this, and i am getting too tired to think clearly
    # right now

    # global variables
    datetime = time.strftime('%Y/%m/%d_%H:%M')
    suffix = '.' + datetime + '.backup.tar.gz'
    default_dir = os.getcwd()

    # this variable will have use for the logic i am planning for multiple OS
    # compatibility in the future
    system_type = sys.platform

    # if there are arguments called with the script, just like calling a regular
    # tar command order
    if len(sys.argv) > 1:
        # variable declarations
        arg = sys.argv[1]
        filename = sys.argv[2]
        path = sys.argv[3]
        # by default, the files will be *.tar.gz
        if arg.lower() == 'c':
            tar = tarfile.open(name=filename + suffix, mode='x:gz')

    # if there are no arguments given with the script
    else:
        # input variable creation
        arg = input('Would you like to [c]ompress or e[x]tract a tar archive?\n>> ')
        path = input('Please enter the (abs) path to the directory which contains the file(s)\nyou would like to compress or extract.\n>> ')
        filename = input('Please enter the name of the file or directory to be archived.\n>> ')
        compression = input('Would you like to use compression type [gz], [bz2], or [xz]?\n>> ')
        name = filename + datetime + '.tar.' + compression


    # define function to put us in the working directory
    def ch_working_dir():
        '''
        when called, the function will change to the desired directory
        '''
        os.chdir(path)
        return os.listdir()

    # define function for compression/creation of tarfile
    def make_tar_file():
        '''
        this is the main function of this program, which is to create a tarfile
        '''
        # (until i am able to add more to it when i have more time and i am not also completely exhausted haha)
        current_dir = ch_working_dir()
        tar = tarfile.open(name, 'x:' + compression)
        for file in current_dir:

            tar.add(file)

        tar.close()


    # try/except clause in case any typos or unintended chars get entered
    try:
        # call function for the archive process
        make_tar_file()
    # if process completes with exit status other than 0, raise Exception
    except Exception as err:
        print(err)
        quit()

if __name__ == '__main__':
    main()
