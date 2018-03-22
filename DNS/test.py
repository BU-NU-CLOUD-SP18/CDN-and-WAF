#!/usr/bin/env python3

import itertools
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))
cacheServerIPs = ["128.31.26.6","128.31.25.244","128.31.26.50"]
# iterList = itertools.cycle(cacheServerIPs)
iterList = roundrobin(cacheServerIPs)
print(len(cacheServerIPs))
