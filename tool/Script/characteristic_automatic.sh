cd `dirname $0`

if [ $# -lt 1 ]
then
   log_day=`date -d "-1 day" +%Y%m%d`
else
   log_day=`date -d "-1 day $1" +%Y%m%d`
fi


log_day_bf15=`date -d "-15 day $log_day" +%Y%m%d`



echo $log_day

impala-shell -q "
drop table if exists tmp.sb_0;
create  table tmp.sb_0 as
select userid,GROUP_CONCAT(concat(event,element_name,element_page,num)) as a from
(SELECT b.userid,b.event,b.element_name,b.element_page,cast(count(1) as STRING) as num from
(SELECT master_id,apprentice_id from  newsearn_dp_view.parquet_newsearn_task_ma_master_view
WHERE replace(substr(create_time,1,10),'-','')='$log_day')a
join
(select * from   newsearn_dp_view.parquet_newsearn_events_view_all
where logday='$log_day' and event in ('AppClick','WebClick','AppBannerClick'))b
on cast(a.apprentice_id as string)=b.userid
join
(select userid,count(1) as cnt from   newsearn_dp_view.parquet_newsearn_events_view_all
where logday='$log_day' and event in ('AppClick','WebClick','AppBannerClick') group by userid having count(1)>9)c
on cast(a.apprentice_id as string)=c.userid
group by b.userid,b.event,b.element_name,b.element_page)t
group by userid
;
"
sleep 5


impala-shell -q  "select * from tmp.sb_0" -B --output_delimiter=","  -o /data10/app/script/gray_user/strategy/file.csv


python /data10/app/script/gray_user/strategy/sort.py 

impala-shell -q "ALTER TABLE anti_cheat.anti_tezheng_user add if not exists partition (type=1);"

mv /data10/app/script/gray_user/strategy/sort.csv  /mnt/hdfs/user/hive/warehouse/anti_cheat.db/anti_tezheng_user/type=1

impala-shell  -q "refresh anti_cheat.anti_tezheng_user";

sql_str=`cat /data10/app/script/gray_user/strategy/sql/characteristic_automatic.sql`


sql_str=${sql_str//__log_day_bf15/$log_day_bf15}
sql_str=${sql_str//__log_day/$log_day}

echo $sql_str

impala-shell -q "$sql_str"

sleep 6

impala-shell -q "select distinct user_id  from anti_cheat.anti_click_abnormal  where logday='$log_day' and type=7"|sed 's/|/''/g' |grep -v "^$\|+\|user_id">/data10/app/script/gray_user/data/Characteristic_Automatic_Timer.csv