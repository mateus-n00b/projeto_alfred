#!/bin/bash
[ $# -lt 1 ] && exit
echo "Found items"
locate "$1" | while read res; do
    echo "$res is from type $(file $res | awk -F: '{print $2}')"
done
