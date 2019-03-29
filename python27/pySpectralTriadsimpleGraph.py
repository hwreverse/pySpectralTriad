"""
Author: 	HWReverse
Twitter: 	@r0_hw aka HWR0
GitHub:		https://github.com/hwreverse/

"""

import serial  
import numpy   
import matplotlib.pyplot as plt  
from drawnow import *  
from serial import Serial

 
spectreData = serial.Serial("COM7", 115200) #Cchange COM7 to the right port - under Linux it will look more like "/dev/ttyACMx"... 
 
spectreReadings = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,] 
defaultYLimit = 1023
 
plt.ion()     
 
 
def doPlot():     
	plt.ylim(0,defaultYLimit)                            
	plt.title('Spectral Response')           
	plt.grid(True)                              
	plt.ylabel('Response ')                          
	plt.plot(spectreReadings, 'ro-', label='Spectral readings')       
	plt.legend(loc='upper left')                
	 
while True:            
	while (spectreData.inWaiting()== 0):        
		pass            
	spectreString = spectreData.readline()
	spectreList = spectreString.split(",")
	if(len(spectreList)==18): # we have 3 x 6 measure points, so ...
		for num, value in enumerate(spectreList,start=0):
			spectreReadings[num]=float(value)
			
		defaultYLimit=max(spectreReadings)+2 # cosmetics , just used to
		drawnow(doPlot)
		
	
