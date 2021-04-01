import os
import argparse
import numpy as np
import torch
from torchvision import transforms
from PIL import Image

parser = argparse.ArgumentParser('Running script', add_help=False)
parser.add_argument('--input_dir', default='../input_dir', type=str)
parser.add_argument('--output_dir', default='../output_dir', type=str)

class ImageNetDataset(torch.utils.data.Dataset):

    def __init__(self, data_dir, meta_file, transform=None):

        self.data_dir = data_dir
        self.meta_file = meta_file
        self.transform = transform
        self._indices = []

        with open(os.path.join(data_dir, meta_file)) as f:
            for line in f.readlines()[1:]:
                img_path, label = line.strip().split(',')
                self._indices.append((os.path.join(self.data_dir, 'images', img_path), label))

    def __len__(self): 
        return len(self._indices)

    def __getitem__(self, index):
        img_path, label = self._indices[index]
        img = Image.open(img_path).convert('RGB')
        label = int(label)
        img_name = img_path.split('/')[-1]
        if self.transform is not None:
            img = self.transform(img)
        return img, label, img_name

def tensor2img(input_tensor, save_dir, save_name):

    if input_tensor.is_cuda == True:
        input_tensor = input_tensor.cpu()

    input_tensor = input_tensor.permute(0, 2, 3, 1).data.numpy()
    for i in range(input_tensor.shape[0]):
        Image.fromarray((input_tensor[i] * 255).astype(np.uint8)).save('{}/{}'.format(save_dir, save_name[i]))
        print('{} saved in {}.'.format(save_name[i], save_dir))

if __name__ == '__main__':

    args = parser.parse_args()

    dataset = ImageNetDataset(data_dir=args.input_dir, meta_file='dev.csv', transform=transforms.ToTensor())
    data_loader = torch.utils.data.DataLoader(
            dataset, batch_size=1, shuffle=False, num_workers=4)

    for inputs, targets, img_name in data_loader:

        noise = torch.empty(inputs.shape).normal_(std=0.2)
        if torch.cuda.is_available():
            inputs = inputs.cuda()
            targets = targets.cuda()
            noise = noise.cuda()

        output_data = torch.clamp(inputs + noise, 0, 1)
        tensor2img(input_tensor=output_data, save_dir=args.output_dir, save_name=img_name)
    
