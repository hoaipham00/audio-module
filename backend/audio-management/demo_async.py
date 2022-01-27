# import asyncio
# import subprocess

# async def upload(src_path_blob, dst_path):
#     try:
#         command = f'gsutil -o GSUtil:parallel_composite_upload_threshold=100M cp {src_path_blob} {dst_path}'
#         subprocess.run(command, shell=True)
#         for i in range(100000):
#             if(i==6000):
#                 print('ahihi')
#             i = i/2


#     except Exception as error:
#         print('Cannot update to db cause ' + repr(error)) 

# async def main():
#     src_path_blob1 = '/home/lenovo/Desktop/convert_audio_2/split_5_seconds/23d7606e-84d6-4547-aa10-79604ffd9ec2_split0033_split.ogg'
#     dst_path1 = 'gs://hoai_try/audio-split/23d7606e-84d6-4547-aa10-79604ffd9ec2_split0033.ogg'
#     src_path_blob2 = '/home/lenovo/Desktop/convert_audio_2/split_5_seconds/23d7606e-84d6-4547-aa10-79604ffd9ec2_split0047_split.ogg'
#     dst_path2 = 'gs://hoai_try/audio-split/23d7606e-84d6-4547-aa10-79604ffd9ec2_split0047.ogg'
#     # Schedule three calls *concurrently*:
#     L = await asyncio.gather(
#         upload(src_path_blob1, dst_path1),
#         upload(src_path_blob2, dst_path2),
#     )
#     print(L)
# asyncio.run(main())


# import asyncio
# import time

# async def say_after(delay, what):
#     asyncio.sleep(delay)
#     print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")

#     say_after(1, 'hello')
#     say_after(2, 'world')

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())

# import subprocess
# import audioread
# from termcolor import colored
# from pydub import AudioSegment

# # command = 'cp -a /home/lenovo/Desktop/convert_audio_2/music/88fa885b-edb6-4fa9-a824-c030c56b8de6_split_4.ogg //home/lenovo/Desktop/convert_audio_2/convert_to_ogg'
# # subprocess.run(command, shell=True)

# src_path = '/home/lenovo/Desktop/convert_audio_2/music/76ef627a-c064-47aa-a05c-45b6ab29dcfc_split0017.ogg'
# dst_path = 

# def audio_cutter(src_path, dest_path, start_seconds, end_seconds):
#     f =  audioread.audio_open(src_path)    
#     duration = f.duration*1000

#     if( start_seconds >= end_seconds):
#         print(colored("start_time is greater than end_time, please check again", "red"))
#     elif(start_seconds < 0):
#         print('Invalid params, please check again')
#         print(colored("Working in processing.....", "red"))
#         return
#     else:
#         print(colored("Working in processing.....", "yellow"))
#         #to miliseconds
#         startTime = start_seconds*1000 - 50
#         if (startTime <= 0):
#             startTime = 0
#         endTime = end_seconds*1000 + 50
#         if(endTime > duration):
#             endTime = duration - 5 
#         song = AudioSegment.from_file(src_path)
#         extract = song[startTime:endTime]
#         extract.export(dest_path, format="ogg")


from flask import Flask
from flask_pymongo import PyMongo

user_name = "myuser"
pass_word = "1234"  

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://myUserAdmin:1234@34.123.74.23:27017/amdin"
mongo = PyMongo(app)
online_users = mongo.db.metadata.find({'owner': 'hoaipham'})
# for i in online_users:
    # print(i)
# print(online_users)