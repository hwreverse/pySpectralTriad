import serial  
import numpy   as np
import matplotlib.pyplot as plt  
from drawnow import *  
from serial import Serial
from scipy.interpolate import interp1d
 
spectreData = serial.Serial("COM7", 115200) 
 
spectreReadings = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,] 
x = np.linspace(0, 17, num=18, endpoint=True)
defaultYLimit = 1024
xnew = np.linspace(0, 17, num=200, endpoint=True) 
plt.ion()     
 
 
def doPlot():     
	plt.ylim(0,defaultYLimit)                            
	plt.title('Spectral Response')           
	plt.grid(True)                              
	plt.ylabel('Response ')                          
	#plt.plot(spectreReadings, 'ro-', label='Spectral readings')       
	plt.plot(x, spectreReadings, 'o', xnew, f(xnew), '-')       
	plt.legend(loc='upper left')                
	 
while True:            
	while (spectreData.inWaiting()== 0):        
		pass            
	spectreString = spectreData.readline()
	spectreList = spectreString.split(",")
	if(len(spectreList)==18):
		for num, value in enumerate(spectreList,start=0):
			spectreReadings[num]=float(value)
			
		defaultYLimit=max(spectreReadings)*1.3 # thus, the cubic spline should remain inside the plotarea
		f=interp1d(x,spectreReadings,kind='cubic')

		drawnow(doPlot)
		
	
	
	