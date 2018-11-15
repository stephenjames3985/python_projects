#!/usr/bin/env python3

import sys
import os

def main():
    opts = 'zcvf'
    infile = sys.argv[1]
    outfile = sys.argv[2]
    tarfile = 'tar'
    args = sys.argv[1:]

    for file in os.execv(tarfile, args).readline():
        print(file)

if __name__ == '__main__':
    main()
