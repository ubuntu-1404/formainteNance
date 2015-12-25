#!/bin/bash
#get runtime parameters from inputing
if [ $# -eq 0 ] ; then
        echo "no parameters !"
        exit
else
        for i in "$@" ; do
                echo "${i}";
        done
fi

#make string to be substring one
tmp0="aa.bb.cc.dd"
echo "${tmp0}##*.==>${tmp0##*.}"
echo "${tmp0}%%.*==>${tmp0%%.*}"
echo "`echo ${tmp0} | cut -c 3-5`"
echo "`echo ${tmp0} | tr -sc 'a-zA-Z' ' '`"
