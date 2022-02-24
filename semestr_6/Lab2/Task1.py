import sys


def main(args):
    sort = 0
    Dicts = dict()
    while args:
        arg = args.pop(0)
        if arg == '--sort':
            sort = 1
        else:
            s = arg.find("=")
            Dicts[arg[0:s]] = arg[s+1:]
    if sort == 1:
        Dicts = dict(sorted(Dicts.items(), key=lambda x: x[0]))
    for dic in Dicts:
        print("Key: "+dic+" Value: "+Dicts[dic])


main(sys.argv[1:])
