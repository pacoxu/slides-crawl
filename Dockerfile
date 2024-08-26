# m.daocloud.io/docker.io/library/python
FROM python:3.9
RUN python3 -m pip install requests BeautifulSoup4 
ADD download_slides.py .
CMD python3 download_slides.py 


