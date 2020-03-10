normalize

% Powers of target functinos
k = [0.3,0.2,0.2,0.3];

% Multiplicative convolution 
f_mult = @(x) f1_norm(x)^k(1) * f2_norm(x)^k(2) * f3_norm(x)^k(3) * f4_norm(x)^k(4);
