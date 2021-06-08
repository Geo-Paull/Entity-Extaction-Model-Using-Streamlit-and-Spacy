# import pandas as pd
# import numpy as np
# import streamlit as st
# import time
#
# st.title("my first project")
#
# st.write("First attempt at using data to create a table")
# df = (pd.DataFrame({'x': [1, 2, 3, 4],
#                     'y': [10, 20, 30, 40]
#                    }))
# df
#
# #plotting a chart
# if st.checkbox('Show data'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])
#     chart_data
#
# #plotting a map
# if st.checkbox('Show map'):
#     map_data = pd.DataFrame(
#         np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#         columns=['lat', 'lon'])
#     st.map(map_data)
#
# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#      df['x'])
#
# 'Starting a long computation...'
#
# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
#
# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
#
# '...and now we\'re done!'
