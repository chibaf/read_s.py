import serial, sys, time

class ardser():
  def open_s(self,port,bps,file):
    ser=serial.Serial(port,bps)
    f=open(file,"w")
    print("connected to: " + ser.portstr)
    return(ser,f)
  def read_s(self,ser,f):
    ut = time.time()
    line=ser.readline()
    nums=line.split()
    if len(nums)==3:
      num0=nums[0].strip().decode('utf-8')
      num1=nums[1].strip().decode('utf-8')
      num2=nums[2].strip().decode('utf-8')
      num=[ut,float(num0),float(num1),float(num2)]
    else:
      num=[ut,0.0,0.0,0.0]
    num_str=str(num[0])+","+str(num[1])+","+str(num[2])+","+str(num[3])
    f.write(num_str)
    f.write("\n")
    return(num)
  def close_s(self,ser,f):
    ser.close()
    f.close()
    return
  
  
# how to use
ard=ardser()
ret=ard.open_s(sys.argv[1],sys.argv[2],sys.argv[3])  # port name, bps
while True:
  try:
    num=ard.read_s(ret[0],ret[1])
    print(num)
  except KeyboardInterrupt:
    print("exiting")
    break
ard.close_s(ret[0],ret[1])
