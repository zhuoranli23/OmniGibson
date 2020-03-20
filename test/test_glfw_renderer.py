from gibson2.core.render.mesh_renderer.mesh_renderer_vr import MeshRendererVR
from gibson2.core.render.mesh_renderer.mesh_renderer_cpu import MeshRenderer
import cv2
import sys
import numpy as np
from gibson2.core.render.mesh_renderer.mesh_renderer_cpu import VisualObject, InstanceGroup, MeshRenderer
import time

renderer = MeshRendererVR(MeshRenderer)
""" renderer.load_object("C:\\Users\\shen\\Desktop\\GibsonVRStuff\\gibsonv2\\gibson2\\assets\\datasets\\Ohoopee\\Ohoopee_mesh_texture.obj")
renderer.add_instance(0)

print(renderer.visual_objects, renderer.instances)
print(renderer.materials_mapping, renderer.mesh_materials)
camera_pose = np.array([0, 0, 1.2])
view_direction = np.array([1, 0, 0])
renderer.set_camera(camera_pose, camera_pose + view_direction, [0, 0, 1])
renderer.set_fov(90)

px = 0
py = 0

_mouse_ix, _mouse_iy = -1, -1
down = False

def change_dir(event, x, y, flags, param):
    global _mouse_ix, _mouse_iy, down, view_direction
    if event == cv2.EVENT_LBUTTONDOWN:
        _mouse_ix, _mouse_iy = x, y
        down = True
    if event == cv2.EVENT_MOUSEMOVE:
        if down:
            dx = (x - _mouse_ix) / 100.0
            dy = (y - _mouse_iy) / 100.0
            _mouse_ix = x
            _mouse_iy = y
            r1 = np.array([[np.cos(dy), 0, np.sin(dy)], [0, 1, 0], [-np.sin(dy), 0, np.cos(dy)]])
            r2 = np.array([[np.cos(-dx), -np.sin(-dx), 0], [np.sin(-dx), np.cos(-dx), 0], [0, 0, 1]])
            view_direction = r1.dot(r2).dot(view_direction)
    elif event == cv2.EVENT_LBUTTONUP:
        down = False

cv2.namedWindow('GLFW Renderer Test')
cv2.setMouseCallback('test', change_dir)

while True:
    frame = renderer.render(vrMode=False)
    cv2.imshow('test', cv2.cvtColor(np.concatenate(frame, axis=1), cv2.COLOR_RGB2BGR))
    q = cv2.waitKey(1)
    if q == ord('w'):
        px += 0.05
    elif q == ord('s'):
        px -= 0.05
    elif q == ord('a'):
        py += 0.05
    elif q == ord('d'):
        py -= 0.05
    elif q == ord('q'):
        break
    camera_pose = np.array([px, py, 1.2])
    print("new camera pose")
    print(camera_pose)
    renderer.set_camera(camera_pose, camera_pose + view_direction, [0, 0, 1])

renderer.release()"""