# -*- coding: utf-8 -

import sample
#from . import sample doesnt work

sample.hmm()


print(sample.dummy.dumdum())
print(sample.subsample.test.test())

from sample.subsample.test import test as xmp

print(xmp())