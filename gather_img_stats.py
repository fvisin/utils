import numpy as np
import os
from PIL import Image
import subprocess


def get(command):
    return subprocess.check_output(["/bin/bash", "-c", command]).decode(
        "utf-8")


def gather_imgs(directory, m_subject='image', verbose=True):
    total_size = []
    sizes = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            f = os.path.join(root, f)
            mtype = get('file --mime-type "' + f + '"').strip().split(' ')[-1]
            if m_subject in mtype:
                # size = get("du -hk " + file).split()[0]
                # total_size.append(int(size))
                fimg = Image.open(f)
                if verbose:
                    print('{} \t {} \t {}'.format(f, mtype, fimg.size))
                    # size + 'k')
                if fimg.size not in sizes:
                    sizes.append(fimg.size)
    # PRINT
    print("Number of files: {}\n Total size: {}k".format(len(total_size),
                                                         sum(total_size)))
    print('Image sizes: {}'.format(sizes))
    print("Average size: {}".format(np.mean(np.array(sizes), 0)))

    # WRITE LOG
    f = open('img_stats.txt', 'w')
    f.write("Number of files: {}\n Total size: {}k".format(len(total_size),
                                                           sum(total_size)))
    f.write('Image sizes: {}'.format(sizes))
    f.write("Average size: {}".format(np.mean(np.array(sizes), 0)))
    f.close()


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Process some integers.')
    parser.add_argument('directory', default='.',
                        help='an integer for the accumulator')
    parser.add_argument('verbose', action='store_false',
                        help='an integer for the accumulator')
    args = parser.parse_args()
    gather_imgs(args.directory, verbose=args.verbose)
