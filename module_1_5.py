immutable_var = tuple_ = ("date", "month", 20, 10, 20.24)
print(immutable_var)
# immutable_var.extand("date") # не расширяет список, путем разбивки слово "дата" на символы: 'd', 'a', 't', 'e'
print(immutable_var)
# immutable_var.remove(20.24) # не удаляет число float
print(immutable_var)
print(immutable_var[::-1])
# immutable_var[-1] = 2024 # не действует метод замены
print(immutable_var)
mutable_list = ["date", "month", 20, 10, 20.24]
mutable_list.extend("date")
print(mutable_list)
mutable_list = ["date", "month", 20, 10, 20.24]
mutable_list.remove(20.24)
print(mutable_list)
print(mutable_list[::-1])  # почему в кортеже выводит 20.24, а здесь нет???
mutable_list[-1] = 2024
print(mutable_list)
