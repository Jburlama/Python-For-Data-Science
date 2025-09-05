ft_list = ["Hello", "tata!"]  # Ordered, mutable and indexable
ft_tuple = ("Hello", "toto!") # Orderd, imutable and indexable
ft_set = {"Hello", "tutu!"}   # Unordered, mutable and unique
ft_dict = {"Hello" : "titi!"} # Unordered, mutable, and key-value-pair

ft_list[1] = "World!"
ft_tuple = ("Hello", "Portugal!")
ft_set.remove("tutu!")
ft_set.add("Porto!");
ft_dict["Hello"] = "42Porto!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
