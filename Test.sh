#!/usr/bin/sh
find ./ -name "test_*.py" -exec echo {} \; -exec python {} \;

# Remove stay python test fragments.
rm *.pyc
