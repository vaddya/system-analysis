normalize

f_minmax = @f_minmax_decl;

function f = f_minmax_decl (x)
    % Target functions
    f1 = @(x) -x(4);
    f2 = @(x) -200*x(3) - 100*x(4);
    f3 = @(x) x(3);
    f4 = @(x) 0.01*x(2) + 0.1*x(3) + 1*x(4);

    % Target functions' mins
    f1_min = -21;
    f2_min = -6500;
    f3_min = 16.45;
    f4_min = 15.011;

    % Normalized target functions
    f(1) = f1(x) / f1_min;
    f(2) = f2(x) / f2_min;
    f(3) = f3(x) / f3_min;
    f(4) = f4(x) / f4_min;
end
