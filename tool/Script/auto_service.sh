#!/bin/sh
# 自动循环执行脚本，默认开始时间为执行脚本时的那个小时。可以传入时间参数 例如 20180417-15 标识查询15点数据开始执行
cd `dirname $0`

script_path=$1
query_time=$2

if [ -z  "$query_time"  ]
then
	query_time=`date  +"%Y%m%d-%H"`
fi

if [ -z  "$script_path"  ]
then
        echo "请传入脚本执行路径"
        exit
fi




# 循环,反作弊策略的调度,间隔时间3600s
at="15636091725,18311283082"
while :
do
    start_time=`date +%s`
    format_query_time=`echo $query_time|sed 's/-/ /g'`
    sh $script_path $format_query_time
    end_time=`date +%s`
    exec_time=$(( $end_time - $start_time ))
    if [ $exec_time -lt 1 ];then
    coohua_alarm -type markdown -title 反作弊服务流程  -text $query_time反作弊服务流程执行时间$exec_time小于40s,请注意检查 -a $at
    fi
    if [ $exec_time -gt 1800 ];then
    coohua_alarm -type markdown -title 反作弊服务流程  -text $query_time反作弊服务流程执行时间$exec_time大于600s,请注意检查 -a $at
    fi
    if [ $? -eq 0 ]; then
	sleep 600
	query_time=`date  +"%Y%m%d-%H"`
    else
        coohua_alarm -type markdown -title 反作弊服务流程  -text $query_time反作弊服务流程执行失败  -a $at
	break
    fi
        
done
