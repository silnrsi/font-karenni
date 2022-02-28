#!/usr/bin/python3

APPNAME="karenni"
VERSION="1.3"
BUILDVERSION=''

for s in ('regular', 'bold'):
    f = font(target = process('Karenni-' + s.title() + '.ttf', 
                name('Karenni'),
                cmd('hackos2 -u 100000000000000000000080000000 ${DEP} ${TGT}'),
                cmd('../tools/ttfaddemptyot.py -t gpos ${DEP} ${TGT}')),
             source = 'source/Karenni-' + s.title() + '.ttf',
             version = 1.3,
             )
