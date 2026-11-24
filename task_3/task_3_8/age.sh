#!/bin/bash

readonly CURRENT_YEAR=2026
read -p "enter your birth year: " BIRTH_YEAR

AGE=$((CURRENT_YEAR - BIRTH_YEAR))

echo "current year is $CURRENT_YEAR"
echo "your probable age is $AGE"
