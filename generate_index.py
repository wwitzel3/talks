def main(args):
    if len(args) != 2:
        print "Error: please supply output file name"
        return -1
    output_file = args[1]
    import glob
    files = glob.glob('*.html')

    with open(output_file, 'w') as fp:
        for f in files:
            if f != output_file:
                fp.write('<a href="%s">%s</a>\n' % (f, f))


if __name__ == '__main__':
    import sys
    main(sys.argv)
