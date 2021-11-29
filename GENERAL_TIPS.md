Data Science is hard! (and fun and very satisfying if you can do it AT THE END)

Great data scientist excels in twofold: science and engineering.

Science -> Why?
- Visualize your datasets (know what is X and y)
- Understand your datasets (where they are from, and how they are collected, and how they are potentially contaminated)
- Form hypotheses (only one group did this)
- Form an intuition which architecture would work well
  - CNN1D - good for getting spatial and temporal footprint; basically window-based classification
  - CNN1D + LSTM - if you believe that previous window affects the next window, then it's a good choice; good for signal
  - LSTM only - good for text, because previous text affects the next text; usually bad for signal, because each sample does not mean anything
  - CNN2D - good for any images
  - Attention - can be apply on top of CNN or LSTM or only attention; it's about correlations/similarity
- Master/Ph.D. thesis asks a lot of whys!  Every decision you make is okay that you don't know whether it's right or wrong (because you are still learning), but you all MUST have a clear "why" in your mind (don't do it because Chaky teaches you or it's something new)

Engineering - how?
- First try a simple model (e.g., SVM)
- Then try a simple neural network
- Monitor your progress
  - Loss plateau (if it is very steep or unstable, use these techniques)
    - learning rate, batch norm, momentum, Adam (adaptive learning algorithm)
  - Gradient variances (if your gradients are very small, or very big)
    - activation, weight initialization, skip connections, batch norm
  - Weights (if your weights are not uniform, or very similar)
    - weight initialization 
- Always MAKE SURE to overfit your training data
- Last thing to complete your model is to change your hyperparameters (quality of life perk)
- To counter overfitting, use regularization L1/L2, dropout, label smoothing, batch norm, skip connections     
- Keeping your results in tabular format (e.g., excel) is a really good way for communication
- How to train-test split is EXTREMELY important; but regardless of whatever way you do, please make sure you pass these different levels of tests (i.e., increasing difficulty): generalization across (1) within him/herself, (2) participants, (3) tasks, and (4) domain.
- Always reserve a testing set that is NEVER seen by the model
- Look for inspirations
  - Read papers; read 25 papers for good results, read 100 papers for breakthroughs
  - Look at github; many nice guys out there
- Deep learning is a craft (not entirely 100% science), so it is very normal to have a trial and error, but there is always something call "intuition" behind.  TA and myself ALSO don't have answers to your questions because there is no definite science behind most of these deep stuffs.
