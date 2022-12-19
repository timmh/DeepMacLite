#!/bin/sh

wget --content-disposition -P "$(dirname $0)" --no-check-certificate https://download.tensorflow.org/models/object_detection/tf2/20210329/deepmac_1024x1024_coco17.tar.gz