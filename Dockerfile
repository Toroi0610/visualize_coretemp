FROM python:3.7

WORKDIR /work
ADD . /work

# copying files over
COPY app /work/
COPY log_coretemp /work/
COPY log_coretemp /work/
COPY run.py /work/
COPY requirements.txt /work/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 
ENV PORT 8501

# cmd to launch app when container is run
CMD streamlit run run.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'