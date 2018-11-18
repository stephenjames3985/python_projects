#!/usr/bin/env python3

import sys
import tarfile
import time
import os
import shutil


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
    datetime = time.strftime('%Y-%m-%d_%H:%M')
    #suffix = '.' + datetime + '.backup.tar.gz'
    default_dir = os.getcwd()


    # input variables determined by user interaction
    arg = input('Would you like to [c]ompress or e[x]tract a tar archive?\n>> ')
    location = input('Please enter the (abs) path to the location which contains the file(s) you would like to compress or extract.\n>> ')
    # ask for other input variables if the user hasn't selected 'extract'
    if not arg.lower() == 'x':
        filename = input('Please enter the name of the file archive to be created.\n>> ')
        compression = input('Would you like to use compression type [gz], [bz], or [xz]?\n>> ')
        name = filename + '_' + datetime

    # this variable will have use for the logic i am planning for multiple OS
    # compatibility in the future
    system_type = sys.platform

    # define function to put us in the working directory
    def ch_working_dir():
        '''
        when called, the function will change to the desired directory, and
        list its contents
        '''
        os.chdir(location)
        return os.listdir()

    # define function for compression/creation of tarfile
    def make_tar_file():
        '''
        calling this function calls ch_working dir() creates the desired
        tarfile
        '''
        # tarfile creation variable declaration
        ch_working_dir()
        shutil.make_archive(name, compression + 'tar', location)
        # print confirmation of the file that was created before closing the program
        print(f'The desired tarfile has been created in {location} as {name + ".tar." + compression}.')

    # define function for extraction of tarfile
    def extract_tar_file():
        '''
        calling this function will call ch_working_dir(), list the files in it,
        ask the user for input to determine the file and then extracts the
        desired tarfile
        '''
        print(ch_working_dir())
        # ask user for input after printing the directory contents, so exact filename can be seen before input
        # hopefully lessening the chance of a mistake being made
        filename = input('Please enter the filename that you wish to extract.\n>> ')
        extract_dir = input('Please enter the (abs) path location you wish to extract the archive into (default is the directory in which the file exists).\n>> ')
        shutil.unpack_archive(filename, extract_dir=location)
        # print confirmation of what was done before exiting
        print(f'The file, {filename} was extracted into {extract_dir}.')

    def selected_function(arg):
        '''
        When called, this function will execute the user's preferred function,
        extract or compress
        '''
        if arg.lower() == 'c':
            return make_tar_file()
        elif arg.lower() == 'x':
            return extract_tar_file()
        else:
            print('An incorrect selection was made.')
            raise ValueError

    if arg.lower() == 'c':
        # confirm settings for user
        print(f'Ok, so you chose to tar -{arg}, with location {location} contents being archived, and the final file prefix will be {name}.')
        reply = input('If this is correct, please be sure to enter [y], and if it is incorrect, please enter [n].\n>> ')
        # if confirmation input is not 'y', print message and end program
        if not reply.lower() == 'y':
            print('Please be sure to type more carefully next time.')
            quit()
        # print confirmation of the fact that the file is being created now
        else:
            print(f'The files you selected will be archived into filename {name + ".tar." + compression}.')

    elif arg.lower() == 'x':
        # confirm as above
        print(f'You have chosen tar -{arg} to extract a file that already exists. You will be asked for more input to select preferences momentarily.')
        reply = input('If this is the intended action, please enter [y], otherwise, enter [n].\n>> ')
        # if confirmation input is not 'y', print message and end program
        if not reply.lower() == 'y':
            print('Please be sure to type more carefully next time.')
            quit()

        else:
            print('On with our program then!')
    # try/except clause in case any typos or unintended chars get entered
    try:
        # call selected function
        selected_function(arg)

    # if process completes with exit status other than 0, raise Exception
    except Exception as err:
        print(err)
        quit()

# call main()
if __name__ == '__main__':
    main()
