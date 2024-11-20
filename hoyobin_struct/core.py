

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

	def read_bytes(n):
		nonlocal pos
		old_pos = pos
		pos += n
		return buffer[old_pos: pos]

	buffer = memoryview(data)
	pos = 0
	return read_varint, read_bytes