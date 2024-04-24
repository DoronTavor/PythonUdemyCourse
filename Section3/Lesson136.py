class SuperList(list):
    def __len__(self):
        return 1000



super_lst1= SuperList()
print(len(super_lst1))
super_lst1.append(5)
print(super_lst1[0])
print(issubclass(SuperList,list))