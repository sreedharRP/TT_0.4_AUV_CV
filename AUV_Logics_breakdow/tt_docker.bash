# AUV
docker build -t team_torpedo:0.2 .
docker run --rm --network host -v tt_volume:/home/team_torpedo/tt_0.4_CS/TT_0.4_Docker/tt_docker_files  --device /dev/ttyUSB0 --device /dev/ttyUSB1 --device /dev/input/event0 --device /dev/input/event1 --device /dev/input/event2 --device /dev/input/event3 --device /dev/input/event4 --device /dev/input/event5 --device /dev/input/event6 --device /dev/input/event7 --device /dev/input/event8 -it team_torpedo:0.2

#old 
docker build -t team_torpedo:0.2 .
docker run -v tt_volume:/home/team_torpedo/tt_0.4_CS/TT_0.4_Docker/tt_docker_files  --device /dev/ttyUSB0:/dev/ttyUSB0 --device /dev/ttyUSB1:/dev/ttyUSB1 -it team_torpedo:0.2

#System
docker run  -p-p 192.168.0.30:8080:80  -it control_tt:0.1




