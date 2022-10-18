#!/bin/bash
read -p "Enter dataset path" fsocoPATH
read -p "Enter new dataset path" newPATH

cd $fsocoPATH

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
