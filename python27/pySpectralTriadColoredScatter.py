"""
Author: 	HWReverse
Twitter: 	@r0_hw aka HWR0
GitHub:		https://github.com/hwreverse/

"""

import serial  
import numpy   as np
import matplotlib.pyplot as plt  
import matplotlib.colors
from drawnow import *  
from serial import Serial
from scipy.interpolate import interp1d, InterpolatedUnivariateSpline
 
spectreData = serial.Serial("COM7", 115200) # replace by your real comport, on Linux it is something like "/dev/ttyACMx"
spectreData.reset_input_buffer()
resolution = 1000



loop=True

mp=interp1d([410,610,680,730,760,860,940],[0,8,10,12,13,15,17]) #mapping the sensor wavelenghts to the linear space (sometimes delta=25 sometimes 35 or 50...
 
spectreReadings = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]
spectreWavelenghts =[410,435,460,485,510,535,560,585,610,645,680,705,730,760,810,860,900,940] 
x = np.linspace(0, 17, num=18, endpoint=True)
xNew = np.linspace(0, 17, num=resolution, endpoint=True)
defaultYLimit = 1024
wLspace = np.linspace(410, 940, num=resolution, endpoint=True) 
# ----------------------------------------------------------
norm = matplotlib.colors.Normalize(380,940)
colors = [[norm(380), "black"], # so 410nm looks better
		  [norm(405), "indigo"],
          [norm(427), "midnightblue"],
		  [norm(435), "darkblue"],
          [norm(460), "blue"],
		  [norm(487), "cyan"],
		  [norm(510), "green"],
		  [norm(520), "darkgreen"],
		  [norm(570), "gold"],
		  [norm(585), "orange"],
		  [norm(610), "orangered"],
		  [norm(640), "red"],
		
		  [norm(670), "darkred"],
	
		  [norm(690), "maroon"],
		  [norm(720), "black"],
		  [norm(940), "black"]]

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

fig,ax=plt.subplots() 	

plt.ion()   
  
def handle_close(evt):
	spectreData.reset_input_buffer()
	plt.ioff()
	plt.close()
	global loop
	loop=False
	#print("close event")
	#exit()
	#sys.exit()

def doPlot(): 
	


	fig.canvas.mpl_connect('close_event', handle_close) # figured out finally how to close the "groundhog" window

	
	plt.ylim(0,defaultYLimit)                            
	plt.title('Spectral Response')           
	plt.grid(True)                              
	plt.ylabel('28.6 nW/cm2/count')
	plt.xlabel('Wavelenght in nm')
	plt.xrange=[410,940]
    
	plt.legend(loc='upper left')                

	plt.scatter(wLspace,f(mp(wLspace)), c=wLspace, norm=norm, cmap=cmap)
	sc = ax.scatter(wLspace,f(mp(wLspace)), c=wLspace, norm=norm, cmap=cmap)
	fig.colorbar(sc, orientation="horizontal")
	#plt.draw()	
	plt.show() 
	
while (loop):            
	while (spectreData.inWaiting()== 0):        
		pass            
	spectreString = spectreData.readline()
	spectreList = spectreString.split(",")
	
	if(len(spectreList)==18):
		for num, value in enumerate(spectreList,start=0):
			spectreReadings[num]=float(value)
			
		defaultYLimit=max(spectreReadings)*1.1 # univariatespline is not a cubic one and WILL stay inside the plot area, at least at the top
		
		#f=interp1d(x,spectreReadings,kind='cubic')
		f=InterpolatedUnivariateSpline(x,spectreReadings)

		drawnow(doPlot)
	

print(".")
	
