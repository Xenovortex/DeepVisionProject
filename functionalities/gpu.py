import torch

def get_device(dev_idx=0):
    """
    Check if GPU is available and select GPU base on provided device index.

    :param dev_idx: index of the GPU device to use (if your PC has multiple GPU's). Default: 0
    :return: device variable used for further training on the GPU
    """

    torch.cuda.set_device(dev_idx)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
   

    return device
