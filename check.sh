#!/bin/bash
# script para a verificacao de uso de memoria pelos diretorios
#
# Mateus-n00b, Dezembro 2016
#
# Versao 1.0
#
# Licensa GPL
# -===================================================================================== -
rm /tmp/outLogs 2> /dev/null

for x in "$HOME/"*
do
  echo "Total memory usage of $(basename "$x") is at $(du -sh "$x"| awk '{print $1}')" >> /tmp/outLogs
done
