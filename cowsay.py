# A python implementation of cowsay <http://www.nog.net/~tony/warez/cowsay.shtml>
# Copyright 2011 Jesse Chan-Norris <jcn@pith.org>
# Licensed under the GNU LGPL version 3.0

# Edited in some places by David Tschida. 

import sys
import textwrap
# To strip whitespace
import re

def cowsay(str, length=40):
    return build_bubble(str, length) + build_cow()

def build_cow():
    return """
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    `````````````````````````````
    """

def build_bubble(str, length=40):
    bubble = []

    # Replace multiple spaces with single space
    # ' '.join(str.split())
    str = re.sub( '\s+',' ', str ).strip()

    lines = normalize_text(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalize_text(str, length):
    lines  = textwrap.wrap(str, length)
    #lines = textwrap.TextWrapper(width=90,break_long_words=False,replace_whitespace=False)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]

    elif index == 0:
        return [ "/", "\\" ]
    
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    
    else:
        return [ "|", "|" ]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: '%s string'" % sys.argv[0]
        sys.exit(0)

    print cowsay(sys.argv[1])
