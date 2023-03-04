class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def set_width(self,width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return self.width * 2 + self.height *2

	def get_diagonal(self):
		return  ((self.width ** 2 + self.height ** 2) ** .5)

	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		i = 0
		picture = ''
		while i < self.height:
			str = ''
			picture += str.ljust(self.width, '*') + '\n'
			i += 1
		return picture

	def get_amount_inside(self, obj):
		if obj.width > self.width or obj.height > self.height:
			return 0
		width_param = int(self.width / obj.width)
		height_param = int(self.height / obj.height)
		if width_param == 0:
			width_param = 1
		if height_param == 0:
			height_param =1
		return width_param * height_param

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
	def __init__(self, value):
		self.width = value
		self.height = value

	def set_width(self, value):
		self.width = value
		self.height = value

	def set_height(self, value):
		self.width = value
		self.height = value

	def set_side(self, side):
		self.width = side
		self.height = side

	def __str__(self):
		return f'Square(side={self.width})'
