# 项目核心代码概览
## [coco.py](./samples/coco/coco.py)
用于COCO 数据集的训练、评估、推理主脚本。

定义了 COCO 数据集的加载方式（CocoDataset 类）
配置参数（CocoConfig 类）
支持命令行训练、评估、推理等多种模式

**主要结构**

***CocoConfig***
继承自 mrcnn.config.Config，设置 COCO 任务的参数（如类别数、batch size、学习率等）。

***CocoDataset***
继承自 mrcnn.utils.Dataset，实现 COCO 格式数据的加载、解析、mask 生成等。

***main*** 
解析命令行参数，根据 train、evaluate、detect 等命令调用不同流程。


# [config.py](./mrcnn/config.py)
**定义**所有 Mask R-CNN 训练和推理的参数配置。

通过继承 **Config** 类，可以定制训练参数（如类别数、图片尺寸、batch size、学习率等）。
主要内容：

**Config 类**：包含所有可配置参数的默认值
子类通过覆盖属性实现自定义

# [model.py](./mrcnn/model.py)
核心文件，实现了 Mask R-CNN 的全部模型结构、训练、推理、损失函数、数据生成等。

MaskRCNN 类

- **__init__**：初始化模型

- **build**：构建网络结构（ResNet+FPN+RPN+ROIAlign+Head）
- **train**：训练主流程，支持断点续训、日志保存、回调
- **detect**：推理主流程，对输入图片输出检测和分割结果
- **load_weights / find_last**：权重加载与管理
- **unmold_detections**：将网络输出转为实际图片上的检测框、mask、类别等
- **其它辅助函数**: ProposalLayer、PyramidROIAlign 等自定义 Keras 层
实现 RPN、ROIAlign、FPN 等关键模块。
- **损失函数实现**
- rpn_class_loss_graph
- rpn_bbox_loss_graph
- mrcnn_class_loss_graph
- mrcnn_bbox_loss_graph

- **数据生成器**
- **data_generator**：训练/验证时的数据批量生成

# [utils.py](./mrcnn/utils.py)
提供大量常用工具函数，包括 mask 处理、IoU 计算、数据增强、图片 resize、权重下载等。

- **resize_image、resize**：图片和 mask 的缩放

- **extract_bboxes、compute_iou、compute_overlaps**：目标检测常用的 bbox、IoU 计算

- **minimize_mask、expand_mask**：mask 的压缩与还原

- **download_trained_weights**：自动下载 COCO 预训练权重

- **Dataset 基类**：自定义数据集时继承

# [visualize.py](./mrcnn/visualize.py)
分割结果、检测框、mask、类别等的可视化显示和保存。

- **display_instances**：在图片上绘制检测框、mask、类别名、置信度

- **apply_mask**：将 mask 叠加到图片上

- **random_colors**：生成可视化用的随机颜色

- **display_images**：批量显示图片

# 注意事项
  [**requirements.txt**](./requirements.txt):
- 由于matterport发布的时间较早，使用的库函数都是比较老的版本，特别注意由于tensorflow的版本较老，所以只支持较低版本的python，推荐使用python 3.6/3.7

**setup.py / setup.cfg / MANIFEST.in**
- 开源项目Matterport的项目安装脚本和元数据等，与本课程项目无关

**可能忽略的问题**
- utils.py 的 Dataset 类
所有自定义数据集都要继承它，实现load_coco 和 load_mask 方法。

[LICENSE](./LICENSE)

# 训练过程中输出参数的含义
## 1. loss（总损失）
所有子损失（rpn_class_loss、rpn_bbox_loss、mrcnn_class_loss、mrcnn_bbox_loss、mrcnn_mask_loss）之和。
典型范围：初始一般在 2~5，训练后期会降到 1 以下，甚至 0.5 以下。
判断标准：loss 越低越好，但不能过于低下，甚至为0，这是过拟合的表现。这个参数持续下降说明模型在收敛。
### 子损失
1. rpn_class_loss（RPN分类损失）
- RPN 区域建议网络
- 判断 anchor 是前景还是背景的分类损失。
典型范围：0.01~0.1，训练后趋于 0.01~0.05。这个参数可以说明 RPN 能否较好地区分前景和背景。
1. rpn_bbox_loss（RPN回归损失）
- RPN 区域建议网络
- 预测 anchor 框与真实框的回归损失。
典型范围：0.1~0.5，训练后趋于 0.1~0.2。

1. mrcnn_class_loss（检测头分类损失）
- Mask R-CNN 检测头对 ROI 内目标类别的分类损失。
典型范围：0.2~0.7，训练后趋于 0.1~0.3。
1. mrcnn_bbox_loss（检测头回归损失）
- Mask R-CNN 检测头对 ROI 内目标框的回归损失。
典型范围：0.2~0.7，训练后趋于 0.1~0.3。
1. mrcnn_mask_loss（mask分支损失）
- Mask R-CNN mask 分支预测的分割掩码与真实 mask 的差异。
典型范围：0.2~0.7，初始较高，训练后趋于 0.1~0.3。

# 训练参数输出样例
第182个epoch的参数
182/1000 [====>.........................] - ETA: 4:22:48 - loss: 1.2853 - rpn_class_loss: 0.0227 - rpn_bbox_loss: 0.2909 - mrcnn_class_loss: 0.1975 - mrcnn_bbox_loss: 0.3833 - mrcnn_mask_loss: 0.3908coco.py:265: Deprecation

