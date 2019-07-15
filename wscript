#!/usr/bin/python

APPNAME="kyephogyi"
VERSION="0.2"
COPYRIGHT = "Copyright (c) 2008-2019, Khu Oo Reh"
fmap = {
    'regular' : 'uni_dh0.1.ttf',
    'bold' : 'bold_uni.ttf'
}

for s in fmap.keys() :
    f = font(target = process('Kyephogyi-' + s.title() + '.ttf', 
                name('Kyephogyi'),
                cmd('hackos2 -u 100000000000000000000080000000 ${DEP} ${TGT}'),
                cmd('../tools/ttfaddemptyot -t gpos ${DEP} ${TGT}')),
             source = 'source/karenni_' + fmap[s],
             license = ofl('kyephogyi'),
             copyright = COPYRIGHT)
