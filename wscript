#!/usr/bin/python

APPNAME="karenni"
VERSION="1.3"
COPYRIGHT = "Copyright (c) 2008-2019, Khu Oo Reh"
fmap = {
    'regular' : 'uni_dh0.1.ttf',
    'bold' : 'bold_uni.ttf'
}
BUILDVERSION=''

for s in fmap.keys() :
    f = font(target = process('Karenni-' + s.title() + '.ttf', 
                name('Karenni'),
                cmd('hackos2 -u 100000000000000000000080000000 ${DEP} ${TGT}'),
                cmd('../tools/ttfaddemptyot -t gpos ${DEP} ${TGT}'),
                name("Version 1.3", string=5)),
             source = 'source/karenni_' + fmap[s],
             version = 1.3,
             license = ofl(),
             copyright = COPYRIGHT)
