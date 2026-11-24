#!/bin/bash

read -p "enter your weight (kg): " WEIGHT
read -p "enter your height (m): " HEIGHT

BMI=$(( (WEIGHT) / (HEIGHT * HEIGHT) ))

echo "your BMI is $BMI"
