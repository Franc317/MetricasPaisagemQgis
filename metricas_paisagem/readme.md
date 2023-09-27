This is an experimental plugin written for Qgis version 3.22.16-Białowieża. The purpose of this plugin is to 
calculate common landscape metrics used in field ecology and related areas. 

As the plugin is still experimental a StopIteration error occurs while running all radiobuttons simultaneously, this
is perhaps the next step in the plugin imporvement, besides adding other landscape metrics. 

The plugin works as follows: the user creates a Qgis projetc, loads a raster layer upon which metrics will be calculated. Next,
a polygon type vector layer is manually created by the user over this raster selecting fragments from
the desired class (Unfortunatelly, only a single class is supported right now). The metrics will be calculated based on the shapefile generated, but in 
order for the plugin to work properly the raster layer must be selected as the active layer. The user then loads the dialog box from the Plugins Menu and
selects a .txt file where the data will be written to. 

Next, the metrics to be chosen have to be run one at at time and this the weak point to whcih improvements have to be made, as stated before. The file containing
the data has to be placed in the same directory of the metricas_paisagem.py main module. 

Be sure to input 0 value to the No data field by accessing the raster layer: properties -> transparency. This is very important, as i don't know if the no
data values are taken into account when performing the calculations. 

