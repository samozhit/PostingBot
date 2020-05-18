#!/bin/bash

LOGIN="login"
PASSWORD="password"

cd ~/Bot && rm -rf *

cd ~/Bot && git clone https://$LOGIN:$PASSWORD@github.com/DvlprNkt-s/PostingBot/
