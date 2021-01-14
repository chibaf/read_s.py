import serial, sys, time, struct

def open_s(port,bps):
  ser=serial.Serial(port, bps)
  print("connected to: " + ser.portstr)
  time.sleep(1)
  return(ser)
def read_s(ser):
  line=ser.readline()
  nums=line.split()
  if len(nums)==3:
    num0=nums[0].strip().decode('utf-8')
    num1=nums[1].strip().decode('utf-8')
    num2=nums[2].strip().decode('utf-8')
    num=[float(num0),float(num1),float(num2)]
  else:
    num0=nums[0].strip().decode('utf-8')
    num=[float(num0),0.0,0.0]
#  num=float(nums1[0],nums1[1],nums1[2])
  return(num)
def close_s(ser):
  ser.close
  
#ser = serial.Serial(
#    port=strPort,\
#    baudrate=sys.argv[2],\
#    parity=serial.PARITY_NONE,\
#    stopbits=serial.STOPBITS_ONE,\
#    bytesize=serial.EIGHTBITS,\
#        timeout=0)
ser=open_s(sys.argv[1],sys.argv[2])

while True:
  num=read_s(ser)
  print(num)
