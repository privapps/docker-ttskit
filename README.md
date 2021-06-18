## What
提供中文文字转语音(Text To Speech / TTS) 的库/软件
这是拥有最基本 [ttskit](https://github.com/KuangDD/ttskit) 功能的 衍生 包括
* [Github Action](https://github.com/privapps/docker-ttskit/tree/action)
* [Docker Image Tool](https://github.com/privapps/docker-ttskit/tree/tool)

## 如何使用
#### 参看上面的两个链接

## Why
ttskit语音生成的效果不错，但是有很多第三方库，还有一些训练过的数据。如果是一台新机器，需要很长时间下载，设置。这里把所有打包好了，可以拿起来马上用

**注： 只支持中文**

`吃葡萄不吐葡萄皮儿，不吃葡萄倒吐葡萄皮儿。床前明月光，一阵美人香。不知春梦里，枉自硬帮帮。一 二 三 四 五 六 七 八 九 十。 Hello World`

 | id | 简介 | URL | 其他 | 
 | ------------- |:-------------:| ----- | --- |
 | 0 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/0.mp3 |  | 
 | 1 | 孩 | https://github.com/privapps/docker-ttskit/raw/samples/1.mp3 |  | 
 | 2 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/2.mp3 |  | 
 | 3 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/3.mp3 |  | 
 | 4 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/4.mp3 |  | 
 | 5 | 中 | https://github.com/privapps/docker-ttskit/raw/samples/5.mp3 |  | 
 | 6 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/6.mp3 |  | 
 | 7 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/7.mp3 |  | 
 | 8 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/8.mp3 |  | 
 | 9 | 孩 | https://github.com/privapps/docker-ttskit/raw/samples/9.mp3 |  | 
 | 10 | 孩 | https://github.com/privapps/docker-ttskit/raw/samples/10.mp3 |  | 
 | 11 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/11.mp3 |  | 
 | 12 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/12.mp3 | 快 | 
 | 13 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/13.mp3 | 快 | 
 | 14 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/14.mp3 |  | 
 | 15 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/15.mp3 | 快 | 
 | 16 | 孩 | https://github.com/privapps/docker-ttskit/raw/samples/16.mp3 |  | 
 | 17 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/17.mp3 |  | 
 | 18 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/18.mp3 |  | 
 | 19 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/19.mp3 |  | 
 | 20 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/20.mp3 |  | 
 | 21 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/21.mp3 |  | 
 | 22 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/22.mp3 |  | 
 | 23 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/23.mp3 |  | 
 | 24 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/24.mp3 |  | 
 | 25 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/25.mp3 | 快 | 
 | 26 | ? | https://github.com/privapps/docker-ttskit/raw/samples/26.mp3 |  | 
 | 27 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/27.mp3 |  | 
 | 28 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/28.mp3 |  | 
 | 29 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/29.mp3 |  | 
 | 30 | 男 | https://github.com/privapps/docker-ttskit/raw/samples/30.mp3 |  | 
 | 31 | 女 | https://github.com/privapps/docker-ttskit/raw/samples/31.mp3 |  | 

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

### 相关项目
 * [TTSKIT](https://github.com/KuangDD/ttskit)
 * [TTS Action](https://github.com/l-O-O-l/TTS-action/blob/dev/README_CN.md) 一个提供免费转文字的服务
