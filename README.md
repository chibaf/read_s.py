# read_s.py
read serial on raspberry-py

usage: python3 read_s.py "/dev/ttyACM0" 115200

usage: python3 read_s2.py "/dev/ttyACM0" 115200

usage: python3 read_s3.py "/dev/ttyACM0" 115200

usage: python3 read_s4.py "/dev/ttyACM0" 115200

usage: python3 read_s4t.py "/dev/ttyACM0" 115200 "temp.csv"

arg1=port name, arg2=serial speed (bps)

read_s3.py gives subroutines reading serial

read_s4.py gives class reading serial

read_s4t.py gives class reading serial and writing a csv file: time,"1","2","3"
