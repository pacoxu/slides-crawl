# slides-crawl

download all slides from sched.com event: kubecon/istiocon 

- `/list/descriptions/`: this page will include all slides links in the page directly.

## KubeCon + CloudNativeCon Events (2023-2025)

### 2023 Events

#### KubeCon + CloudNativeCon
- **China 2023**: https://kccncosschn2023.sched.com/list/descriptions/
- **Europe 2023**: https://kccnceu2023.sched.com/list/descriptions/
- **North America 2023**: https://kccncna2023.sched.com/list/descriptions/

#### Colocated Events
- **Europe 2023**: https://colocatedeventseu2023.sched.com/list/descriptions/
- **North America 2023**: https://colocatedeventsna2023.sched.com/list/descriptions/

#### Other Events
- **IstioCon China 2023**: https://istioconchina2023.sched.com/list/descriptions/

### 2024 Events

#### KubeCon + CloudNativeCon
- **China 2024**: https://kccncosschn2024.sched.com/list/descriptions/
- **Europe 2024**: https://kccnceu2024.sched.com/list/descriptions/
- **North America 2024**: https://kccncna2024.sched.com/list/descriptions/
- **India 2024**: https://kccncin2024.sched.com/list/descriptions/

#### Colocated Events
- **Europe 2024**: https://colocatedeventseu2024.sched.com/list/descriptions/
- **North America 2024**: https://colocatedeventsna2024.sched.com/list/descriptions/

### 2025 Events

#### KubeCon + CloudNativeCon
- **Europe 2025**: https://kccnceu2025.sched.com/list/descriptions/
- **North America 2025**: https://kccncna2025.sched.com/list/descriptions/
- **China 2025**: https://kccncosschn2025.sched.com/list/descriptions/
- **Japan 2025**: https://kccncjpn2025.sched.com/list/descriptions/
- **India 2025**: https://kccncin2025.sched.com/list/descriptions/

#### Colocated Events
- **Europe 2025**: https://colocatedeventseu2025.sched.com/list/descriptions/
- **North America 2025**: https://colocatedeventsna2025.sched.com/list/descriptions/

#### CNCF Maintainer Summit
- **Europe 2025**: https://cncfmaintainersummiteu2025.sched.com/list/descriptions/
- **North America 2025**: https://cncfmaintainersummitna2025.sched.com/list/descriptions/

## Notes

- **URL Availability**: Some future event URLs may not be live yet. Sched.com pages are typically published closer to the event dates.
- **Regional Variations**: URL patterns may vary slightly between events. If a URL doesn't work, try checking the official KubeCon website for the correct sched.com link.
- **Event Schedules**: KubeCon events typically occur multiple times per year across different regions. Check the [CNCF Events page](https://events.linuxfoundation.org/about/calendar/) for official dates and locations.

## URL Validation

You can test if a sched.com URL is accessible and contains slides using the validation script:

```bash
python3 validate_url.py https://kccncna2024.sched.com/list/descriptions/
```

This will check if the URL is accessible and report how many slide files are available for download.

## Usage

### Run with python3

```bash
python3 -m pip install requests BeautifulSoup4
python3 download_slides.py
```

### Quick Run in Docker

```bash
docker run ghcr.io/pacoxu/slides-crawl:latest
```

### Download from Specific Events

You can specify which event to download from using the `SCHED_LINK` environment variable:

```bash
# KubeCon North America 2024
docker run -e SCHED_LINK=https://kccncna2024.sched.com/list/descriptions/ ghcr.io/pacoxu/slides-crawl:latest

# KubeCon Europe 2024
docker run -e SCHED_LINK=https://kccnceu2024.sched.com/list/descriptions/ ghcr.io/pacoxu/slides-crawl:latest

# Colocated Events North America 2024  
docker run -e SCHED_LINK=https://colocatedeventsna2024.sched.com/list/descriptions/ ghcr.io/pacoxu/slides-crawl:latest

# Using Python directly
export SCHED_LINK=https://kccnceu2025.sched.com/list/descriptions/
python3 download_slides.py
```

Downloaded files will be saved in the `downloaded_slides/` folder (when running locally) or inside the container (when using Docker). You can use volume mounts or `docker cp` to get files from the container to your local machine.

### Docker with Volume Mount

```bash
# Mount a local directory to save downloads
docker run -v $(pwd)/downloads:/app/downloaded_slides -e SCHED_LINK=https://kccncna2024.sched.com/list/descriptions/ ghcr.io/pacoxu/slides-crawl:latest
```
