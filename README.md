# Submit template for CVPR-2021 AIC-VI: Unrestricted Adversarial Attacks on ImageNet

## Dos and Don'ts

- Do use GPUs to accelerate the running of your code.

- Don't using 5000 test images and `dev.csv` to train any substitution model or finetune your model parameters. We only allow the model inference at final evaluation stage.

## Usage

- First you need clone the this repository
```
git clone https://github.com/vtddggg/submit_template_for_AI_challenger_sea6.git
cd submit_template_for_AI_challenger_sea6
```
In this template, we provide some example images in `input_dir/images` and label file `dev.csv` in `input_dir`.

- Build your custom running environment by Dockerfile

```
docker build -t securityaicompetition/season6:v1 .
```
Note that this command will copy `code` folder into your custom docker image.

- Run the docker image

for people who need GPUs to run, `nvidia-docker` must be installed:

```
nvidia-docker run -v $(pwd)/input_dir:/workspace/input_dir -v $(pwd)/output_dir:/workspace/output_dir -w /workspace/code securityaicompetition/season6:v1 python run.py
```

otherwise:
```
docker run -v $(pwd)/input_dir:/workspace/input_dir -v $(pwd)/output_dir:/workspace/output_dir -w /workspace/code securityaicompetition/season6:v1 python run.py
```


- Finally if you can see some generated images in `output_dir` folder, it means you run the example code successfully. Congratulations!

## Submit

- Once you have run this template code successfully, you can next move your implementation code into `code` folder. And then modify the `Dockerfile` to add the dependencies of your implementation. 

- If the code can successfully produce the result images in `output_dir` folder, everything is ok! You can submit this to us.



# AI安全挑战者计划第六期ImageNet无限制攻击比赛提交示例

## 注意事项

- 尽量使用GPU加速攻击算法的运行

- 不要使用5000张用于测试的图像和对应标签去训练任何替代模型或者在已有模型参数上finetune。在最终测试阶段，我们只允许利用模型的进行测试

## 使用方法

- 首先您需要clone我们的提交模版
```
git clone https://github.com/vtddggg/submit_template_for_AI_challenger_sea6.git
cd submit_template_for_AI_challenger_sea6
```
此模版中，我们在`input_dir/images`文件夹下提供了一些示例图像以供调试，并且标签文件`dev.csv`放置在`input_dir`下.

- 使用Dockerfile构建镜像

```
docker build -t securityaicompetition/season6:v1 .
```
此操作会把`code`文件夹打入镜像

- 运行镜像获得输出

如果您的算法需要GPU来运行，则需要提前安装`nvidia-docker`:

```
nvidia-docker run -v $(pwd)/input_dir:/workspace/input_dir -v $(pwd)/output_dir:/workspace/output_dir -w /workspace/code securityaicompetition/season6:v1 python run.py
```

否则:
```
docker run -v $(pwd)/input_dir:/workspace/input_dir -v $(pwd)/output_dir:/workspace/output_dir -w /workspace/code securityaicompetition/season6:v1 python run.py
```


- 运行后如果有在`output_dir`文件夹中生成图像，说明您成功了运行了提交的示例代码！

## 提交说明

- 一旦您成功跑通了我们的提交模版，接下来您需要把您的方法移入`code`文件夹下，并且修改`Dockerfile`来定制运行提交方案需要的额外环境和依赖库

- 如果您成功的运行了自己的方案，并且可以在`output_dir`文件夹下生成结果图像，那么一切就绪！您可以将此目录打包进行提交
