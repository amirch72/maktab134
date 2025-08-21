import re

# user_input=input("please input your email address .. ")
regex_pattern = r"([a-zA-Z0-9\.]{5,20}@[a-zA-Z0-9\-]{5,10}\.(org|ir|com))"
user_input = "niloufar.arab@gmail.gmf.hasani@gmail.com allieh@yahoo.com mahdi.shamkhani1380@gmail.com ghazraz221b@gmail.com"
# test=re.match(regex_pattern,user_input)
# print(test)
# print(True if test else False)
# print( test!=None)
# test = re.findall(regex_pattern, user_input)
# print(test)
# ------------------------------------
import pickle

data = {"ahmad": 32, "hamid": 25, "reza": 30}
# pickle_data = pickle.dumps(data)
# print(pickle_data)
# loaded_data=pickle.loads(pickle_data)
# print(loaded_data)

with open("pickle.b","ab") as f:
    pickle.dump(data,f)

with open("pickle.b","rb") as f:
    loaded_data=pickle.load(f)
print(loaded_data)