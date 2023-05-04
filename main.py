import numpy as np
import pandas as pd
# coding: utf-8

cgm_data = pd.read_csv('CGMData.csv',
                       low_memory=False, usecols=['Date', 'Time', 'Sensor Glucose (mg/dL)'])
insulin_data = pd.read_csv(
    'InsulinData.csv', low_memory=False)

cgm_data['date_time_stamp'] = pd.to_datetime(
    cgm_data['Date'] + ' ' + cgm_data['Time'])

insulin_data['date_time_stamp'] = pd.to_datetime(
    insulin_data['Date'] + ' ' + insulin_data['Time'])

start_of_am = insulin_data.sort_values(
    by='date_time_stamp', ascending=True).loc[insulin_data['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF'].iloc[0]['date_time_stamp']

cgm_data = cgm_data.dropna(
    subset=['Sensor Glucose (mg/dL)'], how='all')

cg_data = cgm_data.groupby('Date')[
    'Sensor Glucose (mg/dL)'].count().where(lambda x: x >= 230.4).dropna().index.tolist()

cgm_data = cgm_data.loc[cgm_data['Date'].isin(cg_data)]

am_data_df = cgm_data.sort_values(
    by='date_time_stamp', ascending=True).loc[cgm_data['date_time_stamp'] >= start_of_am]
mm_data_df = cgm_data.sort_values(
    by='date_time_stamp', ascending=True).loc[cgm_data['date_time_stamp'] < start_of_am]

am_data_df = am_data_df.set_index(
    'date_time_stamp')

percent_hyperglycemia_fullday_am = (am_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_midday_am = (am_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_nighttime_am = (am_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_critical_fullday_am = (am_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_critical_midday_am = (am_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_critical_nighttime_am = (am_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_fullday_am = (am_data_df.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    am_data_df['Sensor Glucose (mg/dL)'] >= 70) & (am_data_df['Sensor Glucose (mg/dL)'] <= 180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_midday_am = (am_data_df.between_time('6:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    am_data_df['Sensor Glucose (mg/dL)'] >= 70) & (am_data_df['Sensor Glucose (mg/dL)'] <= 180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_nighttime_am = (am_data_df.between_time('0:00:00', '05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    am_data_df['Sensor Glucose (mg/dL)'] >= 70) & (am_data_df['Sensor Glucose (mg/dL)'] <= 180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_sec_fullday_am = (am_data_df.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    am_data_df['Sensor Glucose (mg/dL)'] >= 70) & (am_data_df['Sensor Glucose (mg/dL)'] <= 150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_sec_midday_am = (am_data_df.between_time('6:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    am_data_df['Sensor Glucose (mg/dL)'] >= 70) & (am_data_df['Sensor Glucose (mg/dL)'] <= 150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

percent_range_sec_nighttime_am = (am_data_df.between_time('0:00:00', '05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    am_data_df['Sensor Glucose (mg/dL)'] >= 70) & (am_data_df['Sensor Glucose (mg/dL)'] <= 150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

percent_hypoglycemia_lv1_fullday_am = (am_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv1_midday_am = (am_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv1_nighttime_am = (am_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv2_fullday_am = (am_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv2_midday_am = (am_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv2_nighttime_am = (am_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[am_data_df['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

mm_data_df = mm_data_df.set_index(
    'date_time_stamp')

percent_hyperglycemia_fullday_manual = (mm_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_midday_manual = (mm_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)

percent_hyperglycemia_nighttime_manual = (mm_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] > 180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_critical_fullday_manual = (mm_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_critical_midday_manual = (mm_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hyperglycemia_critical_nighttime_manual = (mm_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] > 250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_fullday_manual = (mm_data_df.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    mm_data_df['Sensor Glucose (mg/dL)'] >= 70) & (mm_data_df['Sensor Glucose (mg/dL)'] <= 180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_time_midday_manual = (mm_data_df.between_time('6:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    mm_data_df['Sensor Glucose (mg/dL)'] >= 70) & (mm_data_df['Sensor Glucose (mg/dL)'] <= 180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_time_nighttime_manual = (mm_data_df.between_time('0:00:00', '05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    mm_data_df['Sensor Glucose (mg/dL)'] >= 70) & (mm_data_df['Sensor Glucose (mg/dL)'] <= 180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_sec_fullday_manual = (mm_data_df.between_time('0:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    mm_data_df['Sensor Glucose (mg/dL)'] >= 70) & (mm_data_df['Sensor Glucose (mg/dL)'] <= 150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_sec_midday_manual = (mm_data_df.between_time('6:00:00', '23:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    mm_data_df['Sensor Glucose (mg/dL)'] >= 70) & (mm_data_df['Sensor Glucose (mg/dL)'] <= 150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_range_sec_nighttime_manual = (mm_data_df.between_time('0:00:00', '05:59:59')[['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[(
    mm_data_df['Sensor Glucose (mg/dL)'] >= 70) & (mm_data_df['Sensor Glucose (mg/dL)'] <= 150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv1_fullday_manual = (mm_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv1_midday_manual = (mm_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv1_nighttime_manual = (mm_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] < 70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv2_fullday_manual = (mm_data_df.between_time('0:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv2_midday_manual = (mm_data_df.between_time('6:00:00', '23:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


percent_hypoglycemia_lv2_nighttime_manual = (mm_data_df.between_time('0:00:00', '05:59:59')[
    ['Date', 'Time', 'Sensor Glucose (mg/dL)']].loc[mm_data_df['Sensor Glucose (mg/dL)'] < 54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


results_df = pd.DataFrame({'percent_hyperglycemia_nighttime': [percent_hyperglycemia_nighttime_manual.mean(axis=0), percent_hyperglycemia_nighttime_am.mean(axis=0)],


                           'percent_hyperglycemia_critical_nighttime': [percent_hyperglycemia_critical_nighttime_manual.mean(axis=0), percent_hyperglycemia_critical_nighttime_am.mean(axis=0)],


                           'percent_range_nighttime': [percent_time_nighttime_manual.mean(axis=0), percent_range_nighttime_am.mean(axis=0)],


                           'percent_range_sec_nighttime': [percent_range_sec_nighttime_manual.mean(axis=0), percent_range_sec_nighttime_am.mean(axis=0)],


                           'percent_hypoglycemia_lv1_nighttime': [percent_hypoglycemia_lv1_nighttime_manual.mean(axis=0), percent_hypoglycemia_lv1_nighttime_am.mean(axis=0)],


                           'percent_hypoglycemia_lv2_nighttime': [np.nan_to_num(percent_hypoglycemia_lv2_nighttime_manual.mean(axis=0)), percent_hypoglycemia_lv2_nighttime_am.mean(axis=0)],
                           'percent_hyperglycemia_midday': [percent_hyperglycemia_midday_manual.mean(axis=0), percent_hyperglycemia_midday_am.mean(axis=0)],
                           'percent_hyperglycemia_critical_midday': [percent_hyperglycemia_critical_midday_manual.mean(axis=0), percent_hyperglycemia_critical_midday_am.mean(axis=0)],
                           'percent_range_midday': [percent_time_midday_manual.mean(axis=0), percent_range_midday_am.mean(axis=0)],
                           'percent_range_sec_midday': [percent_range_sec_midday_manual.mean(axis=0), percent_range_sec_midday_am.mean(axis=0)],
                           'percent_hypoglycemia_lv1_midday': [percent_hypoglycemia_lv1_midday_manual.mean(axis=0), percent_hypoglycemia_lv1_midday_am.mean(axis=0)],
                           'percent_hypoglycemia_lv2_midday': [percent_hypoglycemia_lv2_midday_manual.mean(axis=0), percent_hypoglycemia_lv2_midday_am.mean(axis=0)],


                           'percent_hyperglycemia_fullday': [percent_hyperglycemia_fullday_manual.mean(axis=0), percent_hyperglycemia_fullday_am.mean(axis=0)],
                           'percent_hyperglycemia_critical_fullday': [percent_hyperglycemia_critical_fullday_manual.mean(axis=0), percent_hyperglycemia_critical_fullday_am.mean(axis=0)],
                           'percent_range_fullday': [percent_range_fullday_manual.mean(axis=0), percent_range_fullday_am.mean(axis=0)],
                           'percent_range_sec_fullday': [percent_range_sec_fullday_manual.mean(axis=0), percent_range_sec_fullday_am.mean(axis=0)],
                           'percent_hypoglycemia_lv1_fullday': [percent_hypoglycemia_lv1_fullday_manual.mean(axis=0), percent_hypoglycemia_lv1_fullday_am.mean(axis=0)],
                           'percent_hypoglycemia_lv2_fullday': [percent_hypoglycemia_lv2_fullday_manual.mean(axis=0), percent_hypoglycemia_lv2_fullday_am.mean(axis=0)]


                           },
                          index=['mm', 'am'])


results_df.to_csv('Results.csv', header=False, index=False)
