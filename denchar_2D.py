#################################################################################
########################## GETTING 2D PLOT OF DENCHAR ###########################
######################      By Omar Hernández Montes     ########################
######################          24 MAY 221             #########################
#
# Verify you've installed the python libraries numpy & matplotlib
# You will run this program from 'getting_2d_denchar.sh' script:
#                   ./getting_2d_denchar.sh
# Ensure you've modified the 'label' var in 'getting_2d_denchar.sh' script.
#################################################################################
#
import math
import numpy as np
import matplotlib.pyplot as plt
#############This will store variables in one array named "coord"###############
N=NPOINTS 
ydum=[]
coord=np.array(np.zeros([N,3]),dtype=np.float64) #it's necessary change dimensionality
filex = 'filename_denchar.scf'
fic = open(filex,"r+")
fic.seek(0)
for linea in fic.readlines():
    ydum.append(linea.replace('\n',''))
fic.close()
for m in range(len(ydum)):
    w=[float(x) for x in ydum[m].split(',')]
    coord[m,:]=w
ydum.clear() 
########################### G R A P H ##################################
x2=filex.replace('_denchar.scf','')
x = coord[:,0]
y = coord[:,1]
rho = coord[:,2]
cmax=max(coord[:,2])
cmin=min(coord[:,2])
cm = plt.cm.get_cmap('RdBu')
plt.figure(figsize=[20,15])
sc = plt.scatter(x, y, c=rho, vmin=cmin, vmax=cmax, s=1, cmap=cm)
plt.colorbar(sc)
plt.axis('scaled')
plt.xlabel('x')
plt.ylabel('y')
plt.title(x2, fontsize=20)
#plt.savefig(str(x2)) # uncomment if you want to save the plot in a png file
plt.show()
