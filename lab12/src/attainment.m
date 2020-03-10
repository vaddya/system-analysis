normalize

f = @(x) [f1(x), f2(x), f3(x), f4(x)];
goal = [f1_min, f2_min, f3_min, f4_min];
weights = abs(goal);
