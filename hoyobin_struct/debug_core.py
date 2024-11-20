from .core import _read_float, _read_double


def _build_base_reader(data):
	def read_varint():
		nonlocal pos
		num = 0
		shift_bit_num = 0
		while True:
			byte_unit = buffer[pos]
			pos += 1
			num |= (byte_unit & 0x7F) << shift_bit_num
			if byte_unit & 0x80 == 0:
				return num
			shift_bit_num += 7

	def read_bytes(n: int):
		nonlocal pos
		old_pos = pos
		pos += n
		return buffer[old_pos: pos]

	def read_float():
		nonlocal pos
		ret = _read_float(buffer, pos)
		pos += 4
		return ret

	def read_double():
		nonlocal pos
		ret = _read_double(buffer, pos)
		pos += 8
		return ret

	def read_pos():
		return pos

	buffer = memoryview(data)
	pos = 0
	return read_varint, read_bytes, read_float, read_double, read_pos


