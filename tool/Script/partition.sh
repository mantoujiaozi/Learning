#!bin/sh


tables=`impala-shell -B -q "show tables in $1"`

echo "$tables" | while read table
do

    echo "$table"
	hive -e "msck repair table $1.$table"
	impala-shell -q "invalidate metadata $1.$table"
	echo "$1.$table done"
done