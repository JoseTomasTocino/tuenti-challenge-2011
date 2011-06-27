#!/bin/bash
cat entrada | ./debase.py
for f in rsa/1024/*
do
openssl rsautl -decrypt -in salida -passin file:k -inkey $f 2> /dev/null && break
done
echo "######################################################## Resuelto con $f"
rm salida
