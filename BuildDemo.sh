#!/bin/bash

set -e

# Clean up tactical engine
rm -f ~/TacticalEngine/Tactical.jar
rm -Rf ~/TacticalEngine/bin

# Clean up LegaciesOfVeridocia
rm -f ~/commrpg-code/LegaciesOfVeridocia/lib/Tactical.jar
rm -f ~/commrpg-code/LegaciesOfVeridocia/LoV-Dev.jar
rm -Rf ~/commrpg-code/LegaciesOfVeridocia/bin

# Clean up latestBuild
rm -f  ~/commrpg-code/latestBuild/LoV-Dev.jar
rm -f  ~/commrpg-code/latestBuild/LoV-Official.jar

# Clean up demo.exe
rm -f ~/LoV-Demo.exe

cd ~/TacticalEngine
git pull
ant compile create_run_jar
mv Tactical.jar  ../commrpg-code/LegaciesOfVeridocia/lib/
cd ../commrpg-code/LegaciesOfVeridocia
svn update
ant -f LoV-Ant-Dev.xml compile create_run_jar
mv LoV-Dev.jar ../latestBuild/
cd ../latestBuild/
svn update
ant -f LoV-Ant-Official.xml
cd ~
launch4j/launch4j LovExeConfig.xml
date > build.date
