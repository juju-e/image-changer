from PIL import Image
import os
import sys
def change_images(path_dir,save_to,exists):
   if exists==False:
         os.mkdir(save_to)
   images=os.listdir(path)
   for image in images:
      image_clone=image
      image=Image.open(path+"/"+image_clone)
      if image.size[0]>image.size[1]:
         width=400
         percentage=width/float(image.size[0])
         height=int((float(image.size[1])*float(percentage)))
         img_res=Image.open(path+"/"+image_clone).resize((width,height),Image.ANTIALIAS)
         img_res.save(save_to+"/"+image_clone)
      else:
         height=400
         percentage=height/float(image.size[1])
         width=int((float(image.size[0])*float(percentage)))
         img_res=Image.open(path+"/"+image_clone).resize((width,height),Image.ANTIALIAS)
         img_res.save(save_to+"/"+image_clone)
         height=400
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
