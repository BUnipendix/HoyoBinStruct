from collections import namedtuple
from enum import IntEnum
from .util import *
MusicSegment = (namedtuple('MusicSegment', ('segment_name', 'short_id', 'end_position')), ((1, (), None), (0, (), None), (5, (4,), (a,()))))
MusicSegments = (namedtuple('MusicSegments', ('segments')), ((2, ((4,MusicSegment,None),), None),))
