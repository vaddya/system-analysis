% Target functions' mins
f1_min = -21;
f2_min = -6500;
f3_min = 16.45;
f4_min = 15.011;

% Normalized target functions
f1_norm = @(x) -x(4) / abs(f1_min);
f2_norm = @(x) (-200*x(3) - 100*x(4)) / abs(f2_min);
f3_norm = @(x) x(3) / abs(f3_min);
f4_norm = @(x) (0.01*x(2) + 0.1*x(3) + 1*x(4)) / abs(f4_min);

% Weights of target functinos
w = [0.3, 0.2, 0.2, 0.3];

% Additive convolution 
f = @(x) w(1)*f1_norm(x) + w(2)*f2_norm(x) + w(3)*f3_norm(x) + w(4)*f4_norm(x);

% Unequalities
A = [
    0,0,-1,1;
    -1,0,1,0;
    0,-10,0,1;
];
b = [0, 0, 0];

% Equalities
Aeq = [1,1,1,1];
beq = 100;

% Bounds
lb = [1,1,1,13];
ub = [65,2.1,22,99];