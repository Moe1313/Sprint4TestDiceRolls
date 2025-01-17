import scipy.stats
import streamlit as st
import time
import pandas as pd
#chart = st.line_chart([0.5])
chart = st.line_chart(pd.DataFrame({"Mean": [0.5]}))

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows(pd.DataFrame({"Mean": [mean]}))
        #chart.add_rows([mean])
        time.sleep(0.05)

    return mean

st.header('Tossing a Coin')

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
    mean = toss_coin(number_of_trials)