#Code Created by PhamNghia

import torch
#Torch version
print("Torch version-->"+torch.__version__)
#GPU Selected
print("GPU selected-->",torch.cuda.device(0))
#CUDA Available?
print("GPU 0 is available?-->",torch.cuda.is_available())
print("GPU 0 name-->"+torch.cuda.get_device_name(0))
print("Current GPU-->",torch.cuda.current_device())
print("GPU count-->",torch.cuda.device_count())
