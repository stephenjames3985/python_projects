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
    #suffix = '.' + datetime + '.backup.tar.gz'
    default_dir = os.getcwd()

    # input variables determined by user interaction
    arg = input('Would you like to [c]ompress or e[x]tract a tar archive?\n>> ')
    location = input('Please enter the (abs) path to the location which contains the file(s)\nyou would like to compress or extract.\n>> ')
    filename = input('Please enter the name of the file archive to be created or extracted.\n>> ')
    compression = input('Would you like to use compression type [gz], [bz2], or [xz]?\n>> ')
    name = filename + '_' + datetime + '.tar.' + compression

    # this variable will have use for the logic i am planning for multiple OS
    # compatibility in the future
    system_type = sys.platform

    # define function to put us in the working directory
    def ch_working_dir():
        '''
        when called, the function will change to the desired directory, and list its contents
        '''
        os.chdir(path)
        return os.listdir()

    # define function for compression/creation of tarfile
    def make_tar_file():
        '''
        calling this function calls ch_working dir() creates the desired tarfile
        '''
        # tar variable declaration
        tar = tarfile.open(name, 'x:' + compression)
        # loop through all of the files in the current directory
        for file in ch_working_dir():
            # add file to the tar archive
            tar.add(file)
        # close the tarfile once it is done writing itself
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
