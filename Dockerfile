FROM locustio/locust

ADD /locustfiles/api_load_test.py /locustfiles/

#======================
# Install dependencies
#======================
COPY requirements.txt /dependencies/
RUN pip3 install -r /dependencies/requirements.txt


