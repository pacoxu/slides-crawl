# slides-crawl
download all slides from sched.com event: kubecon/istiocon 

1. KubeCon China 2023: https://kccncosschn2023.sched.com/list/descriptions/
2. IstioCon China 2023: https://istioconchina2023.sched.com/list/descriptions/

- `/list/descriptions/`: this page will include all slides links in the page directly.

### Run with python3

```
python3 -m pip install requests BeautifulSoup4
python3 download_slides.py
```

### Quick Run in Docker

```
docker run ghcr.io/pacoxu/slides-crawl:latest
```

For KubeCon NA 2024, you can run 
```
docker run -e SCHED_LINK=https://kccncna2024.sched.com/list/descriptions/ ghcr.io/pacoxu/slides-crawl:latest
```
download files will be inside  the container, and you can use volume or `docker cp` to get them to your PC.
