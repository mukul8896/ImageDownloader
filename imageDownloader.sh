#!/bin/bash
function download() {
    if [ $# -eq 2 ]
    then
        echo "in myp"
        python3 DownloadGallary.py --link $1 --site $2
    elif [ $# -eq 3 ]
    then
        python3 DownloadGallary.py --link $1 --pages $2 --site $3
    else
        echo "Wrong Inputs"
    fi
}
