## What
这是拥有最基本 [ttskit](https://github.com/KuangDD/ttskit)功能的 docker image

## Why
ttskit语音生成的效果不错，但是有很多第三方库，还有一些训练过的数据。如果是一台新机器，需要很长时间下载，设置。这里把所有打包好了，可以拿起来马上用

## Usage
```
echo "需要转换的文字" > __input__.txt
echo 17 > __voice__.txt
docker run --rm -v .:/workspace privapps/ttskit

# out put should at __out__.wav
```
其中 `__voice__.txt` 是可选项，里面是语音的ID，具体一共有30个不同的语音
```
{
    1: 'Aibao', 2: 'Aicheng', 3: 'Aida', 4: 'Aijia', 5: 'Aijing',
    6: 'Aimei', 7: 'Aina', 8: 'Aiqi', 9: 'Aitong', 10: 'Aiwei',
    11: 'Aixia', 12: 'Aiya', 13: 'Aiyu', 14: 'Aiyue', 15: 'Siyue',
    16: 'Xiaobei', 17: 'Xiaogang', 18: 'Xiaomei', 19: 'Xiaomeng', 20: 'Xiaowei',
    21: 'Xiaoxue', 22: 'Xiaoyun', 23: 'Yina', 24: 'biaobei', 25: 'cctvfa',
    26: 'cctvfb', 27: 'cctvma', 28: 'cctvmb', 29: 'cctvmc', 30: 'cctvmd'
}
```
部分演示可以在[这里找到小样](https://github.com/KuangDD/zhrtvc/tree/master/data/files/examples)
