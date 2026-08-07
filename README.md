# QPALZM Web Search

> [English Documentation](./README.en.md)

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
| WebSearch.dmg | macOS | Mac 标准安装包，拖拽至应用程序即可使用 |
| WebSearch_Mac.zip | macOS | 绿色压缩包，解压后直接运行 |

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
