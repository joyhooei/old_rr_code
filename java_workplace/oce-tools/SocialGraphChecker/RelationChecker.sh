#!/bin/sh

for i in ./lib/*
do
export CLASSPATH=$CLASSPATH:$i
done
export CLASSPATH=$CLASSPATH:./jar/SocialGraphChecker.jar
echo $CLASSPATH

java checker.RelationChecker $1 $2