############
### EASY ###
############

# 1
# import os
# print('os.getcwd() = ', os.getcwd())
# for i in range(1,10):
#     dir_name = 'dir_' + str(i)
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.mkdir(dir_path)
#     except FileExistsError:
#         print('Такая директория существует')


# for i in range(1,10):
#     dir_name = 'dir_' + str(i)
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.rmdir(dir_path)
#     except FileExistsError:
#         print('Такой директории не существует')


# 2

# import  os
# get_dir = os.listdir()
# for name in get_dir:
#     if os.path.isdir(name):
#         print(os.path.join(name))


# 3
import  os
import sys
import shutil
script = sys.argv
print(script[0])
print(os.getcwd())
name_script, format_script = str(script[0]).split('.')
copy_script = name_script + '_copy.' + format_script
shutil.copy(script[0], copy_script)




