#!/bin/sh
export RR=$(docker ps | grep router-ayumusak-1 | cut -b 1-12)
export VTEP1=$(docker ps | grep router-ayumusak-2 | cut -b 1-12)
export VTEP2=$(docker ps | grep router-ayumusak-3 | cut -b 1-12)
export VTEP3=$(docker ps | grep router-ayumusak-4 | cut -b 1-12)

export D_PATH=~/Board/badass/P3

sudo docker exec -i $RR bash -s < $D_PATH/_ayumusak-1.sh
sudo docker exec -i $VTEP1 bash -s < $D_PATH/_ayumusak-2.sh
sudo docker exec -i $VTEP2 bash -s < $D_PATH/_ayumusak-3.sh
sudo docker exec -i $VTEP3 bash -s < $D_PATH/_ayumusak-4.shclear
