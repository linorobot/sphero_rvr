#!/usr/bin/env bash

sudo cp sphero.rules  /etc/udev/rules.d

sudo service udev reload
sudo service udev restart