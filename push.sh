#! /bin/bash

pushd /home/anton/Programming &&
tar -cf Wellesley.tar Wellesley &&
scp Wellesley.tar blueridge:/home/pi/store &&
ssh blueridge /home/pi/store/deploy_wellesley.sh &&
rm Wellesley.tar &&
popd
