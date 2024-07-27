import sensor, image, pyb

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_contrast(-3)
sensor.skip_frames(100)
sensor.set_hmirror(True)
sensor.set_vflip(True)
P0 = pyb.Pin('P0',pyb.Pin.OUT_PP)#left
P2 = pyb.Pin('P2',pyb.Pin.OUT_PP)#right
roi1 = [0,0,320,60]
roi2 = [0,60,320,60]
roi3 = [0,120,320,60]
roi4 = [0,180,320,60]
P0.value(0)
P2.value(0)
while(True):
   img = sensor.snapshot()
   #img.histeq()#直方图均衡
   img.lens_corr()#畸形矫正
   #img.binary([(9, 27, -17, 6, -5, 17)])
   #img.mean(1, threshold=True, offset=5, invert=True)
   blobs1 = img.find_blobs([(9, 27, -17, 6, -5, 17)],merge=True,roi = roi1,x_stride = 10,y_stride = 40)
   blobs2 = img.find_blobs([(9, 27, -17, 6, -5, 17)],merge=True,roi = roi2,x_stride = 10,y_stride = 40)
   blobs3 = img.find_blobs([(9, 27, -17, 6, -5, 17)],merge=True,roi = roi3,x_stride = 10,y_stride = 40)
   blobs4 = img.find_blobs([(9, 27, -17, 6, -5, 17)],merge=True,roi = roi4,x_stride = 10,y_stride = 40)
   for blob1 in blobs1:
       img.draw_rectangle(blob1.rect(),color=(0,255,0))
       img.draw_cross(blob1.cx(),blob1.cy(),size=5,color=(0,255,0))

   for blob2 in blobs2:
       img.draw_rectangle(blob2.rect(),color=(0,255,0))
       img.draw_cross(blob2.cx(),blob2.cy(),size=5,color=(0,255,0))

   for blob3 in blobs3:
       img.draw_rectangle(blob3.rect(),color=(0,255,0))
       img.draw_cross(blob3.cx(),blob3.cy(),size=5,color=(0,255,0))

   for blob4 in blobs4:
       img.draw_rectangle(blob4.rect(),color=(0,255,0))
       img.draw_cross(blob4.cx(),blob4.cy(),size=5,color=(0,255,0))

   img.draw_line(blob1.cx(),blob1.cy(),blob2.cx(),blob2.cy())
   img.draw_line(blob2.cx(),blob2.cy(),blob3.cx(),blob3.cy())
   img.draw_line(blob3.cx(),blob3.cy(),blob4.cx(),blob4.cy())

   if blob4.cx()>240:
       P2.value(1)#右转
   if blob4.cx()<90:
       P0.value(1)#左转
   if blob1.w()>150 and blob1.w()>blob4.w() and blob1.cx() > blob4.cx():
       P2.value(1)#右转
   if blob1.w()>150 and blob1.w()>blob4.w() and blob1.cx() < blob4.cx():
       P2.value(1)#左转
   elif blob4.cx() and blob1.cx() and blob2.cx() and blob3.cx() >90 and blob4.cx() and blob1.cx() and blob2.cx() and blob3.cx()<240:
       P2.value(0)
       P0.value(0)
