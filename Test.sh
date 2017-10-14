#!/usr/bin/sh
find ./ -name "test_*" -exec echo {} \; -exec {} \;

# Remove stay python test fragments.
rm *.pyc
