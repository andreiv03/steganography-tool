# Steganography Tool

A powerful **Flask-based web application** for encoding and decoding hidden messages inside images using **LSB (Least Significant Bit)** steganography.

## ✨ Features

- **Encode messages into images** – Hide secret messages inside image files.
- **Decode hidden messages** – Extract messages embedded in images.
- **Web-based Interface** – Easy-to-use UI with file upload & download support.
- **Automatic Directory Handling** – Ensures all necessary folders exist before saving files.
- **Docker & Docker-Compose Support** – Run the app seamlessly in a containerized environment.

## ⚡ Technology Stack

- **Python (3.9 or later)** – Core programming language for backend execution.
- **Flask** – Lightweight web framework for handling requests and rendering templates.
- **Pillow (PIL)** – Used for image processing to encode and decode messages.
- **Docker & Docker Compose** – For containerized application deployment.

## ⚙️ Build & Installation

### Prerequisites

Before installing the project, ensure you have the following installed:

- **Python 3.9+** (for running the Flask application)
- **Docker & Docker Compose** (for containerized execution, optional)

### Installation Instructions

Follow these steps to clone, build, and run the steganography tool:

**Option 1: Running with Docker (Recommended)**
```sh
# Ensure Docker & Docker Compose are installed
docker --version
docker-compose --version

# Clone the repository
git clone https://github.com/andreiv03/steganography-tool.git
cd steganography-tool

# Build and run the project
docker-compose up --build
```
The app will be accessible at [http://localhost:5000](http://localhost:5000).

**Option 2: Running Locally (Without Docker)**
```sh
# Ensure Python 3.9+ is installed
python3 --version

# Clone the repository
git clone https://github.com/andreiv03/steganography-tool.git
cd steganography-tool

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 index.py
```
The app will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the project, follow these steps:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature-branch`)
3. **Commit** your changes (`git commit -m "feat: add new feature"`)
4. **Push** your changes (`git push origin feature-branch`)
5. Open a **Pull Request** 🚀

For suggestions or bug reports, feel free to open an issue with the appropriate label.

⭐ **If you find this project useful, consider giving it a star!** ⭐

## 📜 License

Distributed under the **MIT License**. See `LICENSE.txt` for details.
