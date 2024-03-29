#!/bin/bash

if [ "$#" != 1 ]; then
	echo "Run script with c to clean or i to init"
	exit 0
fi

if [ $1 == "i" ]; then
	flask db init
	flask db migrate
	flask db upgrade
	if [ -x "$(command -v python3)" ]; then
		python3 database.py
	elif [ -x "$(command -v python)" ]; then
		python database.py
	fi
	exit 0

elif [ $1 == "c" ]; then
	DB=./app.db
	MIG=./migrations/
	if test -f "$DB"; then
		rm $DB
	fi
	if test -d "$MIG"; then
		rm -rf $MIG
	fi
	exit 0
fi
