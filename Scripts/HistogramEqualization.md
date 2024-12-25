Sometimes, the histogram expansion is not enough or doesn't present the best result
To solve this problem, you can use the histogram equalization

$$\begin{equation}
s_{k}=T\left(r_{k} \right)=(L-1)  \displaystyle \sum_{j=0}^{k} p_{r}\left( r_{j} \right);\ k=0,\ 1,\ 2,\ ...,\ L-1
\end{equation}$$

This equation represents a new distribution for the intensity levels of the image

<p align="middle">
  <img src="/Images/equ1.png" height=200 width=200>
  <img src="/Images/equ2.png" height=200 width=200>
  <img src="/Images/equ3.png" height=200 width=200>
</p>
