#!/bin/bash
svn checkout https://svn.code.sf.net/p/commrpg/code/ commrpg-code
git clone https://github.com/obrokedo/TacticalEngine.git
wget -O launch4j.tgz https://downloads.sourceforge.net/project/launch4j/launch4j-3/3.12/launch4j-3.12-linux.tgz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Flaunch4j%2Ffiles%2Flaunch4j-3%2F3.12%2Flaunch4j-3.12-linux.tgz%2Fdownload&ts=1555346586
tar -xvf launch4j.tgz
