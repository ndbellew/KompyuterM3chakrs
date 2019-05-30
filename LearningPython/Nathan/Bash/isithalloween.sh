#!/bin/bash
read m d
if [[ $m == "OCT" ]] && [[ $d -eq 31 ]]; then
  echo "yup"
elif [[ $m == "DEC" ]] && [[ $d -eq 25 ]]; then
  echo "yup"
else
  echo "nope"
fi
