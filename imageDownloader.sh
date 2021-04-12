#!/bin/bash
function downloadImages() {
    if [ $# -eq 1 ]
    then
        python3 DownloadGallary.py --link $(termux-clipboard-get) --site $1
    elif [ $# -eq 2 ]
    then
        python3 DownloadGallary.py --link $(termux-clipboard-get) --pages $1 --site $2
    else
        echo "Wrong Inputs"
    fi
}
