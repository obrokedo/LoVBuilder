#!/bin/bash
touch isbuilding
./BuildDemo.sh > Build.log
rm isbuilding
