"""
Data are often more interesting and powerful when we compare them across various locations. Let’s compare the computed NDVI map with the one of another region in the same Sentinel-2 scene: the Texel island, located in the North Sea.

You should have the red- and the NIR-band rasters already loaded (red and nir variables, respectively).
Crop the two rasters using the following bounding box: (610000, 5870000, 630000, 5900000). Don’t forget to check the shape of the data, and make sure the cropped areas have the same CRSs, heights and widths.
Compute the NDVI from the two raster layers and check the max/min values to make sure the data is what you expect.
Plot the NDVI map and export the NDVI as a GeoTiff.
Compare the distributions of NDVI values for the two regions investigated.
"""