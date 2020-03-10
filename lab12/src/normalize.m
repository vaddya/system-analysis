model

% Target functions' mins
f1_min = -21;
f2_min = -6500;
f3_min = 16.45;
f4_min = 15.011;

% Normalized target functions
f1_norm = @(x) f1(x) / f1_min;
f2_norm = @(x) f2(x) / f2_min;
f3_norm = @(x) f3(x) / f3_min;
f4_norm = @(x) f4(x) / f4_min;
