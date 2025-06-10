参数的含义
1. loss（总损失）
含义：所有子损失（rpn_class_loss、rpn_bbox_loss、mrcnn_class_loss、mrcnn_bbox_loss、mrcnn_mask_loss）之和。
典型范围：初始一般在 2~5，训练后期会降到 1 以下，甚至 0.5 以下。
你的数值：1.8~1.9，属于训练初期的正常水平，说明模型正在学习，loss 还会继续下降。
判断标准：loss 越低越好，但不能为0。持续下降说明模型在收敛。
2. rpn_class_loss（RPN分类损失）
含义：RPN 区域建议网络判断 anchor 是前景还是背景的分类损失。
典型范围：0.01<del>0.1，初始可能高一点，训练后趋于 0.01</del>0.05。
你的数值：0.026~0.03，属于正常范围，说明 RPN 能较好地区分前景和背景。
3. rpn_bbox_loss（RPN回归损失）
含义：RPN 区域建议网络预测 anchor 框与真实框的回归损失。
典型范围：0.1<del>0.5，初始可能更高，训练后趋于 0.1</del>0.2。
你的数值：0.33~0.35，属于正常范围，后期会继续下降。
4. mrcnn_class_loss（检测头分类损失）
含义：Mask R-CNN 检测头对 ROI 内目标类别的分类损失。
典型范围：0.2<del>0.7，初始较高，训练后趋于 0.1</del>0.3。
你的数值：0.37~0.39，属于正常范围，后期会继续下降。
5. mrcnn_bbox_loss（检测头回归损失）
含义：Mask R-CNN 检测头对 ROI 内目标框的回归损失。
典型范围：0.2<del>0.7，初始较高，训练后趋于 0.1</del>0.3。
你的数值：0.58~0.60，略高但正常，后期会继续下降。
6. mrcnn_mask_loss（mask分支损失）
含义：Mask R-CNN mask 分支预测的分割掩码与真实 mask 的差异。
典型范围：0.2<del>0.7，初始较高，训练后趋于 0.1</del>0.3。
你的数值：0.52~0.54，属于正常范围，后期会继续下降。


第182个epoch的参数
182/1000 [====>.........................] - ETA: 4:22:48 - loss: 1.2853 - rpn_class_loss: 0.0227 - rpn_bbox_loss: 0.2909 - mrcnn_class_loss: 0.1975 - mrcnn_bbox_loss: 0.3833 - mrcnn_mask_loss: 0.3908coco.py:265: Deprecation

