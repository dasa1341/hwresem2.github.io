from matplotlib import pyplot as plt

U = 1; % Uniform stream
% GRID:
x = -2:.02:2;
y = -2:.02:2;
for m = 1:length(x)
for n = 1:length(y)
xx(m,n) = x(m); yy(m,n) = y(n);
% Velocity potential function:
phi UniFlow(m,n) = U * x(m);
% Stream function:
psi UniFlow(m,n) = U * y(n);
end
end
% Plots
% Uniform stream in x direction:
contour(xx,yy,psi UniFlow,[-2:.5:2],’k’),hold on
contour(xx,yy,phi UniFlow,[-10:1:5],’r’)
axis image,hold off
title(’Uniform stream in x direction’)
xlabel(’x’),ylabel(’y’