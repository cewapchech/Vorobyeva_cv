import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.io import imread
from pathlib import Path

save_path = Path(__file__).parent

def count_holes(region):
    shape = region.image.shape
    new_image = np.zeros((shape[0] + 2, shape[1] + 2))
    new_image[1:-1, 1:-1] = region.image
    new_image = np.logical_not(new_image)
    labeled = label(new_image)
    return np.max(labeled) - 1

def count_lines(region):
    shape =region.image.shape
    image = region.image
    vlines = (np.sum(image,0)/shape[0]==1),sum()
    hlines = (np.sum(image,1)/shape[1]==1),sum()
    return vlines, hlines

def symetry(region):
    shape=region.image.shape
    image=region.image
    top=image[:shape[0]//2]
    bottom=image[-shape[0]//2:]


def clasificator(region):
    holes=count_holes(region)
    if holes ==2: #B 8
        v,_=count_lines(region)
        v/=region.image.shape[1]
        if v>0.2:
            return "B"
        else:
            return "8"
    elif holes==1: #A 0
        pass
    elif holes==0: #1,W,X,*,-,/
        pass
    return "?"

image = imread("alphabet.png")[:, :, :-1]
binary_alphabet = image.mean(2) > 0
alabeled = label(binary_alphabet)
aprops = regionprops(alabeled)
result = {}
image_path = save_path/"out_tree"
image_path.mkdir(exist_ok = True)

#plt.ion()
plt.figure(figsize = (5, 7))

for region in aprops:
    symbol = classificator(region)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
    plt.cla()
    plt.title(f"Class - '{symbol}'")
    plt.imshow(region.image)
    plt.savefig(image_path/f"image_{region.label}.png")
print(result)

plt.imshow(alabeled)
plt.show()