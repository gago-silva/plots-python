from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

m = Basemap(llcrnrlon=90.,llcrnrlat=-60.,urcrnrlon=180.,urcrnrlat=10.,
            resolution='l',projection='stere',
            lat_0=0,lon_0=133.)
m.shadedrelief()
#Title and text
plt.title("Title")
plt.figtext(.1,.5,'Other text 1',fontsize=12,ha='center')
plt.figtext(.9,.5,'Other text 2',fontsize=12,ha='center')
plt.figtext(.5,.0,'Other text 3',fontsize=12,ha='center')
plt.show()
