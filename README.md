# File Storage Demo

A simple Flask web application that demonstrates file upload and download functionality using local file storage. Users can upload files from their device and browse/download uploaded files via a web interface.

## Features
- Upload files from a web browser (designed for mobile-friendly usage).
- View a list of uploaded files and download them individually.
- Automatic directory listing powered by [Flask-AutoIndex].

## Technology Stack
- Python 3
- [Flask]
- [Flask-AutoIndex]

## Directory Structure
```
├── startweb.py           # Main application script
├── public
│   ├── index.html       # HTML template for the upload/download UI
│   ├── static
│   │   └── style.css    # CSS styles for the UI
│   └── user             # (ignored) Upload destination folder for user files
├── run_Windows.bat      # Helper script to launch the app on Windows
├── .gitignore           # Git ignore rules (ignores public/user/ uploads)
└── webstorage-demo.code-workspace  # VS Code workspace configuration
```

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_dir>
   ```
2. (Optional) Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install Flask Flask-AutoIndex
   ```
4. Create the upload directory (ignored by Git):
   ```bash
   mkdir -p public/user
   ```

## Usage

### On Linux/macOS
```bash
python3 startweb.py
```

### On Windows
Double-click `run_Windows.bat` or run:
```bat
run_Windows.bat
```

By default, the application listens on port 80 on all network interfaces (0.0.0.0).
Open your browser and navigate to:

- http://<server-ip>/

If local debug mode is enabled (see Configuration), the server binds to 127.0.0.1:80:

- http://127.0.0.1/

## Configuration
- To enable local loopback mode binding to `127.0.0.1`, create an empty file named `debug` in the project root before running the app.

## License
This project does not include a license. See individual source files for any usage notes.

[Flask]: https://github.com/pallets/flask
[Flask-AutoIndex]: https://github.com/general03/flask-autoindex
