# Flask IPv4 Check App

A simple Python Flask web application that provides IPv4-related utilities via a web interface. Includes static and templated HTML pages for user interaction.

## Features

- Web-based IPv4 tools
- Simple UI with `index.html` and `calc.html` templates
- Container-ready with a Dockerfile

## Prerequisites

- Python 3.7 or higher
- `pip` package manager
- (Optional) Docker, if you prefer containerized deployment

## Installation (Local)

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/flask-ipv4-check.git
cd flask-ipv4-check
```

2. **Create a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Application**

```bash
python ipv4-check.py
```

Then visit http://localhost:5000 in your browser.


## Building (Docker)

1. **Build the image**
```bash
docker build -t ip-calc .
```

2. **Run the container**

```bash
docker run -p 80:5000 ip-calc
```

Then visit http://localhost in your browser.

## Installation (Docker)

```bash
docker run -p 5000:5000 lilithbtw/ip-calc
```

Then visit http://localhost:5000 in your browser
