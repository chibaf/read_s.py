import serial, sys

def open_s(port,bps):
  ser=serial.Serial(port, bps)
  print("connected to: " + ser.portstr)
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
    num=[0.0,0.0,0.0]
  return(num)
def close_s(ser):
  ser.close()
  return
  
  
# how to use
ser=open_s(sys.argv[1],sys.argv[2])  # port name, bps

while True:
  try:
    num=read_s(ser)
    print(num)
  except KeyboardInterrupt:
    print("exiting")
    break
  
close_s(ser)
