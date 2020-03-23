#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:46:54 2020

@author: jingshuzheng
"""
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall *= (1 - 0.1) 
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= (1 + 0.05)
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= (1 - 0.05)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)

mon_sales = "121"
mon_sales = float(mon_sales)
tues_sales = "105"
tues_sales = float(tues_sales)
wed_sales = "110"
wed_sales = float(wed_sales)
thurs_sales = "98"
thurs_sales = float(thurs_sales)
fri_sales = "95"
fri_sales = float(fri_sales)
x = mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales
x = str(x)
print("This week\'s total sales: " + x )