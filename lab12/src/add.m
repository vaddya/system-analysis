normalize

% Weights of target functinos
w = [0.3,0.2,0.2,0.3];

% Additive convolution 
f_add = @(x) w(1)*f1_norm(x) + w(2)*f2_norm(x) + w(3)*f3_norm(x) + w(4)*f4_norm(x);
