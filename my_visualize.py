import os
import sys
import numpy as np
import skimage.io

# 根目录
ROOT_DIR = os.path.abspath(".")

# Mask R-CNN 代码路径
sys.path.append(ROOT_DIR)
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn.config import Config
from mrcnn import visualize


# 自定义配置（与训练时一致）
class InferenceConfig(Config):
    NAME = "coco"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 6  # 背景+训练的类别数

config = InferenceConfig()

# 创建模型对象（推理模式）
model = modellib.MaskRCNN(mode="inference", config=config, model_dir="logs")

# 加载权重
model_path = "logs/coco20250610T1616/mask_rcnn_coco_0001.h5"  # 预训练权重路径
model.load_weights(model_path, by_name=True)

# 加载图片
image = skimage.io.imread("test2.jpg")  # 测试用图片路径

# 推理
results = model.detect([image], verbose=1)

# 查看结果
r = results[0]
print("检测到的类别：", r['class_ids'])
print("每个目标的分割掩码 shape：", r['masks'].shape)
print("每个目标的置信度：", r['scores'])

# 类别名列表，需训练时的类别顺序一致
class_names = ['BG', 'person', 'car', 'bus', 'truck', 'bicycle', 'motorcycle']  

visualize.display_instances(
    image, r['rois'], r['masks'], r['class_ids'],
    class_names, r['scores']
)