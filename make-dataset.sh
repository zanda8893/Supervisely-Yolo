#!/bin/bash
origin = $(pwd)
read -p "Enter dataset path" fsocoPATH
read -p "Enter new dataset path" newPATH

cd $fsocoPATH

python3 $origin/main.py --no-interactive

mkdir -p $newPATH{images,images_val,labels}

cp $fsocoPATH/*/img/* $newPATH/images

cp $fsocoPATH/*/ann/* $newPATH/labels

cd $newPATH

ls images | shuf -n 1152 > randomset

for f in $(cat randomset); do
    mv images/$f images_val;
done

sed -i -e 's/jpg/txt/g' randomset

while read f; do
    mv labels/$f images_val/;
done < randomset

rm randomset

cd ..

git clone https://github.com/ultralytics/yolov5

cd yolov5

python3 train.py --img 640 --batch 16 --epochs 3 --data $newPATH/dataset.yaml --weights yolov5s.pt
