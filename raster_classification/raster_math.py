import pystac
items = pystac.ItemCollection.from_file("data/geospatial-python-raster-dataset/search.json")

red_uri = items[1].assets["red"].href
nir_uri = items[1].assets["nir08"].href

import rioxarray
red = rioxarray.open_rasterio(red_uri, masked=True)
nir = rioxarray.open_rasterio(nir_uri, masked=True)

bbox = (629_000, 5_804_000, 639_000, 5_814_000)
red_clip = red.rio.clip_box(*bbox)
nir_clip = nir.rio.clip_box(*bbox)

red_clip.plot(robust=True)

nir_clip.plot(robust=True)

print(red_clip.shape, nir_clip.shape)

red_clip_matched = red_clip.rio.reproject_match(nir_clip)
print(red_clip_matched.shape)

ndvi = (nir_clip - red_clip_matched)/ (nir_clip + red_clip_matched)
print(ndvi)

ndvi.plot()

ndvi.plot.hist()

ndvi_nonan = ndvi.interpolate_na(dim="x")
ndvi_nonan.rio.to_raster("NDVI.tif")