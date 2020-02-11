import requests
from bs4 import BeautifulSoup
import json
from matplotlib import pyplot


url = 'https://api.heweather.net/s6/weather/now?location=tianjin&key=089a7047f17e406ab382bfc9c6559e23'
url_hourly = 'https://api.heweather.net/s6/weather/hourly?location=tianjin&key=b5b8aa5195884c06a7a63f5bd6dcf1c7'
"""
webpage = requests.get(url)
#webpage = urlopen('https://free-api.heweather.net/s6/weather/now?location=beijing&key=b5b8aa5195884c06a7a63f5bd6dcf1c7')

soup = BeautifulSoup(webpage.text, 'lxml')



tag = soup.p.get_text()

data = json.loads(tag)

# 抓取当前气温

head = data["HeWeather6"]
body1 = head[0]['basic']['location']
body2 = head[0]['update']['loc']
body3 = head[0]['now']['cond_txt']
body4 = head[0]['now']['tmp']
body5 = head[0]['now']['fl']

output = "地区：{0}， 更新日期：{1}， 天气状况：{2}， 实际气温：{3}， 体感气温：{4}".format(body1, body2, body3, body4, body5)
print(soup.prettify())

#print(soup.p)
#print(webpage.read().decode('UTF-8'))  """
hourly_data_list = []
basic_info_list = []

def get_hourly_data(url, hourly_data_list, basic_info_list):

	"""获取每小时的天气数据 返回一个列表"""

	webpage = requests.get(url)

	soup = BeautifulSoup(webpage.text, 'lxml')
	data = json.loads(soup.p.get_text())  # 获取和风天气返回数据的p标签的内容
	head = data["HeWeather6"]
	body = head[0] # 返回天气数据HeWeather6对应的值为一个只含有一个元素的列表
	basic_info = body["basic"] # 基本信息字典的值，数据类型仍为字典，返回地区代号、经纬度、地区名、时区等
	update_info = body["update"] # 返回更新时间loc格式和utc格式 数据类型字典
	status_info = body["status"] # 返回获取状态，只要其他内容成功获取，此处一定是ok否则报错，未来需要异常处理
	hourly_info_list = body["hourly"] # 返回每小时的天气数据，返回类型为一个列表，列表有24个元素，为一个字典类型

	basic_info_list.append(basic_info["location"]) # 添加地区名
	basic_info_list.append(basic_info["lon"]) # 添加地区经度
	basic_info_list.append(basic_info["lat"]) # 添加地区纬度
	basic_info_list.append(update_info["loc"]) # 添加更新时间 24小时制
	for i in range(24):
		temp = []
		temp.append(int(hourly_info_list[i]["cloud"])) # 添加云量 int型 0-100?
		temp.append(hourly_info_list[i]["cond_txt"]) # 添加当前天气中文描述
		temp.append(int(hourly_info_list[i]["hum"])) # 添加相对湿度
		temp.append(int(hourly_info_list[i]["pop"])) # 添加降水概率
		temp.append(int(hourly_info_list[i]["pres"])) # 添加大气压强
		temp.append(hourly_info_list[i]["time"]) # 添加预报时间
		temp.append(int(hourly_info_list[i]["tmp"])) # 添加温度
		temp.append(hourly_info_list[i]["wind_deg"]) # 添加风向角度
		temp.append(hourly_info_list[i]["wind_dir"]) # 添加风向中文描述
		temp.append(hourly_info_list[i]["wind_sc"]) # 添加风力
		temp.append(int(hourly_info_list[i]["wind_spd"])) # 添加风速 公里每小时

		hourly_data_list.append(temp) 

if __name__ == '__main__':

	get_hourly_data(url_hourly, hourly_data_list, basic_info_list)

	x = []
	y = []
	z = []
	a = []
	b = []
	for content in hourly_data_list:
		x.append(content[5][-5:-3])
		y.append(content[2])
		z.append(content[6])
		a.append(content[10])
		b.append(content[4])
	print("相对湿度", y, "温度", z, "风速", a)


	pyplot.subplot(2, 2, 1)
	pyplot.plot(x, z, 'o')
	pyplot.title('Temperature')
	pyplot.subplot(2, 2, 2)
	pyplot.plot(x, y, 'o')
	pyplot.title('Wet')
	pyplot.subplot(2, 2, 3)
	pyplot.plot(x, a, 'o')
	pyplot.title('WindSpeed')
	pyplot.subplot(2, 2, 4)
	pyplot.plot(x, b, 'o')
	pyplot.title('AtmosphericPressure')


	pyplot.show()






