import csv
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plotting():
    city=[]
    df = pd.read_csv('worldcities.csv')
    df1=pd.read_csv('disaster_tweets.csv')
    for i in (df1['location']):
        if(type(i)==str):
            city.append(i.split(',')[0])
    
    #print(city)
    # plot the blank world map
    plt.figure(figsize=(18,12))
    my_map = Basemap(projection='merc', lat_0=0, lon_0=-100,resolution = 'l', area_thresh = 5000.0,llcrnrlon=-140, llcrnrlat=-55,
                         urcrnrlon=160, urcrnrlat=70)
    # set resolution='h' for high quality 
    # draw elements onto the world map
    my_map.drawcountries()
    my_map.drawstates()
    my_map.drawmapboundary(fill_color='#3ca9fb')
    my_map.fillcontinents(color='#044372',lake_color='#3ca9fb')

    my_map.drawcoastlines(antialiased=False,linewidth=0.005)
     
    # add coordinates as red dots
    #longs = list(df.loc[(df.long != 'NaN')].long)
    latts=list(df['lat'])
    longs=list(df['lng'])
    cities=list(df['city'])
    lat=[]
    lon=[]
    for c in city:
        if c in cities:
            #print(c)
            index=cities.index(c)
            lat.append(latts[index])
            lon.append(longs[index])
    
    x, y = my_map(lon, lat)
    my_map.plot(x, y, 'ro', markersize=4, alpha=0.5)
    plt.show()
    
