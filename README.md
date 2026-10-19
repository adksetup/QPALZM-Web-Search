# QPALZM Web Search

> **简体中文** | **English** — Dual-language documentation

---

[中文文档](#中文文档) | [English Documentation](#english-documentation)

---

<a id="中文文档"></a>

macOS 专用简易网页搜索图形工具，基于 CustomTkinter 开发，一键调用百度、必应搜索，支持自定义网址直接打开。
## 功能特点
- 图形化输入框，快速输入关键词
- 一键百度搜索、Bing国内版搜索
- 支持手动输入任意URL并直接打开浏览器访问
- 窗口支持自由缩放，界面简洁轻量化
- 配套 macOS 一键依赖安装脚本，开箱即用
## 发布资源 Assets 说明
| 文件名称 | 适用平台 | 说明 |
|--------|--------|------|
| install_dependencies.sh | macOS | Mac 依赖安装脚本 |
| InstallDependencies.bat | Windows | Windows 依赖安装脚本 |
| WebSearch_Mac_v0.2.dmg | macOS | Mac 标准安装包，拖拽至应用程序即可使用 |
| WebSearch_Mac_Portable_v0.2.zip | macOS | 绿色压缩包，解压后直接运行 |
| WebSearch_Windows_v0.2.exe | Windows | 绿色程序，可直接双击运行 |
## 使用教程
### 方式一：运行编译好的程序包
1. 进入仓库 Releases 页面，下载对应 macOS 程序文件
2. 运行对应程序：
- Mac DMG：打开镜像文件，将软件拖入「应用程序」文件夹
- Mac 压缩包：解压压缩包，运行内部可执行文件
### 方式二：源码运行
1. 下载源码到本地文件夹
2. 终端执行安装依赖脚本：
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
3. 启动程序
```bash
python main.py
```
## 注意事项
1. 设备需提前安装 Python 并配置系统环境变量
2. 运行shell脚本前需要赋予执行权限
3. 代码使用 macOS 原生 `open` 命令唤起浏览器，仅适配苹果系统
## 项目信息
- 项目名称：QPALZM Web Search
- 工具系列：QPALZM Toolkit
- 开发作者：AdkSetup
- 支持平台：macOS

---

<a id="english-documentation"></a>

macOS-only lightweight web search GUI tool, built with CustomTkinter. One-click access to Baidu and Bing search, with support for opening any custom URL directly.

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

---

## License

This project is licensed under the [MIT License](./LICENSE).
