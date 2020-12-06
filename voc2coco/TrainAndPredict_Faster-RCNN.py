import detectron2
from detectron2.utils.logger import setup_logger

setup_logger()

# import some common libraries
import numpy as np
import cv2
import random
import datetime
import time
import os

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data.datasets import register_coco_instances
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.engine import DefaultTrainer
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode


def Train():
    register_coco_instances("custom", {}, "/home/lsc/datasets/butterfly/Annotations/train.json",
                            "/home/lsc/datasets/butterfly/TrainData/JPEGImages")
    custom_metadata = MetadataCatalog.get("custom")
    dataset_dicts = DatasetCatalog.get("custom")

    cfg = get_cfg()
    cfg.merge_from_file(
        "/home/lsc/detectron2/configs/COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml"
    )
    cfg.DATASETS.TRAIN = ("custom",)
    cfg.DATASETS.TEST = ()
    cfg.DATALOADER.NUM_WORKERS = 8
    cfg.MODEL.WEIGHTS = 'detectron2://COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x/139173657/model_final_68b088.pkl'
    cfg.SOLVER.IMS_PER_BATCH = 2
    cfg.SOLVER.BASE_LR = 0.02
    cfg.SOLVER.MAX_ITER = (
        500
    )
    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = (
        128
    )
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 94

    os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
    trainer = DefaultTrainer(cfg)
    trainer.resume_or_load(resume=False)
    trainer.train()


def Predict():
    register_coco_instances("custom", {}, "datasets/coco/annotations/instances_train2014.json",
                            "datasets/coco/train2014")
    custom_metadata = MetadataCatalog.get("custom")
    DatasetCatalog.get("custom")

    cfg = get_cfg()
    cfg.merge_from_file("/home/lsc/detectron2/configs/COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml")
    cfg.DATASETS.TEST = ("custom",)
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = (
        128
    )
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 94
    predictor = DefaultPredictor(cfg)




if __name__ == "__main__":
    Train()
    # Predict()
