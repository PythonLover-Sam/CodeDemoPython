from pyfirmata import Arduino,util
import time
board = Arduino('COM4') 
while 1: 	
	board.digital[13].write(0) #向端口13写入0   0代表灭灯 	
	time.sleep(0.1) 	
	board.digital[13].write(1) #向端口13写入1   1代表亮灯 	
	time.sleep(0.1)
