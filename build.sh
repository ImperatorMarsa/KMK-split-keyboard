#!/bin/sh

rm -rf /app/build/*

for f in /app/src/*.py; do
    bn=$(basename "$f")
    if [ "$bn" != "code.py" ]; then
        /bin/mpycross "$f" -o "/app/build/${bn%.py}.mpy"
    else
        cp "$f" /app/build/
    fi
done
