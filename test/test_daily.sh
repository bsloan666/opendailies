env PYTHONPATH=`pwd`/customize:`pwd`/src/python src/bin/todaily -h
env PYTHONPATH=`pwd`/customize:`pwd`/src/python python test/test_objects.py 
env PYTHONPATH=`pwd`/customize:`pwd`/src/python src/bin/todaily -i test/image/scene.%04d.exr -o /var/tmp/daily_out/scene.%04d.jpg -s 1001 -e 1010 -f jpg 
