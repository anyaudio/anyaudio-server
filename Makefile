run:
	bash run.sh

install:
	pip install -r requirements.txt

test:
	# assumes you have FFMPEG installed (in PATH)
	export FFMPEG_PATH=ffmpeg
	export OPENSHIFT_PYTHON_IP=127.0.0.1
	python -m unittest discover tests
