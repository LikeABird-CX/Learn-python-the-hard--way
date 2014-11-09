#-*- coding: utf-8 -*
cars = 100 #There are 100 cars
space_in_a_car = 4.0 #Every car has 4 spaces
drivers = 30#There are 30 drivers
passengers = 90 #There are 90 passengers
cars_not_driven = cars - drivers #有多少辆车没有使用 = 总共车的数量 - 司机的数量
cars_driven = drivers #开车的人的数量 = 司机的数量
carpool_capacity = cars_driven * space_in_a_car #合伙使用汽车的容量 = 开车的人的数量 * 每辆车可以坐4人
average_passengers_per_car = passengers / cars_driven #平均每辆车的乘客 = 乘客人数 / 开车的人的数量


print "there are",cars,"cars available." #输出有多少辆可以使用的车的数量
print "there are only",drivers,"drivers available." #输出只有多少个司机可以开车
print "There will be",cars_not_driven,"empty cars today." #输出今天有多少辆车闲置
print "We can transport",carpool_capacity,"people today." #输出今天我们可以载客多少人
print "We have",passengers,"to carpool today." #我们有多少乘客合伙使用汽车
print "We need to put about",average_passengers_per_car,"in each car." #我们需要每辆车安排多少乘客