from struct import Struct
from functools import partial
from fxpmath import Fxp


def a(data):
	return Struct('=f').unpack(data)[0]


def b(data):
	return Struct('=d').unpack(data)[0]


c = partial(Fxp, n_word=64, n_frac=32, raw=True)


class ExcelParseError(Exception):
	def __init__(self, e, pos, last_pos):
		super().__init__(f'解码错误: {e}, 指针位置：{pos}, 上一次指针位置：{last_pos}')
		self.raw_exc = e
		self.pos = pos
		self.last_pos = last_pos
