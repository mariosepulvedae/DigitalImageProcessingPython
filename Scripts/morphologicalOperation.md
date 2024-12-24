In this script i analyze the central pixel from $3\times 3$ neighborhoods in a binary image.

If there are 5 or more pixels equal to 1 around the central pixel, its value will be 1, otherwise, will be 0

$$\begin{align*}
\begin{bmatrix}
	1&1&1\\
	1&\text{\textcolor{purple}{\textbf{0}}}&0\\
	0&1&1
\end{bmatrix}
\Longrightarrow
\begin{bmatrix}
	1&1&1\\
	1&\text{\textcolor{purple}{\textbf{1}}}&0\\
	0&1&1
\end{bmatrix}
\end{align*} $$

