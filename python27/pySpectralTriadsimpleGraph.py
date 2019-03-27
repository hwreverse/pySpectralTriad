import serial  
import numpy   
import matplotlib.pyplot as plt  
from drawnow import *  
from serial import Serial

 
spectreData = serial.Serial("COM7", 115200) 
 
spectreReadings = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,] 
defaultYLimit = 1024
 
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
	if(len(spectreList)==18):
		for num, value in enumerate(spectreList,start=0):
			spectreReadings[num]=float(value)
			
		defaultYLimit=max(spectreReadings)+2
		drawnow(doPlot)
		
	
