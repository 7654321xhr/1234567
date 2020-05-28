
#!/bin/bash

function search_dir(){
    for file in `ls $1`
    do
        if  [ -d $1"/"$file ]; then
            search_dir $1"/"$file
        else
            filetype="_gt.json"
            result=$(echo $file | grep "${filetype}")
            if  [ "$result" != ""  ]; then
               ((count++))
            fi
        fi
    done
}

search_dir  test_dir
echo 目标文件共有$count个

