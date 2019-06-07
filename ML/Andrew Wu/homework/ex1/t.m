clear ; close all; clc

fprintf('Loading data ...\n');
data = load('ex1data2.txt');
X = data(:, 1:2);
y = data(:, 3);
m = length(y);

%[X mu sigma] = featureNormalize(X);

a = raw(X)
