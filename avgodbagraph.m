figure;
pre_03_20_2014_5317_10s_d2 = timeseries(pre_03_20_2014_5317_10s_a2, pre_03_20_2014_5317_10s_t2);
pre_03_20_2014_5317_10s_d2.TimeInfo.Units = 'seconds';
pre_03_20_2014_5317_10s_d2.TimeInfo.Format = 'HH:MM';
pre_03_20_2014_5317_10s_d2.TimeInfo.StartDate = '03/20/2014 10:27:52';
p1 = plot(pre_03_20_2014_5317_10s_d2, 's-m', 'MarkerSize', 6);
%p1 = plot(pre_01_08_2014_5325_hp_d1)
title('Animal 5317 10-second-averaged ODBA(03-21-2014)')
ylabel('ODBA(g)')
%set(gca,'XTick', 0:1:24)
set(p1, 'Color', 'blue', 'LineWidth', 0.5)
grid on;
