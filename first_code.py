username = "Reem Sami AbuMettleq"
first_index = username.find(" ")
first_name = username[0:first_index]
second_index = username.find(" " , first_index + 1)
second_name = username[first_index + 1:second_index]
third_name = username[second_index + 1:]

print(third_name)