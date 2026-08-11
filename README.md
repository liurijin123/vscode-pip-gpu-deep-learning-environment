# VS Code + pip GPU 深度学习环境验证

GitHub 仓库：<https://github.com/liurijin123/vscode-pip-gpu-deep-learning-environment>

仓库状态：已于 2026-08-11 上传并验证 `main` 分支。

本目录对应文章：

```text
drafts/2026-08-10-VSCode与pip从零搭建GPU深度学习环境/ARTICLE.md
```

适用环境：Windows 10/11 64 位、NVIDIA GPU、Python 3.13。

## 在 VS Code 中运行

用 VS Code 直接打开本目录，然后在集成终端依次执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip config --site set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip config --site list
python -m pip install -r requirements-torch-cu126.txt
python -m pip install -r requirements-tools.txt
python -m pip check
python check_gpu.py
```

上述镜像设置只写入当前 `.venv`。`requirements-torch-cu126.txt` 内部指定了 PyTorch 官方 CUDA 12.6 索引，因此安装 PyTorch 时不会改用普通 PyPI 镜像。若要取消当前环境的镜像配置，执行：

```powershell
python -m pip config --site unset global.index-url
```

如果 PowerShell 禁止执行激活脚本，可以将 VS Code 终端切换为“命令提示符”，再执行：

```bat
.venv\Scripts\activate.bat
```

运行成功至少应同时满足：

- `Python` 路径位于本目录的 `.venv`；
- `CUDA available` 为 `True`；
- `GPU` 显示正确的 NVIDIA 显卡型号；
- `Result device` 为 `cuda:0`；
- 最后一行显示 `GPU environment check: PASSED`。

示例版本核对于 2026-08-11。若 PyTorch 官方安装命令已经变化，应先更新 `requirements-torch-cu126.txt`，再运行测试。

pip 镜像配置参考：[清华大学开源软件镜像站 PyPI 使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)。
