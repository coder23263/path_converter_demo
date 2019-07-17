from django.urls import converters,register_converter
#这个类的用处就是在浏览器中url只能为str类型，而reserve传参需要将其他类型变成str类型，
#同理，将url中的字符串中的数据当做参数传入函数运算时需要变成其他相应类型。
#自定义url转换器，在这里我们将 liabi+luban+pangu 一类的字符串和列表之间进行相互转化
class CategoryConverter(object):
	regex = r'\w+|(\w+\+\w+)+'

	def to_python(self, value):
		#将字符串转化为参数
		#libai+luban+pangu
		#['libai','luban','pangu']
		result = value.split("+")
		return result

	def to_url(self, value):
		#反过来，用于reverse反转函数传参
		if isinstance(value, list):
			result = "+".join(value)
			return result
		else:
			raise RuntimeError("转化url的时候，分类参数必须为列表！")
#注册上面写的类
register_converter(CategoryConverter, 'cate')