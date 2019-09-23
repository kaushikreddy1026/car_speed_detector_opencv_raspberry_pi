FROM sgtwilko/rpi-raspbian-opencv:latest
RUN  apt-get update
RUN mkdir /opencv-carspeed
WORKDIR /opencv-carspeed
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /opencv-carspeed
CMD python3 speed_check.py
