# Paper Reading Roadmap

It is good to have some direction when you read deep learning papers.  This is not a comprehensive list of history of impactful papers, but aim to keep it as short as possible, while getting you as close to the state of the art, given the time you have in your project / thesis.

## Starters

Read to get overall picture.

- (2015) [Survey](http://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf)

## Image

Architectures for classifying images.

- (2015) [ResNet](https://arxiv.org/pdf/1512.03385.pdf), [ResNetv2](https://arxiv.org/abs/1603.05027), [ResNetv3](https://arxiv.org/abs/1611.05431)

## Data Augmentation

- (2018) [AutoAugment](https://arxiv.org/abs/1805.09501)

- (2018) [Excitation](https://arxiv.org/abs/1709.01507v4)

## Sequence-to-sequence / RNN (text / signals)

- (2013) [LSTM](http://arxiv.org/pdf/1308.0850)

- (2014) [First Seq2Seq](http://arxiv.org/pdf/1406.1078)


## NLP

### Word Vectors

Effective way to represent words.

- (2013) [Word2Vec](https://arxiv.org/abs/1610.02357)

- (2018) [Deep Word2Vec](https://arxiv.org/abs/1802.05365)

### Seq2Seq

Machine translation.

- (2014) [Seq2Seq](https://arxiv.org/pdf/1409.3215.pdf)

- (2014) [AlignTranslate](https://arxiv.org/abs/1409.0473)

### Attention

Solving long-term dependencies.

- (2017) [Transformer](https://arxiv.org/abs/1706.03762)

### Unsupervised

Unsupervised, e.g., topic modeling, generating text

- (2018) [BERT](https://arxiv.org/abs/1810.04805)


## Neural Architecture Search

Automatically generating a neural network architecture .

- (2017) [NAS with RL](https://arxiv.org/abs/1611.01578)

- (2017) [PNAS](https://arxiv.org/abs/1712.00559)

- (2018) [DARTS](https://arxiv.org/abs/1806.09055)

- (2019) [Random Search](https://arxiv.org/abs/1902.07638)

## Generative Models / Unsupervised

Learning the probability density function and thus able to generate, cluster, or style transfer samples from the distribution.

### Variational Autoencoders

- (2016) [VAE Tutorial](https://arxiv.org/abs/1606.05908)

### Evaluation of Generative Models

- (2018) [Inception Score](https://arxiv.org/abs/1801.01973)

### Generative Adversarial Networks

- (2014) [GAN](https://arxiv.org/abs/1406.2661)

- (2018) [SN-GAN](https://openreview.net/pdf?id=B1QRgziT-)

- (2018) [BigGAN](https://arxiv.org/abs/1809.11096)

- (2018) [StarGAN](https://arxiv.org/abs/1711.09020v3)

- (2019) [AttentionGAN](http://proceedings.mlr.press/v97/zhang19d.html)

### Style Transfer

- (2016) [Style Transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)

- (2017) [CycleGAN](https://arxiv.org/abs/1703.10593)

### Autoregressive Models

- (2016) [PixelCNN](https://arxiv.org/abs/1606.05328)

- (2016) [WaveNet](https://arxiv.org/abs/1609.03499)

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

## Reinforcement Learning

Learn by doing.

- (2016) [Go](https://www.nature.com/articles/nature16961)

- (2017) [Forgetting](https://www.pnas.org/content/114/13/3521.short)

## Theory

Generalization: How to build generalized model across an entire distribution, not only on trained samples?

Robustness: How to build robust model that is robust against distribution shift?

Optimization: How to best improve training procedure?

Pruning: How to make the model more lean with less parameters but with similar accuracy?

- (2013) [Momentum](http://www.jmlr.org/proceedings/papers/v28/sutskever13.pdf)

- (2014) [Drouput](http://jmlr.org/papers/v15/srivastava14a.html)

- (2014) [Adam](https://arxiv.org/abs/1412.6980)

- (2015) [Batch Norm](https://arxiv.org/abs/1502.03167)

- (2015) [Pruning](https://arxiv.org/abs/1510.00149)

- (2016) [Neural Optimzer](https://arxiv.org/pdf/1606.04474)

- (2016) [Rethinking Generalization](https://arxiv.org/abs/1611.03530)

- (2016) [SqueezeNet](https://arxiv.org/abs/1602.07360)

- (2018) [Parameter Function Map](https://arxiv.org/abs/1805.08522)

- (2018) [Texture Bias](https://arxiv.org/abs/1811.12231)

- (2018) [Lottery Ticket](https://arxiv.org/abs/1803.03635)

- (2018) [Large Batch Training](https://arxiv.org/abs/1902.10811)

- (2019) [Imagnet Generalization](https://arxiv.org/abs/1902.10811)

- (2019) [EfficientNet](https://arxiv.org/abs/1905.11946)
