#!/usr/bin/env python3

import sys
import os

def main():
    opts = 'zcvf'
    infile = sys.argv[1]
    outfile = sys.argv[2]
    tarfile = 'tar', ({0}, {1}, {2}).format(opts, infile, outfile)

    for file in os.execv(tarfile, mode='w').readline():
        print(file)

if __name__ == '__main__':
    main()
