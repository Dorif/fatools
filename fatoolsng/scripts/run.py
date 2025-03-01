import sys
import importlib


def greet():
    print('fatoolsng - Python-based DNA fragment-analysis tools')


def usage():
    print('Usage:')
    print('\t%s command [options]' % sys.argv[0])
    sys.exit(0)


def main():
    greet()
    if len(sys.argv) >= 3:
        command = sys.argv[1]
        opt_args = sys.argv[2:]
        print('Running command: %s' % command)
        try:
            M = importlib.import_module('fatoolsng.scripts.' + command)
        except ImportError:
            print('Cannot import script name: %s' % command)
            raise
        parser = M.init_argparser()
        args = parser.parse_args(opt_args)
        M.main(args)
    else:
        print('Insufficient arguments. Please, read fatoolsng manual.')
        sys.exit(1)
