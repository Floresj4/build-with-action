import os, sys

if __name__ == '__main__':
    print('Build with actions python script started...')
    print('\t{}'.format(os.getenv('env_secret', 'unset')))
    print('\t{}'.format(sys.argv))