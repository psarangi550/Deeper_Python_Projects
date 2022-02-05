from tqdm import tqdm
import time
# for i in tqdm(range(100)):
#     time.sleep(0.5)

#bigger size of the content by using mcols
# for i in tqdm(range(100),ncols=100):
#     time.sleep(0.5)

#display output as disabled
# for i in tqdm(range(100),ncols=100,disable=True):
#     time.sleep(0.1)
#now displaying the 3 sec time interval  for each iteration with in the tqdm
for i in tqdm(range(100),ncols=100,mininterval=3):
    time.sleep(0.1)


# # tqdm integration with request module
# from tqdm import tqdm
# import time
# import requests
# resp=requests.get("https://imgs.xkcd.com/comics/angular_momentum.jpg")
# chunck_size=1
# # # print(resp.headers)
# total_size=int(resp.headers["Content-Length"])
# # print(total_size)
# # print(type(total_size))
# with open("prateek.png","wb") as xkcd:
#     for data in tqdm(resp.iter_content(chunck_size,total_size),total=500,desc="Downloading Images",unit='b',mininterval=2):
#         xkcd.write(data)
