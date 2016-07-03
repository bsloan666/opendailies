clean:
	find . -name "*\.pyc" -type f -print | xargs /bin/rm -f

build:
	echo "OpenDailies build"

install: build
	echo "OpenDailies install"

