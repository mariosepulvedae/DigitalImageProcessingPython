Sometimes, the histogram expansion is not enough or doesn't present the best result
To solve this problem, you can use the histogram equalization (Gonzalez & Woods, 2018)

$$\begin{equation}
s_{k}=T\left(r_{k} \right)=(L-1)  \displaystyle \sum_{j=0}^{k} p_{r}\left( r_{j} \right);\ k=0,\ 1,\ 2,\ ...,\ L-1
\end{equation}$$

This equation represents a new distribution for the intensity levels of the image

<p align="middle">
  <img src="/Images/equ4.png" height=200 width=200>
  <img src="/Images/equ5.png" height=200 width=200>
  <img src="/Images/equ6.png" height=200 width=200>
</p>

However, if you're still not convinced, you can also apply a histogram matching:

$$\begin{equation}
 \displaystyle G\left(z_{q}\right)=(L-1)\sum_{i=0}^{q} p_{z}\left( z_{i} \right);\  q=0,1,2,..., L-1
\end{equation}$$

With this equation you can modify the histogram distribution from R (original image) to another histogram with better distribution
(S), this will produce an image with the distributions of intensity levels you want

<p align="middle">
  <img src="/Images/equ1.png" height=200 width=200>
  <img src="/Images/equ2.png" height=200 width=200>
  <img src="/Images/equ3.png" height=200 width=200>
</p>
