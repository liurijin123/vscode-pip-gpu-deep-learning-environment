import sys

import torch


def main() -> None:
    print("Python:", sys.executable)
    print("PyTorch:", torch.__version__)
    print("PyTorch CUDA runtime:", torch.version.cuda)
    print("CUDA available:", torch.cuda.is_available())

    if not torch.cuda.is_available():
        raise RuntimeError(
            "PyTorch 当前无法使用 CUDA，请按文章中的排查顺序检查驱动、解释器和安装来源。"
        )

    device = torch.device("cuda:0")
    print("GPU:", torch.cuda.get_device_name(device))

    # 创建两个约 16 MB 的矩阵，并在 GPU 上执行矩阵乘法
    x = torch.randn((2048, 2048), device=device)
    y = torch.randn((2048, 2048), device=device)
    z = x @ y
    torch.cuda.synchronize(device)

    print("Result device:", z.device)
    print("Result shape:", tuple(z.shape))
    print("GPU environment check: PASSED")


if __name__ == "__main__":
    main()

