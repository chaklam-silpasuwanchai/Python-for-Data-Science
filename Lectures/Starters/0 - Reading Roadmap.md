# Paper Reading Roadmap

It is good to have some direction when you read deep learning papers.  This is not a comprehensive list of history of impactful papers, but aim to keep it as short as possible, while getting you as close to the state of the art, given the time you have in your project / thesis.  

I have estimated that if you read one paper a day, it should take you only around at most a month to understand the landscape.  Of course, you don't want to read everything but focus on what you want to work on in your thesis! 

Note: You MUST (99%) cite these works.  All these works are consider breakthrough in their field.  For example, I exclude AlexNet - although it is one of the most classic paper, it is now consider more classic than something that you must cite, since there are much better state-of-the-art like ResNet or EfficientNet.

## Top conferences

If you want to read, always start here.

- International Conference on Learning Representations (ICLR)
- Neural Information Processing Systems (NIPS)
- International Conference on Machine Learning (ICML)

## Starters

Overall picture.

- (2015) [Survey](http://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf)

## Image

Architectures for classifying images.

- (2015) [ResNet](https://arxiv.org/pdf/1512.03385.pdf), (2016) [ResNetv2](https://arxiv.org/abs/1603.05027), (2017) [ResNetv3](https://arxiv.org/abs/1611.05431)

## Data Augmentation

- (2018) [Excitation](https://arxiv.org/abs/1709.01507v4)

- (2019) [AutoAugment](https://arxiv.org/abs/1805.09501)

## NLP / Sequence

### RNN

Recurrent Neural Networks

- (2014) [LSTM](https://arxiv.org/abs/1308.0850)

- (2014) [GRU](https://arxiv.org/abs/1412.3555)

### Word Vectors

Effective way to represent words.

- (2013) [Word2Vec](https://arxiv.org/abs/1610.02357)

- (2017) [Subword](https://www.mitpressjournals.org/doi/abs/10.1162/tacl_a_00051)

- (2018) [Deep Word2Vec](https://arxiv.org/abs/1802.05365)

### Seq2Seq

Machine translation.

- (2014) [Seq2Seq](https://arxiv.org/abs/1409.3215)

- (2015) [AlignTranslate](https://arxiv.org/abs/1409.0473)

### Attention

Solving long-term dependencies.

- (2017) [Transformer](https://arxiv.org/abs/1706.03762)

### Unsupervised

Unsupervised, e.g., topic modeling, generating text

- (2018) [BERT](https://arxiv.org/abs/1810.04805)

- (2019) [XLNet](https://arxiv.org/abs/1906.08237)

## Neural Architecture Search

Automatically generating a neural network architecture .

- (2017) [NAS with RL](https://arxiv.org/abs/1611.01578)

- (2017) [PNAS](https://arxiv.org/abs/1712.00559)

- (2018) [DARTS](https://arxiv.org/abs/1806.09055)

- (2019) [Random Search](https://arxiv.org/abs/1902.07638)

- (2019) [AmoebaNet](https://arxiv.org/abs/1802.01548)

## Generative Models / Unsupervised

Learning the probability density function and thus able to generate, cluster, or style transfer samples from the distribution.  Hence is able to generate new data to address lack of data or loss of data.

### Variational Autoencoders

- (2016) [VAE Tutorial](https://arxiv.org/abs/1606.05908)

### Evaluation of Generative Models

- (2018) [Inception Score](https://arxiv.org/abs/1801.01973)

### Generative Adversarial Networks

- (2014) [GAN](https://arxiv.org/abs/1406.2661)

- (2017) [ProgressiveGAN](https://arxiv.org/abs/1710.10196)

- (2017) [WGAN](https://proceedings.neurips.cc/paper/2017/hash/892c3b1c6dccd52936e27cbd0ff683d6-Abstract.html)

- (2018) [SN-GAN](https://openreview.net/pdf?id=B1QRgziT-)

- (2018) [BigGAN](https://arxiv.org/abs/1809.11096)

- (2018) [StarGAN](https://arxiv.org/abs/1711.09020v3)

- (2019) [AttentionGAN](http://proceedings.mlr.press/v97/zhang19d.html)

### Style Transfer

- (2016) [Style Transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)

- (2017) [CycleGAN](https://arxiv.org/abs/1703.10593)

### Autoregressive Models

- (2016) [WaveNet](https://arxiv.org/abs/1609.03499)

- (2016) [PixelCNN](https://arxiv.org/abs/1606.05328)

### Normalizing Flows

- (2016) [RealNVP](https://arxiv.org/abs/1605.08803)

- (2018) [Glow](https://arxiv.org/abs/1807.03039)

## Object Detection

Extract locations and predict the class.

- (2015) [Faster R-CNN](https://arxiv.org/abs/1506.01497)

- (2016) [PointNet](https://arxiv.org/abs/1612.00593)

- (2017) [Mask R-CNN](https://arxiv.org/abs/1703.06870)

- (2019) [Mesh R-CNN](https://arxiv.org/abs/1906.02739)

## Meta Learning / Transfer Learning

Apply training to different learning problems.

- (2017) [Meta Learning](https://arxiv.org/abs/1703.03400)

- (2018) [NASNet](https://arxiv.org/abs/1707.07012v4)

## Image Caption

Generating image caption.

- (2015) [Show](https://arxiv.org/pdf/1502.03044v3.pdf)

- (2015) [Show2](http://openaccess.thecvf.com/content_cvpr_2015/html/Vinyals_Show_and_Tell_2015_CVPR_paper.html)

Question answering

- (2016) [Answer](https://arxiv.org/abs/1601.01705)

## Reinforcement Learning

Learn by doing.

- (2013) [Q-learning](https://arxiv.org/abs/1312.5602v1)

- (2016) [Go](https://www.nature.com/articles/nature16961)

- (2017) [Forgetting](https://www.pnas.org/content/114/13/3521.short)

## Theory

### Generalization

How to build generalized model across an entire distribution, not only on trained samples?

- (2016) [Rethinking Generalization](https://arxiv.org/abs/1611.03530)

- (2018) [Parameter Function Map](https://arxiv.org/abs/1805.08522)

### Robustness

How to build robust model that is robust against distribution shift?

- (2018) [Texture Bias](https://arxiv.org/abs/1811.12231)

- (2019) [Imagnet Generalization](https://arxiv.org/abs/1902.10811)

### Optimization

How to improve training procedure?

- (2013) [Momentum](http://www.jmlr.org/proceedings/papers/v28/sutskever13.pdf)

- (2014) [Drouput](http://jmlr.org/papers/v15/srivastava14a.html)

- (2014) [Adam](https://arxiv.org/abs/1412.6980)

- (2015) [Batch Norm](https://arxiv.org/abs/1502.03167)

- (2016) [Layer Norm](https://arxiv.org/abs/1607.06450)

- (2016) [Neural Optimzer](https://arxiv.org/pdf/1606.04474)

- (2016) [Hyperband](https://arxiv.org/abs/1603.06560)

- (2018) [Large Batch Training](https://arxiv.org/abs/1902.10811)

- (2018) [Parallel Hyperparameter Tuning](https://arxiv.org/abs/1810.05934)

- (2019) [Lookahead](https://arxiv.org/abs/1907.08610)

### Pruning

How to make the model more lean with less parameters but with similar accuracy? Or more lightweight?

- (2015) [Pruning](https://arxiv.org/abs/1510.00149)

- (2016) [SqueezeNet](https://arxiv.org/abs/1602.07360)

- (2017) [MobileNets](https://arxiv.org/abs/1704.04861)

- (2018) [Lottery Ticket](https://arxiv.org/abs/1803.03635)

- (2019) [EfficientNet](https://arxiv.org/abs/1905.11946)
