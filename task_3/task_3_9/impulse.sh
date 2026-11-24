#!/bin/bash

read -p "enter gen name: " NAME
read -p "enter expression rate: " RATE

if [ -n "$NAME" ] && [ -n "$RATE" ]; then
	echo "expression of gene $NAME is $RATE units"
else
	echo "lack of input data"
fi
