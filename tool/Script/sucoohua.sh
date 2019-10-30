#!/bin/sh

expect -c '
set USER "coohua"
set PASSWD "fkPfztaqt?a0wihEluum4uhy"
set timeout 10

trap {
    set rows [stty rows]
	set cols [stty columns]
    stty rows $rows columns $cols < $spawn_out(slave,name)
} WINCH
spawn su - $USER
expect "\[P密\]*"
send "$PASSWD\n"
interact
'
