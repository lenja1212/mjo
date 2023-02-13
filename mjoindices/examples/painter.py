import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from pathlib import Path

def rotate_vector(data, angle):
    # make rotation matrix
    theta = np.radians(angle)
    co = np.cos(theta)
    si = np.sin(theta)
    rotation_matrix = np.array(((co, -si), (si, co)))
    # rotate data vector
    rotated_vector = data.dot(rotation_matrix)
    return rotated_vector

def form_data(arr1, arr2):
  data =[]
  for i in range(len(arr1)):
    data.append([arr1[i], arr2[i]])
  return np.array(data)


def drawPc(pc_text_file: Path, pc_png_file: Path, inverse1 = 1, inverse2 = 1):
    pc1 = []
    pc2 = []
    days = np.arange(0, 93, 1, dtype=int)
    #  PCs2     PsCs
    print("path pc: ", pc_text_file)
    print("path graph: ", pc_png_file)
    with open(pc_text_file) as f1:
        next(f1)
        for line in f1:
            if line != ['']:
                line = line.split(",")
                pc1.append(inverse1 * float(line[1]))
                pc2.append(inverse2 * float(line[2]))

    fig, ax = plt.subplots()

    jan_arr_pc1 = pc1[0:31]
    feb_arr_pc1 = pc1[31:59]
    mar_arr_pc1 = pc1[59:90]
    jan_arr_pc2 = pc2[0:31]
    feb_arr_pc2 = pc2[31:59]
    mar_arr_pc2 = pc2[59:90]
    text31 = np.arange(1, 32, 1, dtype=int)
    text28 = np.arange(1, 29, 1, dtype=int)

    # print(form_data(jan_arr_pc1, jan_arr_pc2))
    # rotated_data = rotate_vector(form_data(jan_arr_pc1, jan_arr_pc2), -10)
    # plt.plot(jan_arr_pc1, jan_arr_pc2, color='red', ms=2, label='old')
    # plt.plot(rotated_data[:, 0], rotated_data[:, 1], color='blue', ms=2, label='new')
    # plt.show()
    # exit()

    # plt.annotate("START", (jan_arr_pc1[0], jan_arr_pc2[0] + 0.2), fontsize=8)
    # for i in range(1,len(text31)):
    #     plt.annotate(text31[i], (jan_arr_pc1[i], jan_arr_pc2[i] + 0.2), fontsize=5)
    for i in range(0,len(text31)-1):  
        plt.annotate(text31[i], (mar_arr_pc1[i], mar_arr_pc2[i] + 0.2), fontsize=5)
    plt.annotate("FINISH", (mar_arr_pc1[-1], mar_arr_pc2[-1] + 0.2), fontsize=8)
    for i in range(len(text28)):
        plt.annotate(text28[i], (feb_arr_pc1[i], feb_arr_pc2[i] + 0.2), fontsize=5)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.xlabel('$PC1$')
    plt.ylabel('$PC2$')
    rotated_data = rotate_vector(form_data(jan_arr_pc1, jan_arr_pc2), 0) # 0 -> -10
    plt.plot(rotated_data[:, 0], rotated_data[:, 1], '-o', color='red', ms=2, label='jan', linewidth=2)

    plt.annotate("START", (rotated_data[:,0][0], rotated_data[:,1][0] + 0.2), fontsize=8)
    for i in range(1,len(text31)):
        plt.annotate(text31[i], (rotated_data[:,0][i], rotated_data[:,1][i] + 0.2), fontsize=5)
      
    # rotated_data = rotate_vector(form_data(jan_arr_pc1[-1], feb_arr_pc1[0]), -10)
    # plt.plot([jan_arr_pc1[-1], feb_arr_pc1[0]], [jan_arr_pc2[-1], feb_arr_pc2[0]], '-', color='chartreuse', ms=2, linewidth=2)
    rotated_data = rotate_vector(form_data(feb_arr_pc1, feb_arr_pc2), 0)
    plt.plot(feb_arr_pc1, feb_arr_pc2,'-o', color='chartreuse', ms=2, label='feb')
    # rotated_data = rotate_vector(form_data(jan_arr_pc1, jan_arr_pc2), -10)
    # plt.plot([feb_arr_pc1[-1], mar_arr_pc1[0]], [feb_arr_pc2[-1], mar_arr_pc2[0]], '-', color='blue', ms=2)
    rotated_data = rotate_vector(form_data(mar_arr_pc1, mar_arr_pc2), 0)
    plt.plot(mar_arr_pc1, mar_arr_pc2, '-o', color='blue', ms=2, label='mar')

    for i in range(0,len(text31)-1):  
        plt.annotate(text31[i], (rotated_data[:,0][i], rotated_data[:,1][i] + 0.2), fontsize=5)
    plt.annotate("FINISH", (mar_arr_pc1[-1], mar_arr_pc2[-1] + 0.2), fontsize=8)
    plt.legend()

    #add Circle
    circle1 = plt.Circle((0, 0), 1, color='k', fill=False, linewidth=1)
    ax.plot([0, 1], [0, 1], transform=ax.transAxes, color='k', linewidth = 0.5, ls="--" )
    ax.plot([1, 0], [0, 1], transform=ax.transAxes, color='k', linewidth = 0.5, ls="--" )
    ax.plot([0, 1], [0.5, 0.5], transform=ax.transAxes, color='k', linewidth = 0.5, ls="--" )
    ax.plot([0.5, 0.5], [0, 1], transform=ax.transAxes, color='k', linewidth = 0.5, ls="--" )
    # plt.text(-0.6, 0, "Weak MJO", fontsize=10, weight='bold')
    ax.add_artist(circle1)

    is_exist = os.path.exists(pc_png_file)
    if not is_exist:
        os.makedirs(pc_png_file)
    fig_name = os.path.basename(pc_png_file)
    plt.savefig(f'{pc_png_file}/{fig_name}_{inverse1}_{inverse2}.png')
