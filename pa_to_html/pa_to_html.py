#!/usr/bin/env python3

##################################
# Document specific word->html   #
# parser for Politics & Animals. #
##################################

import sys
import os
import mammoth
from lxml import etree, html

def clean_html(f,m):

    _r = mammoth.convert_to_html(f,style_map=m)
    _dr = html.fromstring(_r.value)

    # add 'word' class at top
    _dr.xpath('//div')[0].attrib['class'] = 'wordsection1'

    _r.value = etree.tostring(_dr, encoding='unicode', pretty_print=True).encode('ascii', 'xmlcharrefreplace')
    _r.value = _r.value.decode('utf-8')

    return(_r)

if __name__ == "__main__":

    # stylemap
    _sf = './style.map'

    try:
        with open(_sf, 'r') as _smf:
            m = _smf.read()
    except:
        print("Don't forget your {}".format(_sf))

    if sys.argv and len(sys.argv) == 2:
        _f = sys.argv[1]
        if os.path.exists(_f):
            try:
                with open(sys.argv[1], 'rb') as f:
                    sf = "{}-clean.html".format(os.path.splitext(sys.argv[1])[0])
                    with open(sf, 'w') as _f:

                        cleaned = clean_html(f,m)
                        _f.write(cleaned.value)

                        # add to style.map
                        print("Done!.. Saved to: {}".format(sf))
                        print("\nAnything you need to add to your style.map?:")
                        for m in cleaned.messages:
                            print("{}: {}".format(m.type,m.message))

            except:
                print("Problem cleaning file.")
        else:
            print("File does not exist: '{}'".format(_f))
    else:
        print("{} [file]".format(sys.argv[0]))
        sys.exit(1)
