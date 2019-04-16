#!/usr/bin/env python

import matplotlib.pyplot as plt
import geopandas
import os

def sval_plot(land=True,ice=True,water=False,ax=None):

    if ax == None:
        fig, ax = plt.subplots()

    ax.set_facecolor("#cbecff")

    module_path = os.path.dirname(__file__)
    data_path = 'data/NP_S100_SHP'
    
    if land:
        land_fname = os.path.join(module_path,data_path,
                                  'S100_Land_f_simplified100x.shp')
        land_shp = geopandas.read_file(land_fname)
        land_shp.plot(ax=ax, color="#927d5a", edgecolor="#927d5a", lw=0.5)
    
    if ice:
        ice_fname = os.path.join(module_path,data_path,
                                 'S100_Isbreer_f_simplified100x.shp')
        ice_shp = geopandas.read_file(ice_fname)
        ice_shp.plot(ax=ax,color="#ffffff",edgecolor="#ffffff",lw=0.1)

    if water:
        water_fname = os.path.join(module_path,data_path,
                                   'S100_Vann_f_simplified100x.shp')
        water_shp = geopandas.read_file(water_fname)
        water_shp.plot(ax=ax,color="#0054f0")

    return ax
