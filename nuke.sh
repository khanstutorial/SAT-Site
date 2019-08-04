#!/usr/bin/env bash

rm ./nukeShelter/index.html
rm ./nukeShelter/thankyou.html
cp ./index.html ./nukeShelter
cp ./thankyou.html ./nukeShelter
rm *.html
rm ./nbrhoodFaqs/*.html
rm ./nbrhoodHoF/*.html
rm ./nbrhoodMtrshp/*.html
rm ./nbrhoodProgs/*.html
cp ./nukeShelter/index.html ./nukeShelter/thankyou.html .
sleep .2
py tempRep.py
