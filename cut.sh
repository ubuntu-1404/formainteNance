#!/bin/bash
tmp0="aa.bb.cc.dd"
echo "${tmp0}##*.==>${tmp0##*.}"
echo "${tmp0}%%.*==>${tmp0%%.*}"
echo "`echo ${tmp0} | cut -c 3-5`"
echo "`echo ${tmp0} | tr -sc 'a-zA-Z' ' '`"
