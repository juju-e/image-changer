from PIL import Image
import os
import sys
def change_images(path_dir,save_to,exists):
   if exists==False:
         os.mkdir(save_to)
   images=os.listdir(path)
   for image in images:
      img_res=Image.open(path+"/"+image).resize((400,400),Image.ANTIALIAS)
      img_res.save(save_to+"/"+image,quality=20,optimize=True)
   print("[***]finished[***]")
path=input("[*]enter the path of the files to change----->>")
save_dir=input("[#]enter the name of the directory the files will be saved to------>>")
if (os.path.exists(save_dir)):
   print("[/**]path already exists do you want to save the files here??--->>")
   d=input()
   if d=='yes':
       change_images(path,save_dir,True)
   else:
      sys.exit()
else:
    change_images(path,save_dir,False)
