input="$*"
cd ~/src/python/tl-dw
source .venv/bin/activate
python3 -m main $input 
deactivate
cd ~
