# reverse-sampling

使用逆变换采样，从均匀分布采样后变换到目标条件分布
$$
\left\{\begin{array}{cc}
2^{k} f(x) & \text { if } p p f\left(\frac{i}{2^{k}}\right)<x<p p f\left(\frac{i+1}{2^{k}}\right), \\
0 & \text { otherwise. }
\end{array}\right.
$$
对比了逆变换采样、拒绝采样和截断正态分布采样的时间成本。
