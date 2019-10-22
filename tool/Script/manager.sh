#!/bin/sh
cd `dirname $0`
command=$1

if [ -z $command ];then
  echo "请使用： manager.sh [start|stop|restart|status]"
  exit 
fi

if [[ $command == "start" ]];then
  ps axu |grep -w "anti_auto_service.sh"|grep -v "grep"
  if [[ $? == 0 ]];then
     ps axu |grep -w "anti_auto_service.sh"|grep -v "grep" |gawk '{print $2}'|xargs -n1  kill -9
  else
     source ~/.bashrc && cd /data10/app/script/gray_user/control/ && nohup  sh /data10/app/script/gray_user/control/anti_auto_service.sh /data10/app/script/gray_user/control/anti_exec_strategy.sh 2>&1 >> ../data/auto.log &
     echo "service started!" 
  fi
elif [[ $command == "stop" ]];then
  ps axu |grep -w "anti_auto_service.sh"|grep -v "grep"
  if [[ $? == 0 ]];then
   ps axu |grep -w "anti_auto_service.sh"|grep -v "grep" |gawk '{print $2}'|xargs -n1  kill -9
  else
    echo "service not start!"
  fi
elif [[ $command == "restart"  ]];then
     ps axu |grep -w "anti_auto_service.sh"|grep -v "grep"
  if [[ $? == 0 ]];then
     ps axu |grep -w "anti_auto_service.sh"|grep -v "grep" |gawk '{print $2}'|xargs -n1  kill -9
     echo "service stop!"
  
     source ~/.bashrc && cd /data10/app/script/gray_user/control/  && nohup sh /data10/app/script/gray_user/control/anti_auto_service.sh /data10/app/script/gray_user/control/anti_exec_strategy.sh 2>&1 >> ../data/auto.log &
   else
     source ~/.bashrc && cd /data10/app/script/gray_user/control/  && nohup sh /data10/app/script/gray_user/control/anti_auto_service.sh /data10/app/script/gray_user/control/anti_exec_strategy.sh 2>&1 >> ../data/auto.log &
     echo "service started!"
  fi 
elif [[ $command == "status"  ]];then
  ps axu |grep -w "anti_auto_service.sh"|grep -v "grep"
  if [[ $? == 0 ]];then
     echo "service is running ..."
  else 
     echo "service stoped!"
  fi  
else
  echo "请使用： manager.sh [start|stop|restart|status]"
fi
