# QPALZM Web Search

> **简体中文** | **English** — Dual-language documentation

---

[中文文档](#中文文档) | [English Documentation](#english-documentation)

---

> **Assets 施工中 / Assets under maintenance**
>
> Releases 页面暂不可用。如需使用，请按下方「源码运行」步骤操作。
>
> The Releases page is temporarily unavailable. To use the tool, run it from source using the steps below.

---

<a id="中文文档"></a>

macOS / Windows 简易网页搜索图形工具，基于 CustomTkinter 开发，一键调用百度、必应搜索，支持自定义网址直接打开。

## 功能特点

- 图形化输入框，快速输入关键词
- 一键百度搜索、Bing 国内版搜索
- 支持手动输入任意 URL 并直接打开浏览器访问
- 窗口支持自由缩放，界面简洁轻量化
- 配套 macOS 与 Windows 一键依赖安装脚本，开箱即用

## 发布资源 Assets 说明

> **暂不建议下载** —— 程序包施工中，请改用下方「方式二：源码运行」。

| 文件名称 | 适用平台 | 说明 |
|--------|--------|------|
| install_dependencies.sh | macOS | Mac 依赖安装脚本 |
| InstallDependencies.bat | Windows | Windows 依赖安装脚本 |
| WebSearch_Mac_v0.2.dmg | macOS | Mac 标准安装包，拖拽至应用程序即可使用 |
| WebSearch_MacOS_Portable_v0.2.zip | macOS | 绿色压缩包，解压后直接运行 |
| WebSearch_Windows_v0.2.exe | Windows | 绿色程序，可直接双击运行 |

## 使用教程

### 方式一：运行编译好的程序包

> **暂不可用**：程序包施工中，请改用下方「方式二：源码运行」。

1. 进入仓库 Releases 页面，下载对应平台的程序文件
2. 运行对应程序：
- **Mac DMG**：打开镜像文件，将软件拖入「应用程序」文件夹
- **Mac 压缩包**：解压压缩包，运行内部可执行文件
- **Windows EXE**：直接双击运行，无需安装

### 方式二：源码运行

1. 下载源码到本地文件夹
2. 执行依赖安装脚本：
- **macOS**：
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
- **Windows**：
```bat
InstallDependencies.bat
```
3. 启动程序：
- **macOS**：
```bash
python3 main.py
```
- **Windows**：
```bat
python main.py
```

## 注意事项

1. 设备需提前安装 Python 并配置系统环境变量
2. macOS 运行 shell 脚本前需要赋予执行权限；Windows 直接双击 `.bat` 即可
3. 程序会自动识别当前系统并调用默认浏览器，无需手动选择平台

## 项目信息

- 项目名称：QPALZM Web Search
- 工具系列：QPALZM Toolkit
- 开发作者：AdkSetup
- 支持平台：macOS / Windows

---

<a id="english-documentation"></a>

A lightweight cross-platform web search GUI tool for macOS and Windows, built with CustomTkinter. One-click access to Baidu and Bing search, with support for opening any custom URL directly.

## Features

- Graphical input box for quick keyword entry
- One-click Baidu search and Bing (China) search
- Manually enter any URL to open it directly in the browser
- Freely resizable window with a clean and lightweight interface
- Comes with one-click dependency installers for both macOS and Windows, ready to use out of the box

## Release Assets

> **Do not download these yet** — the packages are under maintenance. Run from source in the meantime.

| File Name | Platform | Description |
|--------|--------|------|
| install_dependencies.sh | macOS | Mac dependency installation script |
| InstallDependencies.bat | Windows | Windows dependency installation script |
| WebSearch_Mac_v0.2.dmg | macOS | Standard Mac installer, drag to Applications to use |
| WebSearch_MacOS_Portable_v0.2.zip | macOS | Portable archive, extract and run directly |
| WebSearch_Windows_v0.2.exe | Windows | Standalone program, double-click to run |

## Usage Guide

### Method 1: Run the compiled package

> **Temporarily unavailable** — the packages are under maintenance. Use "Method 2: Run from source" below instead.

1. Go to the repository Releases page and download the file for your platform
2. Run the program:
- **Mac DMG**: Open the disk image and drag the app to the "Applications" folder
- **Mac archive**: Unzip the archive and run the included executable
- **Windows EXE**: Double-click to run, no installation required

### Method 2: Run from source

1. Download the source code to a local folder
2. Run the dependency installation script:
- **macOS**:
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
- **Windows**:
```bat
InstallDependencies.bat
```
3. Launch the program:
- **macOS**:
```bash
python3 main.py
```
- **Windows**:
```bat
python main.py
```

## Notes

1. Python must be pre-installed on the device and configured in the system environment variables
2. On macOS, execute permission must be granted to the shell script first; on Windows, simply double-click the `.bat` file
3. The program automatically detects your operating system and uses the default browser — no manual platform selection needed

## Project Info

- Project Name: QPALZM Web Search
- Tool Series: QPALZM Toolkit
- Developer: AdkSetup
- Supported Platforms: macOS / Windows

---

## License

This project is licensed under the [MIT License](./LICENSE).