% Target functions
f1 = @(x) -x(4);
f2 = @(x) -200*x(3) - 100*x(4);
f3 = @(x) x(3);
f4 = @(x) 0.01*x(2) + 0.1*x(3) + 1*x(4);

% Unequalities
A = [
    0,0,-1,1;
    -1,0,1,0;
    0,-10,0,1;
];
b = [0,0,0];

% Equalities
Aeq = [1,1,1,1];
beq = 100;

% Bounds
lb = [1,1,1,13];
ub = [65,2.1,22,99];
