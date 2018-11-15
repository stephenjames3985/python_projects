#!/usr/bin/env python3

import sys
import os

def main():
    opts = 'zcvf'
    infile = sys.argv[1]
    outfile = sys.argv[2]
    tarfile = 'tar' + opts + infile + outfile

    for file in os.popen(tarfile, mode='w').readline():
        print(file)

if __name__ == '__main__':
    main()
