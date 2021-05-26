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

# _ ; _ just runs both commands
# _ && _ returns 0 if both commands' exit codes were 0
  # runs first command, if it was nonzero, then we stop there
# _ || _ returns 0 if either commands' exit code was 0
  # runs first command, if it was zero, then we stop there
# this behavior is called "short-circuiting"

echo text | grep -q tex && echo "previous command successful"

echo text | grep -q tex || echo "previous command unsuccessful"

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

printarg () {
  variable=1
  echo $1
  echo $2
}

echo $variable
printarg $@
echo $variable

# normally, variables are "global scope"

# brace expansion

# command substitution
echo $(echo 4) + $(echo 1) = 5
echo current dir is $(pwd)
echo current dir is `pwd`

# grep for filtering/searching text
# find for searching for files (can execute a command for each file)
# printf for formatting text in more complex ways than echo
# sed for replacing text based on patterns (regex)
# awk for parsing text and processing it
# xargs for dynamically building one command's arguments from another command's output
# curl/wget for downloading webpages (or sending any http requests)
