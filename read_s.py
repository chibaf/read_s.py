import serial, sys

strPort = sys.argv[1]

#ser = serial.Serial(
#    port=strPort,\
#    baudrate=sys.argv[2],\
#    parity=serial.PARITY_NONE,\
#    stopbits=serial.STOPBITS_ONE,\
#    bytesize=serial.EIGHTBITS,\
#        timeout=0)

ser=serial.Serial(strPort, sys.argv[2])

print("connected to: " + ser.portstr)
count=1

while True:
  line = ser.readline()
  print(line)
  count = count+1

ser.close()
