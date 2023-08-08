#! /usr/bin/bash

wget https://figshare.com/ndownloader/files/36028100 geospatial-python-raster-dataset.tar.gz

mkdir data && tar -zxvf geospatial-python-raster-dataset.tar.gz --directory /data

rm geospatial-python-raster-dataset.tar.gz