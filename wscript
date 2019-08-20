#!/usr/bin/python

APPNAME="karenni"
VERSION="1.3"
COPYRIGHT = "Copyright (c) 2008-2019, Khu Oo Reh"
BUILDVERSION=''

for s in ('regular', 'bold'):
    f = font(target = process('Karenni-' + s.title() + '.ttf', 
                name('Karenni'),
                cmd('hackos2 -u 100000000000000000000080000000 ${DEP} ${TGT}'),
                cmd('../tools/ttfaddemptyot -t gpos ${DEP} ${TGT}')),
             source = 'source/Karenni-' + s.title() + '.ttf',
             version = 1.3,
             license = ofl(),
             copyright = COPYRIGHT)
