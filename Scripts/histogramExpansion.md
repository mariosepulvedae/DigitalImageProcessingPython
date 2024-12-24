The histogram expansion allows to obtain intensity levels along the whole grayscale

It's similar to the line equation through two points:

$$\begin{align*}
\dfrac{s_{2}-s_{1}}{r_{2}-r_{1}}&=\dfrac{S-s_{1}}{R-r_{1}}\\
\displaystyle \Longrightarrow S&=\dfrac{s_{2}-s_{1}}{r_{2}-r_{1}}\left(R-r_{1}\right)+s_{1}\\
s_{2}&=L-1=255\\
s_{1}&=0\\
\Longrightarrow S&=\dfrac{255}{r_{2}-r_{1}}\left(R-r_{1}\right)
\end{align*}$$

![histogramExpansionFigure](https://github.com/user-attachments/assets/2b156e05-6711-47cd-b881-fffafa7e1285)

The Figure it's an own elaboration

