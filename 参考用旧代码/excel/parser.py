from .util import ExcelParseError
_a = (0, '', (), None, None, b'')


def decode_excel(factory_class, parse_config, buffer, array_is_sign=True, excel_mode=True):
	# field
	def h(a, b=True):
		a, c, d = a
		if b:
			b = k[a](*c)
		else:
			if a == 5:
				b = b'\x00' * c[0]
			else:
				b = _a[a]
		if d:
			a, c = d
			if isinstance(a, bool) and (b > 1 or b < 0):
				raise TypeError(f'bool的值为{b}')
			b = a(b, *c)
		return b

	# class
	def f(a, b):
		return a(*(h(*i) for i in zip(b, i(len(b)))))

	# struct
	def e(a, b):
		return a(*(h(i) for i in b))

	# list
	def c(b):
		return tuple((h(b) for _ in range(a(array_is_sign))))

	# string
	def b():
		return bytes(g(a())).decode('utf-8')

	# fixed bytes
	def g(a):
		nonlocal j, l
		l = j
		b = j
		j += a
		return buffer[b:j]

	# varint
	def a(b=False):
		nonlocal j, l
		l = j
		a = c = 0
		while True:
			d = buffer[j]
			j += 1
			c |= (d & 0x7F) << a
			a += 7
			if d & 0x80 == 0:
				if b:
					c = (c>>1) ^ -(c&1)
				return c

	# bit mask
	def i(b):
		c = a()
		for _ in range(b):
			yield c & 1
			c >>= 1
		if c:
			raise TypeError("field flags don't match field number")

	def excel_iter():
		for _ in range(a(array_is_sign)):
			data = f(factory_class, parse_config)
			yield data

	buffer = memoryview(buffer)
	# 兼容星穹铁道
	j = l = 1 if buffer[0] == 0 and len(buffer) > 2 else j = l = 0

	k = (a, b, c, e, f, g)
	try:
		return excel_iter() if excel_mode else f(factory_class, parse_config)
	except Exception as exc:
		from traceback import print_exception
		print_exception(exc)
		raise ExcelParseError(e, j, l)
