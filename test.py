
import serial 
for i in range(0,9):
	try:
		print(f"connecting to COM{i} .........")
		Ser= serial.Serial(f'COM{i}',baudrate=9600,timeout=1)
		Ser.readline()
	except:
		print(f'COM{i} not found')