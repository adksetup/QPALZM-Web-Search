# QPALZM Web Search

macOS-only lightweight web search GUI tool, built with CustomTkinter. One-click access to Baidu and Bing search, with support for opening any custom URL directly.

> [中文文档](./README.md)

## Features

- Graphical input box for quick keyword entry
- One-click Baidu search and Bing (China) search
- Manually enter any URL to open it directly in the browser
- Freely resizable window with a clean and lightweight interface
- Comes with a macOS one-click dependency installer, ready to use out of the box

## Release Assets

| File Name | Platform | Description |
|--------|--------|------|
| install_dependencies.sh | macOS | Mac dependency installation script |
| WebSearch.dmg | macOS | Standard Mac installer, drag to Applications to use |
| WebSearch_Mac.zip | macOS | Portable archive, extract and run directly |

## Usage Guide

### Method 1: Run the compiled package

1. Go to the repository Releases page and download the macOS program file
2. Run the program:
- Mac DMG: Open the disk image and drag the app to the "Applications" folder
- Mac archive: Unzip the archive and run the included executable

### Method 2: Run from source

1. Download the source code to a local folder
2. Run the dependency installation script in the terminal:
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
3. Launch the program:
```bash
python main.py
```

## Notes

1. Python must be pre-installed on the device and configured in the system environment variables
2. Execute permission must be granted to the shell script before running
3. The code uses macOS's native `open` command to launch the browser, compatible with Apple systems only

## Project Info

- Project Name: QPALZM Web Search
- Tool Series: QPALZM Toolkit
- Developer: AdkSetup
- Supported Platform: macOS

## License

This project is licensed under the [MIT License](./LICENSE).
