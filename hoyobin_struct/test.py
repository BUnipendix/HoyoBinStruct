from timeit import timeit
from dataclasses import dataclass
from random import randint, randbytes
from collections import namedtuple


def test_namedtuple_dataclass():
	def gen_data():
		return randbytes(16), randint(0,100000), randbytes(16), randint(0,100000), randbytes(16), randint(0,100000)
	@dataclass
	class DataClass:
		a: bytes
		b: int
		c: bytes
		d: int
		e: bytes
		f: int

	def test_fetch(class_obj):
		class_obj = class_obj(*gen_data())
		return class_obj.a, class_obj.b, class_obj.c, class_obj.d, class_obj.e, class_obj.f

	def test_fetch_named_tuple(class_obj):
		class_obj = class_obj(*gen_data())
		return class_obj[0], class_obj[1], class_obj[2], class_obj[3], class_obj[4], class_obj[5]

	NamedTuple = namedtuple("NamedTuple", "a b c d e f")
	print("namedtuple:", timeit("test_fetch_named_tuple(NamedTuple)", globals=locals()))
	print("dataclass:", timeit("test_fetch(DataClass)", globals=locals()))




def test_fetch_speed():
	@dataclass
	class A:
		a: int
		b: int
		c: int
		d: int
		e: int
		f: int

	def test2():
		def set(a1, b1, c1, d1, e1, f1):
			co.a = a1
			co.b = b1
			co.c = c1
			co.d = d1
			co.e = e1
			co.f = f1

		co = A(0, 0, 0, 0, 0, 0)
		return set

	def test1():
		def set(a1, b1, c1, d1, e1, f1):
			nonlocal a, b, c, d, e, f
			a = a1
			b = b1
			c = c1
			d = d1
			e = e1
			f = f1

		a = 0
		b = 0
		c = 0
		d = 0
		e = 0
		f = 0
		return set

	print("nonlocal:", timeit("set(*([randint(0, 10000)]*6))", globals={"set": test1(), "randint": randint}))
	print("class:", timeit("set(*([randint(0, 10000)]*6))", globals={"set": test2(), "randint": randint}))

if __name__ == '__main__':
	test_namedtuple_dataclass()