import os
import cv2
import tqdm
import torch
import argparse
import numpy as np
import open3d as o3d

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='Visualize a specific scene')
parser.add_argument('scene_number', type=int, help='The number of the scene to visualize')
parser.add_argument('-f', type=int, default=-1, help="The number of the frame of the scene to visualize")

# 解析命令行参数
args = parser.parse_args()

# 场景目录路径
scene_dir = '/home/dongzhipeng/Projects/Driv3R/output/nuscenes/'

# 构造点云文件路径
if (args.f == -1):  # 4D 点云可视化
    ply_file = os.path.join(scene_dir, f'scene_{args.scene_number}', 'pcd.ply')
else:  # 单帧点云可视化
    ply_file = os.path.join(scene_dir, f'scene_{args.scene_number}', f'pcd_frame_{args.f}.ply')

# 读取点云文件
print(ply_file)
pcd = o3d.io.read_point_cloud(ply_file)

# 可视化点云
o3d.visualization.draw_geometries([pcd])
