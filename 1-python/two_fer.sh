#!/usr/bin/env bash

# linux file permissions: (ls -l)
# (first: - for file, d for directory)
# three sets of permissions for owner, group, all.
# every file has an owner
# in linux, users have groups
# read, write, execute for each of those

# wrap logic in functions to keep organized
main () {
  # this is how we write most if-else conditions. "-z" is one of many operators:
  # https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions
  # if the first parameter is zero-length (empty)...
  if [[ -z "$1" ]]; then
    # set the variable to "you",
    person=you
  else
    # or else, set the variable to the first parameter.
    person="$1"
  fi

  # use the echo command to send the desired result to STDOUT.,
  # based on the variable's value.
  echo "One for $person, one for me."
}

# call the main function, passing along all the script's parameters to it.
main "$@"
