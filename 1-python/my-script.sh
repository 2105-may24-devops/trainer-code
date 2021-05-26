#!/usr/bin/bash

# this file by itself doesn't tell your system HOW to run it.
# bash is not the only shell (also bash has compatiblity modes)
# in linux, a "shebang" at the top of the file
# tells the system what shell program to run your script with.

echo welcome to my script

# MOST complicated parts of bash are just text substitutions/expansions
# and exit codes

# exit codes:
#   0 means success, anything else means error

if echo text | grep -q tex ; then
    echo "exit code must have been zero"
fi

if [[ 4 == 3 || 5 -gt 4 ]] ; then
    echo "exit code must have been zero"
fi


if (( 0 )) ; then
    echo "exit code must have been zero"
fi

data=4
((data+=1))
echo $data

# double parentheses is for arithmetic
#  (also: parameters don't need to be prefixed with $,
#   and they are treated like numbers not text)

echo you entered: "$@"
echo all done
