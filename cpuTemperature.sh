#!/bin/bash
cpuTemp=`cat /sys/class/thermal/thermal_zone0/temp`
gpuTemp=`/opt/vc/bin/vcgencmd measure_temp`

echo "$(date) @ $(hostname)"
echo "CPU temp=$(($cpuTemp/1000))'C ($(($cpuTemp/1000*9/5+32))'F)"
echo "GPU $gpuTemp"

