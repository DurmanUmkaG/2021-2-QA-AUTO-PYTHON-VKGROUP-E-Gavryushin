#!/bin/bash

FILE=$1 
cat /dev/null > result.txt

echo "Общее количество запросов" >> result.txt
cat $FILE | wc -l  >> result.txt
echo >> result.txt

echo "Общее количество запросов по типу" >> result.txt
awk -F "\"" '{print $2}' $FILE  | awk '{print $1}' | sort | uniq -c | awk 'NR > 1 {print $2, $1}' >> result.txt
echo >> result.txt

echo "Топ 10 самых частых запросов" >> result.txt
awk -F "\"" '{print $2}' $FILE | awk '{print $2}' | sort | uniq -c | sort -nr |  awk '{print $2, $1}' | head >> result.txt
echo >> result.txt

echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой" >> result.txt
awk '$9 ~ /4[[:digit:]]{2}/' $FILE  | sort -nrk10 | awk '{print $7, $9, $10, $1}' | head -5 >> result.txt
echo >> result.txt

echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой" >>result.txt
awk '$9 ~ /5[[:digit:]]{2}/ {print$1}' $FILE | sort | uniq -c | sort -nr | awk '{print $2, $1}' | head -5 >> result.txt
