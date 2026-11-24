#!/bin/bash

check_root() {
	if [ "$EUID" -eq 0 ]; then
		echo "everythig is ok"
	else
		echo "error. not enough rights"
		exit 1
	fi
}

check_root
